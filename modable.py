import time as t
import os as o
import random as r
import keyboard as k
import json as j 

start_load = t.time() #records time at start of loading to see how long it takes to load

game_dir = o.path.dirname(o.path.abspath(__file__))
save_name = "save_file.json"      #Retrives Path For Save File
save_dir = f"{game_dir}/{save_name}"

mod_file = f"{game_dir}/mods"
base_file = f"{game_dir}/modules"

if not o.path.exsist(f"{mod_file}/main.py"):
    import main.py from f"{base_file}/main.py"
if not o.path.exsist(f"{mod_file}/weapons.py")
    import weapons.py from f"{game_dir}/modules/wepons.py"
if not o.path.exsist(f"{}")
        


def temp():
    global health
    global energy
    global damage
    global inventory
    global gold
    global armour_base
    global armour_plate
    global armour_lining
    global energy_efficenty
    global damage_resistence
    global event_speed
    global crit_chance
    global crit_attack
    global crit_multiplier
    global armour_affects
    global class_
    global spell
    global weapon
    global arrow
    global skill
    global class_available
    global spell_available
    global weapon_available
    global arrow_available
    global skill_available
    global damage_affects
    global armour_affects
    global armour_base_available
    global armour_plate_available
    global armour_lining_available
    global beach_wander_loot
    global beach_dig_loot
    global beach_fishing_loot
    global beach_discovered
    global field_discovered
    global forest_discovered
    global overhang_discovered
    global last_checkpoint
    global save_dir
    global companion
    global companion_available
    global tutorial_done
    global text_tutorial_chest
    global text_tutorial_back
    global text_tutorial_forward
    global text_tutorial_done
    global fight_tutorial_dodge
    global fight_tutorial_attack
    global fight_tutorial_crit
    global fight_tutorial_done
    global menu_tutorial_save
    global menu_tutorial_basic
    global menu_tutorial_access
    global menu_tutorial_done
    global weather_chance
    global neg2_weather
    global last_weather
    global this_weather
    global next_weather

#shown information
health = 30
energy = 30
damage = 1
inventory = []
gold = 0

#armour system
armour_base = "none"
armour_plate = "none"
armour_lining = "none"

#armour effects
event_speed = 1
energy_efficenty = 1
damage_resistence = 1

#weapon effects
crit_chance = 1
crit_attack = False
crit_multiplier = 2

armour_base_available = []
armour_plate_available = []
armour_lining_available = []

armour_affects = []

#class & weapon system
class_ = "fighter"
spell = "none"
weapon = "none"
arrow = "none"
skill = "none"

class_available = []
spell_available = []
weapon_available = []
arrow_available = []
skill_available = []

damage_affects = []

energy_timer = 0

#pet
companion = "none"
companion_available = []

#discovered areas
game_started = False
beach_discovered = False
field_discovered = False
forest_discovered = False
overhang_discovered = False

last_checkpoint = "none"

#loot tables
beach_fishing_loot = ["fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "plank", "plank", "plank", "plank", "plank", "plank", "plank",  "plank" "plank", "plank", "plank", "plank", "plank", "plank", "plank", "plank",  "plank" "plank", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "fish_scaling"]
beach_dig_loot = ["rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock","rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "plank", "plank", "plank", "plank" "plank", "plank", "plank", "plank" "plank", "plank", "plank", "plank", "plank", "plank", "plank", "plank", "plank", "plank", "plank", "plank", "plank", "plank", "plank", "plank" "plank", "plank", "plank", "plank", "plank", "plank", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "gold", "gold", "gold", "gold_chest", "rock_dweller"]
beach_wander_loot = ["plank", "plank", "plank", "plank" "plank", "plank", "plank", "plank" "plank", "plank", "plank", "plank"  "plank", "plank", "plank", "plank" "plank", "plank", "plank", "plank", "plank", "plank", "plank" "plank", "plank", "plank", "plank" "plank", "plank", "plank", "plank"  "plank", "plank", "plank", "plank" "plank", "plank", "plank", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "gold", "gold", "gold_chest"]

#weather system
weather_chance = ["sunny", "sunny", "sunny", "sunny", "sunny", "sunny", "clear", "clear", "clear", "clear", "clear", "clear", "clear", "clear", "cloudy", "cloudy", "cloudy", "cloudy", "cloudy", "cloudy", "cloudy", "cloudy", "cloudy", "cloudy", "cloudy", "cloudy", "cloudy", "cloudy", "drizzling", "drizzling", "drizzling", "drizzling", "drizzling", "drizzling", "raining", "raining", "raining", "raining", "raining", "raining", "raining", "raining", "snowing", "snowing", "snowing", "snowing", "snowing"]

thunderstrike_chance = 50

last_weather_effect_refesh = 0
last_weather_change_refesh = 0
weather_change_addtitional_time = 0

neg2_weather = "temp"
last_weather = "temp"
this_weather = "temp"
next_weather = "temp"

warmth = 5
in_shelter = False

#tutorial
tutorial_done = False
text_tutorial_chest = False
text_tutorial_back = False
text_tutorial_forward = False
text_tutorial_done = False
fight_tutorial_dodge = False
fight_tutorial_attack  = False
fight_tutorial_crit  = False
fight_tutorial_done = False
menu_tutorial_basic = False
menu_tutorial_save = False
menu_tutorial_access = False
menu_tutorial_done = False

end_load = t.time()
loading_time = end_load - start_load
loading_time = round(loading_time, 4)
print(f"Loaded In {loading_time} Seconds")
print()

print("Type 'START' To Start")
start_game = str(input())
print()
t.sleep(1)
if start_game == "START":
    if game_started == False:
        print("Welcome")
        t.sleep(1)
        save_data()
        t.sleep(1)
        print("Starting Your New Journey")
        t.sleep(1)
        print()
        tutorial()
    else:
        print("Welcome")
        t.sleep(1)
        load_save()
        t.sleep(1)
        print("Returning To Beach")
        t.sleep(1)
        print()
        game_start()
else:
      print("LEARN TO SPELL")