import random
from .magic import Spell


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class formatting:
    INDENT = '    '
    NEWLINE = '\n'
    WHITESPACE = ' '
    UNDERLINE = '_'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ['Attack', 'Magic', 'Items']

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp +=dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print(f'{formatting.NEWLINE}{bcolors.BOLD}{formatting.WHITESPACE*4}{self.name}:{bcolors.ENDC}')
        print(f"{bcolors.OKBLUE}{bcolors.BOLD}{formatting.WHITESPACE*4}ACTIONS:{bcolors.ENDC}")
        for item in self.actions:
            print(f'{formatting.INDENT*2}{i}. {item}')
            i += 1

    def choose_magic(self):
        i = 1
        print(f"{formatting.NEWLINE}{bcolors.OKBLUE}{bcolors.BOLD}{formatting.WHITESPACE*4}MAGIC:{bcolors.ENDC}")
        for spell in self.magic:
            print(f'{formatting.INDENT*2}{i}. {spell.name} (cost: {spell.cost})')
            i += 1

    def choose_items(self):
        i = 1
        print(f"{formatting.NEWLINE}{bcolors.OKGREEN}{bcolors.BOLD}{formatting.WHITESPACE*4}ITEMS:{bcolors.ENDC}")
        for item in self.items:
            print(f'{formatting.INDENT*2}{i}. {item["item"].name}: {item["item"].description} (x{item["quantity"]})')
            i += 1

    def choose_target(self, enemies):
        i = 1
        print(f'{formatting.NEWLINE}{bcolors.FAIL}{bcolors.BOLD}{formatting.WHITESPACE * 4}TARGET:{bcolors.ENDC}')
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print(f'{formatting.WHITESPACE *8}{i}. {enemy.name}')
                i += 1
        choice = int(input(f'{formatting.WHITESPACE * 4}Choose target: ')) - 1
        return choice


    def get_enemy_stats(self):
        hp_bar = ''
        bar_ticks = (self.hp / self.maxhp) * 100 / 2

        while bar_ticks > 0:
            hp_bar += '█'
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += ' '

        hp_string = f'{self.hp}/{self.maxhp}'
        current_hp = ''

        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)

            while decreased > 0:
                current_hp += ' '
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        print(
            f'{formatting.WHITESPACE * 27}{formatting.UNDERLINE * 50}')
        print(f'{bcolors.BOLD}{self.name}:{formatting.WHITESPACE * 5}'
              f'{current_hp}{formatting.WHITESPACE * 4}|{bcolors.FAIL}{hp_bar}{bcolors.ENDC}|'
              f'{formatting.WHITESPACE * 6}')

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 100 / 10

        while bar_ticks > 0:
            hp_bar += '█'
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += ' '

        while mp_ticks > 0:
            mp_bar += '█'
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += ' '

        hp_string = f'{self.hp}/{self.maxhp}'
        current_hp = ''

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += ' '
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = f'{self.mp}/{self.maxmp}'
        current_mp = ''

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)
            while decreased > 0:
                current_mp += " "
                decreased -= 1

            current_mp += mp_string

        else:
            current_mp = mp_string

        print(f'{formatting.WHITESPACE*28}{formatting.UNDERLINE*25}{formatting.WHITESPACE*16}'
              f'{formatting.UNDERLINE*10}')
        print(f'{bcolors.BOLD}{self.name}:        '
              f'{current_hp}    |{bcolors.OKGREEN}{hp_bar}{bcolors.ENDC}|      '
              f'{current_mp} |{bcolors.OKBLUE}{mp_bar}{bcolors.ENDC}|')

