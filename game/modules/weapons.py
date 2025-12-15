import time as t
import os as o
import random as r
import keyboard as k 
import json as j

class weapons():
    def __init__(self, name, type, rarity, damage, effects, piercing, splash_damage, splash_range, crit_chance, duplicates):
        self.name = name
        self.type = type
        self.rarity = rarity
        self.damage = damage
        self.effects = effects
        self.piercing = piercing
        self.splash_damage = splash_damage
        self.splash_range = splash_range
        self.crit_chance = crit_chance
        self.duplicates = duplicates
    def upgrade(self):
        if self.rarity == "Common":
            if self.duplicates >= 6:
                self.duplicates -= 5
                self.rarity = "Uncommon"
        if self.rarity == "Uncommon":
            if self.duplicates >= 11:
                self.duplicates -= 10
                self.rarity = "Rare"
        if self.rarity == "Rare":
            if self.duplicates >= 21:
                self.duplicates -= 20
                self.rarity = "Epic"
        if self.rarity == "Epic":
            if self.duplicates >= 51:
                self.duplicates -= 50
                self.rarity = "Legendary"
    def add_duplicates(self, num_to_add):
        self.duplicates += num_to_add
    def refresh(self):
        if self.type == "Fighter":
            if self.name == "Sword":
                self.name = "Sword"
                self.splash_range = 0
                self.splash_damage = 0
                if self.rarity == "Common":
                    self.damage = 2
                    self.piercing = 1
                    self.crit_chance = 10
                elif self.rarity == "Uncommon":
                    self.damage = 3
                    self.piercing = 2
                    self.crit_chance = 15
                elif self.rarity == "Rare":
                    self.damage = 4
                    self.piercing = 3
                    self.crit_chance = 20
                elif self.rarity == "Epic":
                    self.damage = 6
                    self.piercing = 3
                    self.crit_chance = 33
                elif self.rarity == "Legendary":
                    self.damage = 10
                    self.piercing = 4
                    self.crit_chance = 50
            elif self.name == "Greatsword":
                self.name = "Greatsword"
                self.piercing = 0
                if self.rarity == "Common":
                    self.damage = 2
                    self.splash_damage = 1
                    self.splash_range = 2
                    self.crit_chance = 5
                elif self.rarity == "Uncommon":
                    self.damage = 2
                    self.splash_damage = 2
                    self.splash_range = 2
                    self.crit_chance = 10
                elif self.rarity == "Rare":
                    self.damage = 4
                    self.splash_damage = 3
                    self.splash_range = 2
                    self.crit_chance = 15
                elif self.rarity == "Epic":
                    self.damage = 6
                    self.splash_damage = 4
                    self.splash_range = 3
                    self.crit_chance = 35
                elif self.rarity == "Legendary":
                    self.damage = 10
                    self.splash_damage = 8
                    self.splash_range = 6
                    self.crit_chance = 40
            if self.name == "Mace":
                self.piercing = 0
                if self.rarity == "Common":
                    self.damage = 3
                    self.splash_damage = 1
                    self.splash_range = 1
                    self.crit_chance = 1
                elif self.rarity == "Uncommon":
                    self.damage = 5
                    self.splash_damage = 2
                    self.splash_range = 1
                    self.crit_chance = 5
                elif self.rarity == "Rare":
                    self.damage = 8
                    self.splash_damage = 3
                    self.splash_range = 1
                    self.crit_chance = 15
                elif self.rarity == "Epic":
                    self.damage = 10
                    self.splash_damage = 4
                    self.splash_range = 2
                    self.crit_chance = 20
                elif self.rarity == "Legendary":
                    self.damage = 12
                    self.splash_damage = 4
                    self.splash_range = 3
                    self.crit_chance = 40 
            if self.name == "Spear":
                self.splash_damage = 0
                self.splash_range = 0
                if self.rarity == "Common":
                    self.damage = 1
                    self.piercing = 3
                    self.crit_chance = 5
                elif self.rarity == "Uncommon":
                    self.damage = 2
                    self.piercing = 4
                    self.crit_chance = 15
                elif self.rarity == "Rare":
                    self.damage = 3
                    self.piercing = 6
                    self.crit_chance = 30
                elif self.rarity == "Epic":
                    self.damage = 4
                    self.piercing = 10
                    self.crit_chance = 50
                elif self.rarity == "Lgendary":
                    self.damage = 8
                    self.piercing = 12
                    self.crit_chance = 70
            elif self.name == "Dagger":
                self.splash_range = 0
                self.splash_damage = 0
                if self.rarity == "Common":
                    self.damage = 1
                    self.piercing = 0
                    self.crit_chance = 30
                elif self.rarity == "Uncommon":
                    self.damage = 4
                    self.piercing = 0
                    self.crit_chance = 35
                elif self.rarity == "Rare":
                    self.damage = 8
                    self.piercing = 0
                    self.crit_chance = 40
                elif self.rarity == "Epic":
                    self.damage = 14
                    self.piercing = 0
                    self.crit_chance = 45
                elif self.rarity == "Legendary":
                    self.damage = 20
                    self.piercing = 1
                    self.crit_chance = 50
            elif self.name == "Nunchucks":
                self.name = "Nunchucks"
                self.piercing = 0
                if self.rarity == "Common": 
                    self.damage = 1
                    self.splash_damage = 1
                    self.splash_range = 3
                    self.crit_chance = 40
                elif self.rarity == "Uncommon":
                    self.damage = 2
                    self.splash_damage = 1
                    self.splash_range = 5
                    self.crit_chance = 60
                elif self.rarity == "Rare":
                    self.damage = 4
                    self.splash_damage = 2
                    self.splash_damage = 7
                    self.crit_chance = 70
                elif self.rarity == "Epic":
                    self.damage = 6
                    self.splash_damage = 4
                    self.splash_range = 9
                    self.crit_chance = 80
                elif self.rarity == "Legendary":
                    self.damage = 8
                    self.splash_damage = 6
                    self.splash_range = 15
        elif self.type == "Wizard":
            self.crit_chance = 0
            self.piercing = 0
            if self.name == "Fireball":
                if "Burning" not in self.effects:
                    self.effects.append("Burning")
                if self.rarity == "Common":
                    self.damage = 3
                    self.splash_damage = 1
                    self.splash_range = 3
                elif self.rarity == "Uncommon":
                    self.damage = 4
                    self.splash_damage = 2
                    self.splash_range = 4
                elif self.rarity == "Rare":
                    self.damage = 6
                    self.splash_damage = 3
                    self.splash_range = 5
                elif self.rarity == "Epic":
                    self.damage = 8
                    self.splash_damage = 6
                    self.splash_range = 6 
                elif self.rarity == "Legendary":
                    self.damage = 10
                    self.splash_damage = 8
                    self.splash_range = 8
            elif self.name == "Snowball":
                if ""
            
    def define(self):
        print(f"Name: {self.name}, Type: {self.type}, Rarity: {self.rarity}, Damage: {self.damage}, Effects: {self.effects}, Piercing: {self.piercing}, Splash Damage: {self.splash_damage}, Splash Range: {self.splash_range}, Crit Chance: {self.crit_chance}, Duplicates: {self.duplicates}")
            
sword = weapons("Sword", "Fighter", "Common", 2, [], 1, 0, 0, 10, 0)
greatsword = weapons("Greatsword", "Fighter", "Common", 2, [], 0, 1, 1, 5, 0)
mace = weapons("Mace", "Fighter", "Common", 5, [], 0, 1, 1, 1, 0)
spear = weapons("Spear", "Fighter", "Common", 1, [], 3, 0, 0, 5, 0)
dagger = weapons("Dagger", "Fighter", "Common", 1, [], 0, 0, 0, 30, 0)
nunchucks = weapons("Nunchucks", "Fighter", "Common", 3, [], 0, 1, 1, 40, 0)

fireball = weapons("Fireball", "Wizard", "Common", 3, ["Burning"], 0, 1, 3, 0, 0)

all_weapons = [sword, greatsword, mace, spear, dagger, nunchucks, fireball]

print(len(all_weapons))

for count in range(0, len(all_weapons) + 0):
    all_weapons[count].define()
    print()