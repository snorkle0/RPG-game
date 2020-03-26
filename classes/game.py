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

    def get_stats(self):
        print(f'{formatting.WHITESPACE*26}{formatting.UNDERLINE*25}{formatting.WHITESPACE*13}{formatting.UNDERLINE*10}')
        print(f'{bcolors.BOLD}{self.name}:        '
              f'{self.hp}/{self.maxhp}    |{bcolors.OKGREEN}████████████            {bcolors.ENDC}|      '
              f'{bcolors.BOLD}{self.mp}/{self.maxmp} |{bcolors.OKBLUE}██████████{bcolors.ENDC}|')

