import time as t
import os as o
import random as r
import keyboard as k
import json as j 

def menu_basic(previous_location_function):
    global health, energy, gold, inventory
    rp("Basic Information:", 0.5)
    rp(f"Health: {health}", 0.5)
    rp(f"Energy: {energy}", 0.5)
    rp(f"Gold: {gold}", 0.5)
    rp(f"Inventory: {inventory}", 0.5, True)
    menu_home(previous_location_function)

def menu_armour(previous_location_function):
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    rp("Armour Information:", 0.5)
    rp(f"Armour Base: {armour_base}", 0,5)
    rp(f"Armour Plating: {armour_plate}", 0.5)
    rp(f"Armour Lining: {armour_lining}", 0.5, True)
    rp("Would You Like To Change Your Armour 'BASE', 'PLATING', 'LINING' Or 'EXIT'")
    armour_change = str(input())
    if armour_change == "BASE":
        rp(f"You Have {armour_base_available} Armour Bases Available", 1)
        rp("To Select An Armour Please Type It How It Shown Above Else Type 'EXIT'")
        select_armour_base = str(input())
        print()
        t.sleep(1)
        if select_armour_base in armour_base_available:
            armour_base_available.append(armour_base)
            armour_base = select_armour_base
            armour_base_available.pop(select_armour_base)
            rp(f"{select_armour_base} Has Been Applied", 1, True)
            menu_armour(previous_location_function)
        else:
            menu_armour(previous_location_function)
    if armour_change == "PLATING":
        rp(f"You Have {armour_plate_available} Armour Platings Available", 1)
        rp("To Select An Armour Please Type It How It Shown Above Else Type 'EXIT'")
        select_armour_plate = str(input())
        print()
        t.sleep(1)
        if select_armour_plate in armour_plate_available:
            armour_plate_available.append(armour_plate)
            armour_plate = select_armour_plate
            armour_plate_available.pop(select_armour_plate)
            rp(f"{select_armour_plate} Has Been Applied", 1, True)
            menu_armour(previous_location_function)
        else:
            menu_armour(previous_location_function)
    if armour_change == "BASE":
        rp(f"You Have {armour_lining_available} Armour Bases Available", 1)
        rp("To Select An Armour Please Type It How It Shown Above Else Type 'EXIT'")
        select_armour_lining = str(input())
        print()
        t.sleep(1)
        if select_armour_lining in armour_lining_available:
            armour_lining_available.append(armour_lining)
            armour_lining = select_armour_lining
            armour_lining_available.pop(select_armour_lining)
            rp(f"{select_armour_lining} Has Been Applied", 1, True)
            menu_armour(previous_location_function)
        else:
            menu_armour(previous_location_function)
    else:
        menu_home(previous_location_function)

def menu_class(previous_location_function):
    global class_, weapon, spell, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    if class_ == "wizard":
        rp("You Are A Wizard", 1)
        rp("You Fight With Spells", 1)
        if spell == "fireball":
            rp("Your Selected Spell Is Fireball", 1)
        elif spell == "iceball":
            rp("Your Selected Spell Is Iceball", 1)
        elif spell == "time_freeze":
            rp("Your Selected Spell Is Time Freeze", 1)
        elif spell == "bludgeon":
            rp("Your Selected Spell If Bludgeon", 1)
        elif spell == "electric":
            rp("Your Selected Spell Is Electric", 1)
        elif spell == "poison":
            rp("Your Selected Spell If Poison", 1)
    elif class_ == "fighter":
        rp("You Are A Fighter", 1)
        rp("You Fight With Unique Weapons", 1)
        if weapon == "none":
            rp("Your Selected Weapon Is Your Fists", 1)
        elif spell == "sword":
            rp("Your Selected Weapon Is A Sword", 1)
        elif spell == "spear":
            rp("Your Selected Weapon Is A Spear", 1)
        elif spell == "dagger":
            rp("Your Selected Weapon Is A Dagger", 1)
        elif spell == "mace":
            rp("Your Selected Weapon Is A Mace", 1)
        elif spell == "nunchuncks":
            rp("Your Selected Weapon Is Nunchuncks", 1)  
    elif class_ == "brawler":
        rp("You Are A Brawler", 1)
        rp("You Fight With Unique Moves", 1)
        if arrow == "none":
            rp("Your Selected Move Is A Basic Punch", 1)
        elif arrow == "fly_kick":
            rp("Your Selected Arrow Is A Flying Kick", 1)
        elif arrow == "1inch_punch":
            rp("Your Selected Arrow Is The One Inch Punch", 1)
        elif arrow == "flurry_punch":
            rp("Your Selected Arrow Is A Flurry Of Punches", 1)
        elif arrow == "flip_kick":
            rp("Your Selected Arrow Is A Flip Kick", 1)
        elif arrow == "sweep_kick":
            rp("Your Selected Arrow Is A Sweeping Kick", 1)
    elif class_ == "archer":
        rp("You Are An Archer", 1)
        rp("You Fight With Unique Arrows", 1)
        if arrow == "none":
            rp("Your Selected Arrow Is A Basic Tip", 1)
        elif arrow == "poison":
            rp("Your Selected Arrow Is A Poison Tip", 1)
        elif arrow == "flame":
            rp("Your Selected Arrow Is A Flaming Arrow", 1)
        elif arrow == "frozen":
            rp("Your Selected Arrow Is A Freezing Tip", 1)
        elif arrow == "conductor":
            rp("Your Selected Arrow Is A Conductive Tip", 1)
        elif arrow == "drill":
            rp("Your Selected Arrow Is A Drill Tip", 1)
    rp("To Change Class Type 'CLASS' or Spell Type 'SPELL' Otherwise Type 'BACK'", )
    class_choice = str(input())
    print()
    t.sleep(1)
    if class_choice == "CLASS":
        menu_class_change(previous_location_function)
    elif class_choice == "SPELL":
        menu_class_weapon_change(previous_location_function)
   
def menu_class_change(previous_location_function):
    global class_, class_available
    rp(f"You Are Currently A {class_}", 1)
    if len(class_available) == 0:
        rp("You Have No Available Classes To Change Too", 1)
        rp("Going Back", 1, True)
        menu_class(previous_location_function)
    else:
        rp(f"You Can Change Into: {class_available}", 1)
        rp("To Change Class Type It As Seen Above")
        change_class = str(input())
        print()
        t.sleep(1)
        if change_class in class_available:
            class_available.append(class_)
            class_ = change_class
            class_available.pop(change_class)
            rp(f"You Are Now A {class_}", 1)
            rp("Going Back", 1, True)
            menu_class(previous_location_function)
        else:
            rp("That Wasn't An Option", 1)
            rp("Going Back", 1, True)
            menu_class(previous_location_function)
           
def menu_class_weapon_change(previous_location_function):
    global class_, spell, weapon, arrow, skill
    global spell_available, weapon_available, arrow_available, skill_available
    if class_ == "wizard":
        if len(spell_available) == 0:
            rp("You Have No Available Spells", 1)
            rp("Going Back", 1, True)
            menu_class(previous_location_function)
        else:
            rp(f"You Can Change To: {spell_available}", 1)
            rp("To Change Spell Type It As Seen Above")
            change_skill = str(input())
            print()
            t.sleep(1)
            if change_skill in spell_available:
                spell_available.append(class_)
                spell = change_skill
                spell_available.pop(change_skill)
                rp(f"You Are Now Use {spell}", 1)
                rp("Going Back", 1, True)
                menu_class(previous_location_function)
            else:
                rp("That Wasn't An Option", 1)
                rp("Going Back", 1, True)
            menu_class(previous_location_function)
    if class_ == "fighter":
        if len(weapon_available) == 0:
            rp("You Have No Available Weapons", 1)
            rp("Going Back", 1, True)
            menu_class(previous_location_function)
        else:
            rp(f"You Can Change To: {weapon_available}", 1)
            rp("To Change Weapon Type It As Seen Above")
            change_skill = str(input())
            change_skill = change_skill.upper()
            print()
            t.sleep(1)
            if change_skill in weapon_available:
                weapon_available.append(class_)
                weapon = change_skill
                weapon_available.pop(change_skill)
                rp(f"You Are Now Use {weapon}", 1)
                rp("Going Back", 1, True)
                menu_class(previous_location_function)
            else:
                rp("That Wasn't An Option", 1)
                rp("Going Back", 1, True)
            menu_class(previous_location_function)
    if class_ == "archer":
        if len(arrow_available) == 0:
            rp("You Have No Available Arrows", 1)
            rp("Going Back", 1, True)
            menu_class(previous_location_function)
        else:
            rp(f"You Can Change To: {arrow_available}", 1)
            rp("To Change Arrow Type It As Seen Above", 1)
            change_skill = str(input())
            print()
            t.sleep(1)
            if change_skill in arrow_available:
                arrow_available.append(class_)
                arrow = change_skill
                arrow_available.pop(change_skill)
                rp(f"You Are Now Use {arrow}", 1)
                rp("Going Back", 1, True)
                menu_class(previous_location_function)
            else:
                rp("That Wasn't An Option", 1)
                rp("Going Back", 1, True)
            menu_class(previous_location_function)
    if class_ == "brawler":
        if len(weapon_available) == 0:
            rp("You Have No Available Moves", 1)
            rp("Going Back", 1, True)
            menu_class(previous_location_function)
        else:
            rp(f"You Can Change To: {skill_available}", 1)
            rp("To Change Weapon Type It As Seen Above", 1)
            change_skill = str(input())
            print()
            t.sleep(1)
            if change_skill in skill_available:
                skill_available.append(class_)
                skill = change_skill
                skill_available.pop(change_skill)
                rp(f"You Are Now Use {skill}", 1)
                rp("Going Back", 1, True)
                menu_class(previous_location_function)
            else:
                rp("That Wasn't An Option", 1)
                rp("Going Back", 1, True)
            menu_class(previous_location_function)

def menu_weather(previous_location):
    global this_weather
    if this_weather == "sunny":
        rp("The Weather Is Sunny", 1)
        rp("Energy Efficenty Is Decreased", 1, True)
    elif this_weather == "clear":
        rp("The Weather Is Clear", 1)
        rp("No Debuffs Applied", 1, True)
    elif this_weather == "cloudy":
        rp("The Weather Is Cloudy", 1)
        rp("No Debuffs Applied", 1, True)
    elif this_weather == "drizzling":       
        rp("The Weather Is Drizzling", 1)
        rp("No Debuffs Applied", 1, True)
    elif this_weather == "raining":
        rp("The Weather Is Raining", 1)
        rp("Energy Efficenty Is Decreased", 1, True)
    elif this_weather == "snowing":
        rp("The Weather Is Snowing", 1)
        rp("You Lose Warmth Over Time", 1)
        rp("If You Run Out Of Warmth You Will Lose Health Over Time", 1, True)
    elif this_weather == "hail_storm":
        rp("There Is A Hail Storm", 1)
        rp("You Take Damage Over Time Unless In Shelter", 1, True)
    elif this_weather == "thundering":
        rp("There Is A Thunder Storm", 1)  
        rp("There Is A Chance You Will Be Struck By Lightning", 1, True)
    elif this_weather == "heatwave":
        rp("There Is A Heatwave", 1)
        rp("You Gain Warmth Over Time", 1, True)
        rp("If You Gain To Much You Will Lose Health Over Time", 1, True)
    menu_home(previous_location)