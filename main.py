from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

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
player_items = [potion, hipotion, superpotion, elixir, megaelixir, grenade]

# Instantiate People:
player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + 'AN ENEMY ATTACKS!' + bcolors.ENDC)

while running:
    print('==================')
    player.choose_action()
    choice = input('Choose action: ')
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(f'You attacked for {dmg} points of damage.')
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input('Choose magic: ')) - 1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(f'{bcolors.FAIL}\nNot enough MP\n {bcolors.ENDC}')
            continue

        player.reduce_mp(spell.cost)

        if spell.type == 'White':
            player.heal(magic_dmg)
            print(f'{bcolors.OKBLUE}\n{spell.name} heals for {magic_dmg} HP.{bcolors.ENDC}')
        elif spell.type == 'Black':
            enemy.take_damage(magic_dmg)
            print(f'{bcolors.OKBLUE} \n{spell.name} deals {magic_dmg} points of damage {bcolors.ENDC}')
    elif index == 2:
        if not player.items:
            print('You have no items.')
            continue
        player.choose_items()
        item_choice = int(input('Choose item: ')) - 1





    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print(f'Enemy attacks for {enemy_dmg}')

    print('--------------------------------------------------')
    print(f'Enemy HP: {bcolors.FAIL} {enemy.get_hp()} / {enemy.get_max_hp()} {bcolors.ENDC} \n')
    print(f'Your HP: {bcolors.OKGREEN} {player.get_hp()} / {player.get_max_hp()} {bcolors.ENDC}')
    print(f'Your MP: {bcolors.OKBLUE} {player.get_mp()} / {player.get_max_mp()} {bcolors.ENDC}')

    if enemy.get_hp() == 0:
        print(f'{bcolors.OKGREEN}You win!{bcolors.ENDC}')
        running = False
    elif player.get_hp() == 0:
        print(f'{bcolors.FAIL}Your enemy has defeated you!{bcolors.ENDC}')
        running = False

