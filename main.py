from classes.game import Person, bcolors, formatting
from classes.magic import Spell
from classes.inventory import Item
import random

# Create Black Magic:
fire = Spell('Fire', 10, 100, 'Black')
thunder = Spell('Thunder', 15, 150, 'Black')
blizzard = Spell('Blizzard', 10, 100, 'Black')
meteor = Spell('Meteor', 20, 200, 'Black')
quake = Spell('Quake', 14, 140, 'Black')

# Create White Magic:
cure = Spell('Cure', 12, 120, 'White')
cura = Spell('Cura', 18, 200, 'White')

# Create some Items:
potion = Item('Potion', 'potion', 'Heals 50 HP', 50)
hipotion = Item('Hi-Potion', 'potion', 'Heals 100 HP', 100)
superpotion = Item('Super Potion', 'potion', 'Heals 500 HP', 500)
elixir = Item('Elixir', 'elixir', 'Fully restores HP/MP of one Party Member', 9999)
megaelixir = Item('MegaElixir', 'elixir', "Fully restores party's HP/MP", 9999)

grenade = Item('Grenade', 'attack', 'Deals 500 damage', 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
enemy_spells = [fire, meteor, cure]
player_items = [{'item': potion, 'quantity': 15}, {'item': hipotion, 'quantity': 5}, {'item': superpotion, 'quantity': 1},
                {'item': elixir, 'quantity': 5}, {'item': megaelixir, 'quantity': 1}, {'item': grenade, 'quantity': 10}]

# Instantiate People:
player1 = Person("Valos", 1200, 65, 150, 34, player_spells, player_items)
player2 = Person("Nick ", 4000, 65, 200, 34, player_spells, player_items)
player3 = Person("Robot", 4000, 65, 300, 34, player_spells, player_items)

enemy2 = Person("Imp  ", 1250, 130, 560, 325, enemy_spells, [])
enemy1 = Person("Magus", 11200, 65, 600, 25, enemy_spells, [])
enemy3 = Person("Imp  ", 1250, 130, 560, 325, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + 'AN ENEMY ATTACKS!' + bcolors.ENDC)
while running:
    print('==================')

    print(f'{formatting.NEWLINE}')
    print(f'NAME{formatting.WHITESPACE*21}HP{formatting.WHITESPACE*37}MP')

    for player in players:
        player.get_stats()

    print(f'{formatting.NEWLINE}')

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input(f'{formatting.INDENT}Choose action: ')
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)

            enemies[enemy].take_damage(dmg)
            print(f'{player.name} attacked {enemies[enemy].name.strip()} for {dmg} points of damage.')

            if enemies[enemy].get_hp() == 0:
                print(f'{enemies[enemy].name.strip()} has died.')
                enemies.pop(enemy)

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input(f'{formatting.INDENT}Choose magic: ')) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(f'{bcolors.FAIL}{formatting.NEWLINE}Not enough MP{formatting.NEWLINE}{bcolors.ENDC}')
                continue

            player.reduce_mp(spell.cost)

            if spell.type == 'White':
                player.heal(magic_dmg)
                print(f'{bcolors.OKBLUE}{formatting.NEWLINE}{player.name} {spell.name}'
                      f' heals for {magic_dmg} HP.{bcolors.ENDC}')
            elif spell.type == 'Black':

                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(magic_dmg)
                print(f'{bcolors.OKBLUE}{formatting.NEWLINE}{player.name}\'s {spell.name}'
                      f' deals {magic_dmg} points of damage{bcolors.ENDC} to {enemies[enemy].name.strip()}')

                if enemies[enemy].get_hp() == 0:
                    print(f'{enemies[enemy].name.strip()} has died.')
                    enemies.pop(enemy)

        elif index == 2:
            if not player.items:
                print('You have no items.')
                continue
            player.choose_items()
            item_choice = int(input(f'{formatting.INDENT}Choose item: ')) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            player.items[item_choice]["quantity"] -= 1

            if player.items[item_choice]["quantity"] == 0:
                player.items.pop(item_choice)
                print(f'{bcolors.WARNING}That was the last {item.name}!{bcolors.ENDC}')

            if item.type == 'potion':
                player.heal(item.prop)
                print(f'{bcolors.OKGREEN}{formatting.NEWLINE}{item.name} heals for {item.prop} HP{bcolors.ENDC}')
            elif item.type == 'elixir':

                if item.name == 'megaelixir':
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                        print(f'{bcolors.OKGREEN}{formatting.NEWLINE}{item.name}Party HP/MP has been fully restored.{bcolors.ENDC}')
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                    print(f'{bcolors.OKGREEN}{formatting.NEWLINE}{item.name} fully restored HP/MP{bcolors.ENDC}')
            elif item.type == "attack":
                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(item.prop)

                print(f'{bcolors.FAIL}{formatting.NEWLINE}{item.name} deals {item.prop} points of damage{bcolors.ENDC} '
                      f'to {enemies[enemy].name.strip()}')

                if enemies[enemy].get_hp() == 0:
                    print(f'{enemies[enemy].name.strip()} has died.')
                    enemies.pop(enemy)

    # Check if battle is over
    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    # Check if Player won
    if defeated_enemies == 3:
        print(f'{bcolors.OKGREEN}You win!{bcolors.ENDC}')
        running = False

    # Check if Enemy won
    elif defeated_players == 3:
        print(f'{bcolors.FAIL}Your enemies have defeated you!{bcolors.ENDC}')
        running = False

    print(f'{formatting.NEWLINE}')
    # Enemy attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)

        # Chose attack
        if enemy_choice == 0:
            target = random.randrange(0, 3)
            enemy_dmg = enemy.generate_damage()
            players[target].take_damage(enemy_dmg)
            print(f'{enemy.name.strip()} attacks {players[target].name.strip()} for {enemy_dmg}')

        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            if spell.type == 'White':
                enemy.heal(magic_dmg)
                print(f'{bcolors.OKBLUE}{enemy.name} {spell.name}'
                      f' heals for {magic_dmg} HP.{bcolors.ENDC}')
            elif spell.type == 'Black':

                target = random.randrange(0, 3)

                players[target].take_damage(magic_dmg)
                print(f'{bcolors.OKBLUE}{formatting.NEWLINE}{enemy.name}\'s {spell.name}'
                      f' deals {magic_dmg} points of damage to {players[target].name.strip()}{bcolors.ENDC}')

                if players[target].get_hp() == 0:
                    print(f'{players[target].name.strip()} has died.')
                    players.pop(target)

            # print(f'Enemy chose {spell}, magic damage is {magic_dmg}')

