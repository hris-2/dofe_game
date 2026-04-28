import time as t
import os as o
import random as r
try:
    import keyboard as k
except:
    o.system('pip install keyboard')
    import keyboard as k
import json as j

start_load = t.time() #records time at start of loading to see how long it takes to load

game_dir = o.path.dirname(o.path.abspath(__file__))
save_name = "save_file.json"      #Retrives Path For Save File
save_dir = f"{game_dir}/{save_name}"

def save_data():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    '''Retrives Character Data And Updates The Save Data With It
    Is A Silent Task
    Returns To The Specified Location Or Menu

    >>> save_data()
    Would Save Data Silently And Return To The Previous Location
    '''
    if not o.path.exists(save_dir):
        open(save_dir, "w").close()
    data = {
        "health": health,
        "energy": energy,
        "gold": gold,
        "inventory": inventory,
        "damage": damage,
        "armour_base": armour_base,
        "armour_plate": armour_plate,
        "armour_lining": armour_lining,
        "armour_base_available": armour_base_available,
        "armour_plate_available": armour_plate_available,
        "armour_lining_available": armour_lining_available,
        "companion": companion,
        "companian_available": companion_available,
        "class_": class_,
        "weapon": weapon,
        "spell": spell,
        "arrow": arrow,
        "skill": skill,
        "neg2_weather": neg2_weather,
        "last_weather": last_weather,
        "this_weather": this_weather,
        "new_weather": new_weather,
        "last_weather_refresh_time": last_weather_change_refesh,
        "last_weather_effect_time": last_weather_effect_refesh,
        "class_available": class_available,
        "weapon_available": weapon_available,
        "spell_available": spell_available,
        "arrow_available": arrow_available,
        "skill_available": skill_available,
        "game_started": game_started,
        "beach_discovered": beach_discovered,
        "field_discovered": field_discovered,
        "forest_discovered": forest_discovered,
        "overhang_discovered": overhang_discovered,
        "tutorial_done": tutorial_done
    }
    with open(save_dir, "w") as a:
        j.dump(data, a)
    return

def load_save():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    '''Retrives Data From The Save Data And Updates The Character Information
    Is A Silent Task
    Returns To The Previous Location
   
    >>> load_save()
    Would Update Character Data From Save File And Return To Previous Location
    '''
    with open(save_dir, "r") as f:
        data = j.load(f)
    health = data.get("health", 30)
    energy = data.get("energy", 30)
    gold = data.get("gold", 0)
    inventory = data.get("inventory", [])
    armour_base = data.get("armour_base", "none")
    armour_plate = data.get("armour_plate", "none")
    armour_lining = data.get("armour_lining", "none")
    armour_base_available = data.get("armour_base_available", [])
    armour_plate_available = data.get("armour_plate_available", [])
    armour_lining_available = data.get("armour_lining_available", [])
    companion = data.get("companion", "none")
    companion_available = data.get("companion_available", [])
    class_ = data.get("class_", "fighter")
    weapon = data.get("weapon", "none")
    spell = data.get("spell", "none")
    arrow = data.get("arrow", "none")
    skill = data.get("skill", "none")
    class_available = data.get("class_available", [])
    weapon_available = data.get("weapon_available", [])
    spell_available = data.get("spell_available", [])
    arrow_available = data.get("arrow_available", [])
    skill_available = data.get("skill_available", [])
    neg2_weather = data.get("neg2_weather", "none")
    last_weather = data.get("last_weather", "none")
    this_weather = data.get("this_weather", "none")
    next_weather = data.get("next_weather", "none")
    last_weather_change_refesh = data.get("last_weather_change_refresh", 1)
    last_weather_effect_refesh = data.get("last_weather_effect_refresh", 1)
    game_started = data.get("game_started", False)
    beach_discovered = data.get("beach_discovered", False)
    field_discovered = data.get("field_discovered", False)
    forest_discovered = data.get("forest_discovered", False)
    overhang_discovered = data.get("overhang_discovered", False)
    tutorial_done = data.get("tutorial_done", False)
    return 

def quick_time_event(time_allowed, prompt_key, keyword):
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    '''Creats A Basic Quick Time Event
    Sets A Timer With The Time Given Multiplied By The Event Speed Stat.
    Sets The Given Key To Be The Trigger Key.
    If Trigger Key Is Set To 'random' A Random Letter Is Chosen
    Prints A Basic Sentence With The Time Allowed, Prompt Key & Keyword Given
    During The Time Allowed It Constsantly Checks If The Selected Key Has Been Pressed
    Incorrectly Pressed Keys Do Not Effect The Event.
    Once Correct Key Is Pressed True Is Returned.
    If The Timer Runs Out Without The Key Being Pressed False Is Returned.

    >>> quick_time_event(20, "b", "Test The Feature")
    You Have 20 Seconds to Press 'b' To Test The Feature

    If The Key Is Pressed In Time True Is Returned
    Otherwise False Is Return
    '''
    time_allowed = time_allowed * event_speed
    if prompt_key == "random":
        prompt_key = r.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
    print(f"You Have {time_allowed} Seconds to Press '{prompt_key}' To {keyword}")
    t.sleep(0.5)
    start = t.time()
    while t.time() - start <= time_allowed:
        if k.is_pressed(prompt_key):
            return True
    return False

def quick_time_double(time_allowed, prompt_key_1, prompt_key_2, keyword):
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    '''Creats A Basic Quick Time Event Where 2 Keys Must Be Pressed At Once
    Sets A Timer With The Time Given Multiplied By The Event Speed Stat.
    Sets The Two Given Key To Be The Trigger Keys.
    If One Of The Trigger Key Is Set To 'random' A Random Letter Is Chosen For That Trigger.
    Prints A Basic Sentence With The Time Allowed, Prompt Keys & Keyword Given
    During The Time Allowed It Constsantly Checks If Both Of The Selected Key Has Been Pressed
    Incorrectly Pressed Keys Do Not Effect The Event.
    Once Both Correct Keys Are Pressed At The Same Time Is Pressed True Is Returned.
    If The Timer Runs Out Without The Keys Being Pressed False Is Returned.

    >>> quick_time_event(20, "a", "b", "Test The Feature")
    You Have 20 Seconds to Press 'a' And 'b' To Test The Feature

    If Both The Keys Are Pressed In Time True Is Returned
    Otherwise False Is Return
    '''
    time_allowed = time_allowed * event_speed
    if prompt_key_1 == "random":
        prompt_key_1 = r.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
    if prompt_key_2 == "random":
        prompt_key_2 = r.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
    print(f"You Have {time_allowed} Seconds To Press '{prompt_key_1}' And '{prompt_key_2}' To {keyword}")
    t.sleep(0.5)
    start = t.time()
    while t.time() - start <= time_allowed:
        if k.is_pressed(prompt_key_1) and k.is_pressed(prompt_key_2):
            return True
    return False

def quick_time_choice(time_allowed, prompt_key_1, prompt_key_2, keyword_1, keyword_2):
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    '''Creates A Basic Quick Time Event Where Multiple Options Are Available Through Different Keys
    Sets A Timer With The Time Given Multiplied By The Event Speed Stat.
    Sets The Two Given Key To Be The Trigger Keys.
    If One Of The Trigger Key Is Set To 'random' A Random Letter Is Chosen For That Trigger.
    Prints A Basic Sentence With The Time Allowed, Prompt Keys & Keywords Given
    During The Time Allowed It Constsantly Checks If Both Of The Selected Key Has Been Pressed
    Incorrectly Pressed Keys Do Not Effect The Event.
    Once A Correct Key Is Pressed It Returns Either 'Option 1' or 'Option 2' Based On the Key Pressed
    If The Timer Runs Out Without Any Key Being Pressed False Is Returned.

    >>> quick_time_event(20, "a", "b", "Test The Feature", "Make Sure This Works")
    You Have 20 Seconds to Press 'a' To Test The Feature Or Press "b" To Make Sure This Works

    If "a" Is Pressed 'Option 1' Is Returned
    Else Is 'b' Is Pressed 'Option 2' Is Returned
    Otherwise False Is Returned
    '''
    time_allowed = time_allowed * event_speed
    if prompt_key_1 == "random":
        prompt_key_1 = r.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
    if prompt_key_2 == "random":
        prompt_key_2 = r.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
    print(f"You Have {time_allowed} Seconds To Press '{prompt_key_1}' To {keyword_1} Or Press '{prompt_key_2}' To {keyword_2}")
    t.sleep(0.5)
    start = t.time()
    while t.time() - start <= time_allowed:
        if k.is_pressed(prompt_key_1):
            return "Option 1"
        elif k.is_pressed(prompt_key_2):
            return "Option 2"
    return False

def quick_time_spam(time_allowed, prompt_key, press_key_number, keyword):
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    '''Creats A Basic Quick Time Event Where A Key Must Be Pressed Multiple Times
    Sets A Timer With The Time Given Multiplied By The Event Speed Stat.
    Sets The Given Key To Be The Trigger Key.
    If Trigger Key Is Set To 'random' A Random Letter Is Chosen
    Sets The Amount The Key Needs To Be Pressed As Given.
    If press_key_number Is Set To 'random' A Random Number From 20 To 30
    Or If press_key_number Is Set To 'random/2' A Random Number From 10 To 20
    Prints A Basic Sentence With The Time Allowed, Prompt Key, Key Pressed Amount Required & Keyword Given
    During The Time Allowed It Constsantly Checks If The Selected Key Has Been Pressed
    Incorrectly Pressed Keys Do Not Effect The Event.
    Once Correct Key Is Pressed True Is Returned.
    If The Timer Runs Out Without The Key Being Pressed False Is Returned.

    >>> quick_time_event(20, "b", 17, "Test The Feature")
    You Have 20 Seconds to Press 'b' 17 Times To Test The Feature

    If The Key Is Pressed Enough Times Within The TIme Given True Is Returned
    Otherwise False Is Return
    '''
    time_allowed = time_allowed * event_speed
    if prompt_key == "random":
        prompt_key = r.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
    if press_key_number == "random":
        press_key_number = r.choice([20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 30])
    if press_key_number == "random/2":
        press_key_number = r.choice([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 20])
    print(f"You Have {time_allowed} Seconds To Press '{prompt_key}' {press_key_number} Times To {keyword}")
    key_pressed = 0
    holding = False
    t.sleep(0.5)
    start = t.time()
    while t.time() - start <= time_allowed:
        if k.is_pressed(prompt_key):
            if not holding:
                key_pressed += 1
                holding = True
        else:
            holding = False
    if key_pressed >= press_key_number:
        print(f"You Hit '{prompt_key}' {key_pressed} Times")
        print()
        t.sleep(1)
        return True
    else:
        print(f"You Hit '{prompt_key}' {key_pressed} Times")
        print()
        t.sleep(1)
        return False

def countspam(time_allowed, prompt_key, keyword):
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    '''Similar To quick_time_spam()
    Except For Baseline For Amount Of Times To Spam Key
    And Returns Amount Of Times Key Was Pressed'''
    time_allowed *= event_speed
    if prompt_key == "random":
        prompt_key = r.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "o", "m", "n", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y" "z"])
    print(f"You Have {time_allowed} Seconds To Spam {prompt_key} To {keyword}")
    t.sleep(0.5)
    key_pressed = 0
    holding = False
    start_time = t.time()
    while t.time() - start_time <= time_allowed:
        if k.is_pressed(prompt_key):
            if not holding:
                key_pressed += 1
                holding = True
        else:
            holding = False
    print(f"You Hit '{prompt_key}' {key_pressed} Times")
    print()
    t.time(1)
    return key_pressed

def waitandhit(time_allowed, prompt_key, keyword):
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    '''Creats A Basic Quick Time Event Where A Key Must Be Pressed After A Random Amount Of Time
    Sets A Timer With A Random Amount Of Time Between 5 And 15 Seconds
    Sets The Given Key To Be The Trigger Key.
    If Trigger Key Is Set To 'random' A Random Letter Is Chosen
    Prints A Basic Sentence With The Time Allowed, Prompt Key & Keyword Given
    During The Short Amount Of Time It Checks If THe Key Has Been Pressed
    Incorrectly Pressed Keys Do Not Effect The Event.
    Once Correct Key Is Pressed True Is Returned.
    If The Timer Runs Out Without The Key Being Pressed False Is Returned.

    >>> waitandhit("random", "b", "Test The Feature")
    Waits A Random Amount Of Time Then Prints "Press 'b' To Test The Feature"

    If The Key Is Pressed In Time True Is Returned
    Otherwise False Is Return
    '''
    if time_allowed == "random":
        time_allowed = r.choice([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    if prompt_key == "random":
        prompt_key = r.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
    print(f"Wait For It...")
    t.sleep(time_allowed)
    print(f"Press '{prompt_key}' To {keyword}")
    start = t.time()
    while t.time() - start <= 3:
        if k.is_pressed(prompt_key):
            return True
    return False

def fight_signal():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global splash_range, splash_damage, piercing
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    '''Prints A Statement To Signal A Fight
    Takes Class and Weapon And Changes It Accordingly'''
    if class_ == "fighter" and not weapon == "none":
        rp("You Raise You Weapon A Fight", 1)
    elif ( class_ == "fighter" and weapon == "none" ) or class_ == "brawler":
        rp("You Clench You Fists For A Fight", 1)
    elif class_ == "wizard":
        rp("You Start Chanting Battle Preperation Spells", 1)
    elif class_ == "archer":
        rp("You Load An Arrow Into Your Bow", 1)
    else:
        rp("You Prepare For A Fight", 1)
    print()

def weather_change():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global splash_range, splash_damage, piercing
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    '''Takes Current Weather And Changes Weather Based On It
    Weather Can Change, Advance, Devance Or Stay The Same
    Some Weathers Can Advance Into Extereme Weathers'''
    heatwave_activate = False
    thunder_activate = False
    hail_activate = False
    last_weather_effect_done = 0
    if this_weather == "sunny" and last_weather == "sunny" and neg2_weather == "sunny":
        heatwave_activate = r.choices(
            [True, False],
            weights = [200, 100],
            k = 1
        )
    elif this_weather == "sunny" and last_weather == "sunny":
        heatwave_activate = r.choices(
            [True, False],
            weights = [100, 100],
            k = 1
        )
    elif this_weather == "sunny":
        heatwave_activate = r.choices(
            [True, False],
            weights = [50, 100],
            k = 1
        )
    else:
        heatwave_activate = False
    if this_weather == "raining" and last_weather == "raining" and neg2_weather == "raining":
        thunder_activate = r.choices(
            [True, False],
            weights = [200, 100],
            k = 1
        )
    elif this_weather == "raining" and last_weather == "raining":
        thunder_activate = r.choices(
            [True, False],
            weights = [100, 100],
            k = 1
        )
    elif this_weather == "raining":
        thunder_activate = r.choices(
            [True, False],
            weights = [50, 100],
            k = 1
        )
    else:
        thunder_activate = False
    if this_weather == "snowing" and last_weather == "snowing" and neg2_weather == "snowing":
        thunder_activate = r.choices(
            [True, False],
            weights = [200, 100],
            k = 1
        )
    elif this_weather == "snowing" and last_weather == "snowing":
        thunder_activate = r.choices(
            [True, False],
            weights = [100, 100],
            k = 1
        )
    elif this_weather == "snowing":
        hail_activate = r.choices(
            [True, False],
            weights = [50, 100],
            k = 1
        )
    else:
        hail_activate = False
    if this_weather == "heatwave" or this_weather == "hail_storm" or this_weather == "thundering":
        new_weather_decide = r.choices(
            ["new", "same", "calm"],
            weights = [5, 80, 15]
        )
    else:    
        new_weather_decide = r.choices(
            ["new", "same", "increase", "decrease"],
            weights = [15, 15, 35, 35]
        )
    new_weather = "cloudy"
    if new_weather_decide == "new":
        new_weather = r.choice(weather_chance)
    elif new_weather_decide == "same":
        new_weather = this_weather
    elif new_weather_decide == "increase":
        if this_weather == "sunny":
            new_weather = "sunny"
        elif this_weather == "clear":
            new_weather = "sunny"
        elif this_weather == "cloudy":
            new_weather = "clear"
        elif this_weather == "drizzling":
            new_weather = "cloudy"
        elif this_weather == "raining":
            new_weather = "drizzling"
        elif this_weather == "snowing":
            new_weather = "raining"
    elif new_weather_decide == "decrease":
        if this_weather == "sunny":
            new_weather = "clear"
        elif this_weather == "clear":
            new_weather = "cloudy"
        elif this_weather == "cloudy":
            new_weather = "drizzling"
        elif this_weather == "drizzling":
            new_weather = "raining"
        elif this_weather == "raining":
            new_weather = "snowing"
        elif this_weather == "snowing":
            new_weather = "snowing"
    elif new_weather_decide == "calm":
        if this_weather == "thundering":
            new_weather = "raining"
        elif this_weather == "hail_storm":
            new_weather = "snowing"
        elif this_weather == "heatwave":
            new_weather = "sunny"
    neg2_weather = last_weather
    last_weather = this_weather
    if heatwave_activate == True:
        new_weather = "heatwave"
    elif thunder_activate == True:
        new_weather = "thundering"
    elif hail_activate == True:
        new_weather = "hail_storm"
    this_weather = new_weather

def rest():
    print("Regaining Energy")
    while energy > 30:
        start_time = t.time()
        while t.time() - start_time > 300:
            time_elasped = start_time
            time_left = 300 - time_elasped
            print(f"{time_elasped} Seconds Untill Next Energy")
            t.sleep(30)
        else:
            print("1 Energy Regained")
        t.sleep(1)
        energy += 1
        print(f"You Have {energy} Energy")
        escape_time = t.time()
        print("Press 'e' To Leave")
        while t.time() - escape_time < 10:
            if k.is_pressed("e"):
                return
    else:
        print("You Are Now At Max Energy")
        t.sleep(1)
        return

def refresh_class():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global splash_range, splash_damage, piercing
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    '''Checks For Current Value Of 'class_'
    Then Checks For Current Value Of 'weapon', 'spell', 'arrow', Or 'skill'
    Adjusts Stats Accordingly
    '''
    damage_affects.clear()
    piercing = 1
    splash_damage = 0
    splash_range = 0
    if class_ == "fighter":
        if weapon == "none":
            damage = 1
            crit_chance = 25
        elif weapon == "sword":
            damage = 3
            crit_chance = 30
        elif weapon == "spear":
            damage = 1
            crit_chance = 25
            piercing = 4
        elif weapon == "mace":
            damage = 2
            crit_chance = 75
            piercing = 2
        elif weapon == "dagger":
            damage = 2
            crit_chance = 150
        elif weapon == "nunchuncks":
            damage = 1
            crit_chance = 500
    elif class_ == "wizard":
        if spell == "fireball":
            damage = 2
            crit_chance = 0
            splash_damage = 1
            splash_range = 3
            damage_affects.append("burning")
        elif spell == "iceball":
            damage = 2
            crit_chance = 0
            splash_damage = 1
            splash_range = 3
            damage_affects.append("freezing")
        elif spell == "bludgeon":
            damage = 3
            crit_chance = 0
            splash_damage = 3
            splash_range = 6
        elif spell == "electric":
            damage = 2
            crit_chance = 0
            splash_damage = 1
            splash_range = 7
            damage_affects.append("shocking")
        elif spell == "poison":
            damage = 1
            crit_chance = 0
            splash_damage = 1
            splash_range = 5
            damage_affects.append("poisoning")
        elif spell == "time_freeze":
            damage = 1
            crit_chance = 0
            splash_damage = 1
            splash_range = 5
            damage_affects.append("time_freezing")
    elif class_ == "archer":
        if arrow == "none":
            damage = 1
            crit_chance = 100
            piercing = 3
        elif arrow == "posion":
            damage = 1
            crit_chance = 100
            piercing = 3
            damage_affects.append("posioning")
        elif arrow == "flame":
            damage = 1
            crit_chance = 100
            piercing = 3
            damage_affects.append("burning")
        elif arrow == "frozen":
            damage = 1
            crit_chance = 100
            piercing = 3
            damage_affects.append("freezing")
        elif arrow == "conductive":
            damage = 1
            crit_chance = 100
            piercing = 3
            damage_affects.append("shocking")
        elif arrow == "drill":
            damage = 1
            crit_chance = 125
            piercing = 7
    elif class_ == "brawler":
        if skill == "none":
            damage = 1
            crit_chance = 50
        elif skill == "sweep_kick":
            damage = 2
            crit_chance = 0
            piercing = 5
        elif skill == "1inch_punch":
            damage = 10
            crit_chance = 5
        elif skill == "fly_kick":
            damage = 3
            crit_chance = 0
            piercing = 2
        elif skill == "flurry_punch":
            damage = 3
            crit_chance = 60

def refresh_armour_base():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global splash_range, splash_damage, piercing
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    '''Checks For Current Value Of 'armour_base'
    Adjusts Stats Accordingly
    '''
    armour_affects.clear()
    if armour_base == "none":
        damage_resistence = 1
        event_speed = 1
    elif armour_base == "fish_scaling":
        damage_resistence = 1.5
        armour_affects.append("skip_swim")
        event_speed = 1
    elif armour_base == "dragon_scaling":
        damage_resistence = 2
        armour_affects.append("heat_immune")
        event_speed = 1
    elif armour_base == "leather":
        damage_resistence = 1.5
        event_speed = 2
    elif armour_base == "boiled_leather":
        damage_resistence = 2.5
        event_speed = 2
    elif armour_base == "chainmail":
        damage_resistence = 3
        event_speed = 0.75
    elif armour_base == "gold_chainmail":
        damage_resistence = 3
        armour_affects.append("shining_glamour")
        event_speed = 0.75
    elif armour_base == "fabric_clothing":
        damage_resistence = 0.5
        event_speed = 3

def refresh_armour_plating():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global splash_range, splash_damage, piercing
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    '''Checks For Current Value of 'armour_plate'
    Adjusts Stat Values Accordingly
    '''
    if armour_plate == "none":
        energy_efficenty = 1
        damage_resistence += 0
    elif armour_plate == "ice":
        armour_affects.append("freezing_aura")
        energy_efficenty = 1.5
        damage_resistence += 1
    elif armour_plate == "coal":
        energy_efficenty = 1.5
        damage_resistence += 1
    elif armour_plate == "burning_coal":
        energy_efficenty = 1.5
        damage_resistence += 1
        armour_affects.append("burning_aura")
    elif armour_plate == "steel":
        energy_efficenty = 2
        damage_resistence = 4
    elif armour_plate == "copper":
        energy_efficenty = 2
        damage_resistence = 2
        armour_affects.append("shocking_aura")
    elif armour_plate == "wood":
        energy_efficenty = 1
        damage_resistence = 1.25
    elif armour_plate == "gold":
        energy_efficenty = 2
        damage_resistence = 4
        if "shining_glamour" in armour_affects:
            armour_affects.remove("shining_glamour")
            armour_affects.append("shining_strength")
        else:
            armour_affects.append("shining_glamour")

def refresh_armour_lining():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global splash_range, splash_damage, piercing
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    '''Checks For Current Value of 'armour_lining'
    Adjusts Stats Accordingly
    '''
    if armour_lining == "none":
        ...
    elif armour_lining == "ice_thread":
        if "freezing_aura" in armour_affects:
            armour_affects.remove("freezing_aura")
            armour_affects.append("freezing_gaze")
        else:
            armour_affects.append("freezing_aura")
    elif armour_lining == "fire_thread":
        if "burning_aura" in armour_affects:
             armour_affects.remove("burning_aura")
             armour_affects.append("burning_roar")
        else:
            armour_affects.append("burning_aura")
    elif armour_lining == "conductive_thread":
        if "shocking_aura" in armour_affects:
            armour_affects.remove("shocking_aura")
            armour_affects.append("shocking_step")
        else:
            armour_affects.append("shocking_aura")
    elif armour_lining == "random_thread":
        armour_affects.append("random_effect")
    elif armour_lining == "auto_dodge":
        armour_affects.append("auto_dodge")
    elif armour_lining == "critical_hit":
        crit_multiplier = 4
        crit_chance += 50
    elif armour_lining == "death_strand":
        damage *= 3
       
def refresh_companion():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global splash_range, splash_damage, piercing
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    '''Checks For Current Value Of 'companion'
    Adjusts Stats Accordingly
    '''
    if companion == "parrot":
        damage *= 2
    elif companion == "rock_dweller":
        damage_resistence += 2
    elif companion == "wolf":
        damage += 2
        damage_resistence += 0.5

def weather_effect_refresh():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global splash_range, splash_damage, piercing
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    '''Checks For Current Weather And Applies Effects Based On It
    Effects Are Applied Every 3 Minutes
    Some Effects Are Repeating While Others Are Constant Until Weather Changes
    Effects Can Change Health, Warmth, Energy Efficenty And More
    '''
    if last_weather_effect_refesh + 180 < t.time(): #Repeating Effects Like Hails
        if this_weather == "thundering":
            thunderstrike_happening_determine = r.choices(
                [True, False],
                weights = [ thunderstrike_chance, 100 ],
            )
            if thunderstrike_happening_determine == True:
                if "auto_dodge" in armour_affects:
                    print("A Thunderbolt Stuck Near You")
                    t.sleep(1)
                    print("That Was Close")
                else:
                    thunderstike_dodge = quick_time_event(5, "random" "Roll From The Thunderbolt")
                    t.sleep(1)
                    if thunderstike_dodge == True:
                        print("That Was Close")
                    else:
                        thunder_lost_health = int( 20 / damage_resistence)
                        health -= thunder_lost_health
                        print("The Thunderbolt Zapped You")
                        t.sleep(1)
                        print(f"You Lost {thunder_lost_health} Health. You Now Have {health}")
            else:
                print("The Thunder Cloud Above You Rumbles Intensely")
            t.sleep(1)
            print()
        elif this_weather == "heatwave":
            if warmth >= 10:
                heatwave_damage_lost = int( 3 / damage_resistence )
                health -= heatwave_damage_lost
                print("The Heat Is Beating Down On You")
                t.sleep(1)
                print(f"You Lost {heatwave_damage_lost} Health. You Are Now On {health}")
            else:
                print("The Sun Is Vicicously Throwing Down Its Heat")
                warmth += 1
                print(f"You Have Gained 1 Warmth. You Are Now On {health} Health")
            t.sleep(1)
            print()
        elif this_weather == "hail_storm":
            if in_shelter == False:
                hail_lost_health = int( 3 / damage_resistence )
                health -= hail_lost_health
                print("The Rough Hails Fall And Hit Your Body")
                t.sleep(1)
                print(f"You Have Lost {hail_lost_health} Health. You Now Have {health} Health")
            else:
                print("The Hails Outside Rattle Against The Roof")
            t.sleep(1)
            print()
        elif this_weather == "snowing":
            if warmth <= 0:
                snow_health_lost = int( 3 / damage_resistence )
                health -= snow_health_lost
                print("The Snow Is Numbing Out Your Entire Body")
                t.sleep(1)
                print(f"You Have Lost {snow_health_lost} Health. You Are Now On {health} Health")
            else:
                print("The Thick White Snow Is Slowing Freezing You")
                warmth -= 1
        elif this_weather == "sunny":
            print("The Clear Sky Gives Way To The Hot Sun")
            if weather_effect_done == False:
                energy_efficenty = int( energy_efficenty / 1.25 )
                weather_effect_done = True
            t.sleep(1)
            print()
        elif this_weather == "clear":
            print("The Cloudless Sky Is Complimented By The Calm Sun")
            t.sleep(1)
            print()
        elif this_weather == "drizzling":
            print("Light Rain Drizzles Over The Island")
            t.sleep(1)
            print()
        elif this_weather == "raining":
            print("The Heavy Rain Drop Cover The Island")
            if weather_effect_done == False:
                energy_efficenty = int( energy_efficenty / 1.25 )
                weather_effect_done = True
            t.sleep(1)
            print()

def refresh_all(ignore_death: bool = False, return_norm: bool = False):
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global splash_range, splash_damage, piercing
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    '''Refreshes All Stats And Values That Need Refreshing
    Health And Energy Are Capped At 30
    If Health Is 0 Or Below The Player Dies And Is Returned To Last Checkpoint
    Weather Change Is Checked And Changed If Needed
    All Refresh Functions Are Called
    Data Is Saved At The End
    '''
    if health > 30:
        health = 30
    if energy > 30:
        energy = 30
    if energy < 0:
        energy = 0
    if ignore_death == False:
        if health <= 0:
            t.sleep(1)
            print()
            print("You Died")
            t.sleep(1)
            print("Health Reset To 30")
            t.sleep(1)
            health = 30
            print("Energy Reset To 30")
            t.sleep(1)
            energy = 30
            print("Armour Base, Plating And Lining Reset To None")
            armour_base = "none"
            armour_plate = "none"
            armour_lining = "none"
            t.sleep(1)
            print("Returning To Last Checkpoint")
            t.sleep(1)
            print()
            if return_norm == False:
                last_checkpoint()
            else: 
                return
    if energy <= 0:
        if energy_timer + 60 < t.time():
            energy += 1
            print("You Regained 1 Energy")
            t.sleep(1)
            print(f"You Now Have {energy} Energy")
            t.sleep(1)
            print()
            energy_timer = t.time()
        t.sleep(1)
        print()
        print("You Have No Energy Left")
        t.sleep(1)
        print("Eat Food Or Lose Health")
        health -= 2
        print(f"You Lost 2 Health. YOu Now Have {health} Health")
        t.sleep(1)
        print()
    if last_weather_change_refesh + weather_change_addtitional_time < t.time():
        weather_change()
        weather_change_addtitional_time = r.choice([300, 360, 420, 480, 540, 600])
    refresh_class()
    refresh_armour_base()
    refresh_armour_lining()
    refresh_armour_plating()
    refresh_companion()
    weather_effect_refresh()
    save_data()

def rp(to_print_: str, wait: int = 0, nl: bool = False, ignore_death: bool = False,) -> None:
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global splash_range, splash_damage, piercing
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    ''' rp = Refresh Print
    Refreshs Everything While Printing
    Optional Wait And Newline Featute
    '''
    refresh_all(ignore_death)
    print(to_print_)
    if wait != 0:
        t.sleep(wait)
    if nl is True:
        print()
        
def ci(prompt: str = "", this_location = "", option_1: str = "", option_2: str = "", option_3: str = "", option_4: str = "", option_5: str = "", option_6: str = "") -> str:
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    ''' ci = Common Input
    Simplified Input Function That Can Be Used For Most Inputs
    Supports Up To 6 Options 
    '''
    print(prompt)
    ci_choice = str(input())
    print()
    t.sleep(1)
    ci_choice = ci_choice.upper()
    if ci_choice == option_1 and option_1 != "":
        return "option_1"
    elif ci_choice == option_2 and option_2 != "":
        return "option_2"
    elif ci_choice == option_3 and option_3 != "": 
        return "option_3"
    elif ci_choice == option_4 and option_4 != "":
        return "option_4"
    elif ci_choice == option_5 and option_5 != "":
        return "option_5"
    elif ci_choice == option_6 and option_6 != "":
        return "option_6"
    elif ci_choice == "MENU":
        menu_home(this_location)
    else:
        return "back"
        
def cfl(list_to_choose_from: list = ["empty"], prompt: str = "", this_location = "") -> str:
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    ''' cfl = Choose From List
    Simplified Input Function That Can Be Used For Choosing From A List
    Takes A List And Prints It With A Prompt
    User Must Type The Option How It Is Shown In The List To Select It
    '''
    cfl_choice = "SOMETHING RANDOMLY IMPOSSIBLE FOR TO ACTUALLY BE IN THE GAME"
    while cfl_choice not in list_to_choose_from:
        rp(prompt, 1)
        rp("You Must Type It As Seen Above", 1)
        cfl_choice = str(input())
        cfl_choice = cfl_choice.lower()
        print()
        t.sleep(1)
        if cfl_choice in list_to_choose_from:
            return cfl_choice
        elif cfl_choice == "menu":
            menu_home(this_location)
        elif cfl_choice == "back":
            return "back"
        else:
            rp("Try Again", 1)

def menu_home(previous_location_function):
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global splash_range, splash_damage, piercing
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    global printed_menu_home
    printed_menu_home = False
    while True:
        if printed_menu_home == False:
            rp("Menu:", 0.5)
            rp("Press 'a' For Basic Information Like Health and Inventory", 0.5)
            rp("Press 'b' For Your Armour Information", 0.5)
            rp("Press 'c' For Your Class, Weapon And Companion", 0.5)
            rp("Press 'd' For Current Weather Effects", 0.5)
            rp("Or Press 'e' To Go Back", 1, True)
            printed_menu_home == True
            if k.is_pressed("a"):
                menu_basic(previous_location_function)
            elif k.is_pressed("b"):
                menu_armour(previous_location_function)
            if k.is_pressed("c"):
                menu_class(previous_location_function)
            elif k.is_pressed("d"):
                menu_weather(previous_location_function)
            elif k.is_pressed("e"):
                return

def menu_basic(previous_location_function):
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global splash_range, splash_damage, piercing
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    global printed_menu_home
    rp("Basic Information:", 0.5)
    rp(f"Health: {health}", 0.5)
    rp(f"Energy: {energy}", 0.5)
    rp(f"Gold: {gold}", 0.5)
    rp(f"Inventory: {inventory}", 0.5, True)
    printed_menu_home = False
    return

def menu_armour(previous_location_function):
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    global printed_menu_home
    printed_menu_home = False
    while True:
        rp("Armour Information:", 0.5)
        rp(f"Armour Base: {armour_base}", 0,5)
        rp(f"Armour Plating: {armour_plate}", 0.5)
        rp(f"Armour Lining: {armour_lining}", 0.5, True)
        rp("Would You Like To Change Your Armour 'BASE', 'PLATING', 'LINING' Or 'BACK'")
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
                armour_base_available.remove(select_armour_base)
                rp(f"{select_armour_base} Has Been Applied", 1, True)
            else:
                rp("Not Vailid", 1)
        elif armour_change == "PLATING":
            rp(f"You Have {armour_plate_available} Armour Platings Available", 1)
            rp("To Select An Armour Please Type It How It Shown Above Else Type 'EXIT'")
            select_armour_plate = str(input())
            print()
            t.sleep(1)
            if select_armour_plate in armour_plate_available:
                armour_plate_available.append(armour_plate)
                armour_plate = select_armour_plate
                armour_plate_available.remove(select_armour_plate)
                rp(f"{select_armour_plate} Has Been Applied", 1, True)
            else:
                rp("Not Vailid", 1)
        elif armour_change == "LINING":
            rp(f"You Have {armour_lining_available} Armour Lining Available", 1)
            rp("To Select An Armour Please Type It How It Shown Above Else Type 'EXIT'")
            select_armour_lining = str(input())
            print()
            t.sleep(1)
            if select_armour_lining in armour_lining_available:
                armour_lining_available.append(armour_lining)
                armour_lining = select_armour_lining
                armour_lining_available.remove(select_armour_lining)
                rp(f"{select_armour_lining} Has Been Applied", 1, True)
            else:
                rp("Not Vailid", 1)
        else:
            return

def menu_class(previous_location_function):
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global splash_range, splash_damage, piercing
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    global printed_menu_home
    printed_menu_home = False
    while True:
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
        else:
            return
   
def menu_class_change(previous_location_function):
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global splash_range, splash_damage, piercing
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    global printed_menu_home
    if len(class_available) == 0:
        rp("You Have No Available Classes To Change Too", 1)
        rp("Going Back", 1, True)
        return
    else:
        rp(f"You Can Change Into: {class_available}", 1)
        rp("To Change Class Type It As Seen Above")
        change_class = str(input())
        print()
        t.sleep(1)
        if change_class in class_available:
            class_available.append(class_)
            class_ = change_class
            class_available.remove(change_class)
            rp(f"You Are Now A {class_}", 1)
            rp("Going Back", 1, True)
            return
        else:
            rp("That Wasn't An Option", 1)
            rp("Going Back", 1, True)
            return
           
def menu_class_weapon_change(previous_location_function):
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    global printed_menu_home
    if class_ == "wizard":
        if len(spell_available) == 0:
            rp("You Have No Available Spells", 1)
            rp("Going Back", 1, True)
            return
        else:
            rp(f"You Can Change To: {spell_available}", 1)
            rp("To Change Spell Type It As Seen Above")
            change_skill = str(input())
            print()
            t.sleep(1)
            if change_skill in spell_available:
                spell_available.append(class_)
                spell = change_skill
                spell_available.remove(change_skill)
                rp(f"You Are Now Use {spell}", 1)
                rp("Going Back", 1, True)
                return
            else:
                rp("That Wasn't An Option", 1)
                rp("Going Back", 1, True)
            return
    if class_ == "fighter":
        if len(weapon_available) == 0:
            rp("You Have No Available Weapons", 1)
            rp("Going Back", 1, True)
            return
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
                weapon_available.remove(change_skill)
                rp(f"You Are Now Use {weapon}", 1)
                rp("Going Back", 1, True)
                return
            else:
                rp("That Wasn't An Option", 1)
                rp("Going Back", 1, True)
            return
    if class_ == "archer":
        if len(arrow_available) == 0:
            rp("You Have No Available Arrows", 1)
            rp("Going Back", 1, True)
            return
        else:
            rp(f"You Can Change To: {arrow_available}", 1)
            rp("To Change Arrow Type It As Seen Above", 1)
            change_skill = str(input())
            print()
            t.sleep(1)
            if change_skill in arrow_available:
                arrow_available.append(class_)
                arrow = change_skill
                arrow_available.remove(change_skill)
                rp(f"You Are Now Use {arrow}", 1)
                rp("Going Back", 1, True)
                return
            else:
                rp("That Wasn't An Option", 1)
                rp("Going Back", 1, True)
            return
    if class_ == "brawler":
        if len(weapon_available) == 0:
            rp("You Have No Available Moves", 1)
            rp("Going Back", 1, True)
            return
        else:
            rp(f"You Can Change To: {skill_available}", 1)
            rp("To Change Weapon Type It As Seen Above", 1)
            change_skill = str(input())
            print()
            t.sleep(1)
            if change_skill in skill_available:
                skill_available.append(class_)
                skill = change_skill
                skill_available.remove(change_skill)
                rp(f"You Are Now Use {skill}", 1)
                rp("Going Back", 1, True)
                return
            else:
                rp("That Wasn't An Option", 1)
                rp("Going Back", 1, True)
            return

def menu_weather(previous_location):
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    global printed_menu_home
    printed_menu_home = False
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
    return
    
def tutorial():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    while True:
        if tutorial_done == True:
            print("Tutorial Done")
            t.sleep(1)
            print("Starting Game")
            print()
            t.sleep(1)
            beach()
        else:
            if menu_tutorial_done == True:
                print("Now You Know How To Use Basic Functions In The Menu")
                t.sleep(1)
                print("I Will Explain Some Other Basic Stuff")
                t.sleep(1)
                print("Armour Is Divied Into Three Sections")
                t.sleep(2)
                print("Base, Plating and Lining. Each Sections Has It's Own Effect")
                t.sleep(2)
                print("All Three Parts Give Special Effects Like Fire Resistence Based On What Part You Have On")
                t.sleep(2)
                print("But They All Have One General Stat That Effect Each. For Example")
                t.sleep(2)
                print("Base Effects The Time Given In Quick Time Events Like Fights")
                t.sleep(2)
                print("Plating Effects Damage Resistence And Energy Effiencey")
                t.sleep(2)
                print("Lining Give Extreme Special Effects Like Frost Aura That Freezes Enemies")
                t.sleep(2)
                print("Also There Are Different Classes That Have Different Abilities")
                t.sleep(2)
                print("For Example At The Start You Are A Fighter. You Collect Weapons And Equip Them")
                t.sleep(2)
                print("There Is Also Wizard Where You Collect Spell Book Pages")
                t.sleep(2)
                print("To Use Them Against Your Enemies Like Frost or Fire Ball")
                t.sleep(2)
                print("You Can Level Up These Classes By Find New Items For Them By Playing Them")
                t.sleep(2)
                print("That Is Mostly All For Classes. Next We Will Look At The Level Layout")
                t.sleep(2)
                print("Levels Branch Out Into 3 More Levels Or Known As Locations.")
                t.sleep(2)
                print("There Will Be 5 Tiers Of These Locations Resulting In 121 Locations To Explore")
                t.sleep(2)
                print("Especially Since Each Location Will Have Activities Of It's Own")
                t.sleep(2)
                print("That's All You Need To Know For Now")
                print()
                tutorial_done = True
                t.sleep(1) 
                beach()
            elif fight_tutorial_done == True:
                print("Now You Know How Fight")
                t.sleep(1)
                print("You Need To Know How To Use The Menu")
                t.sleep(1)
                print("The Menu Can Be Accessed From Any Type Box In The Game")
                t.sleep(1)
                print("Although It Is Not Listed At Most Type Boxes")
                t.sleep(1)
                print("In The Menu You Can Access Some Basic Information")
                t.sleep(1)
                print("Like Health, Energy, Inventory And More")
                t.sleep(1)
                print("It Is A Critical Part Of The Game")
                t.sleep(1)
                print("Have A Go Now")
                t.sleep(1)
                print("To Move On You Need To:")
                t.sleep(1)
                print("- Access The Menu From A Type Box")
                t.sleep(0.5)
                print("- View Your Basic Information")
                t.sleep(0.5)
                print("- Save Your Data From The Menu")
                t.sleep(0.5)
                print("Once All Those Are Done You Will Be Brought Back Here")
                t.sleep(1)
                print()
                menu_tuorial_part_1()
            elif text_tutorial_done == True:
                print("Now You Know How To Navigate The Game")
                t.sleep(1)
                print("You Need To Know How To Fight")
                t.sleep(1)
                print("Fights Are Turned Based And It's Random Who Turn It Is")
                t.sleep(1)
                print("The Fights Are Quick Time Based. A Random Key Will Be Selected For You To Press")
                t.sleep(2)
                print("If You Get To Attack And Successfully Get A Critical Attack Chance")
                t.sleep(2)
                print("You Get To Do A Critical Hit By Pressing 2 Keys At The Same Time")
                t.sleep(2)
                print("Have A Go Now")
                t.sleep(2)
                print("To Move On You Need To:")
                t.sleep(1)
                print("- Succesfully Attack An Enemy")
                t.sleep(0.5)
                print("- Successfully Evade An Enemie's Attack")
                t.sleep(0.5)
                print("- Land A Critical Hit")
                t.sleep(0.5)
                print("Once All Those Are Done You Will Be Brought Back Here")
                t.sleep(1)
                print()
                fight_tutorial()
            else:
                print("If You Want To Skip The Tutorial Type 'YES' Otherwise Type 'NO'")
                tutorial_skip = str(input())
                print()
                t.sleep(1)
                if tutorial_skip == "YES":
                    print("Skipping Tutorial")
                    tutorial_done = True
                    beach()
                print("Welcome To The Tutorial")
                t.sleep(1)
                print("In This Tutorial You Will Learn The Basics Of This Game")
                t.sleep(1)
                print("You Have Already Used The Simple Text Box Used The Most Throughout The Game")
                t.sleep(2)
                print("In There You Type Whatever Is Given And Your Choice To Select It")
                t.sleep(2)
                print("Typing Anything Else Other Than What Is Prompted Acts As Back Or No")
                t.sleep(2)
                print("Sometimes There Are Hidden Prompt That You Aren't Told To Find Hidden Rewards")
                t.sleep(2)
                print("Like 'CHEST' or 'OPEN'")
                t.sleep(1)
                print("Have A Go Now")
                t.sleep(2)
                print("To Move On You Need To:")
                t.sleep(1)
                print("- Move Forwards To A New Location")
                t.sleep(0.5)
                print("- Move Back Using Any Word Other Than 'BACK'")
                t.sleep(0.5)
                print("- Find The Hidden Tresure")
                t.sleep(0.5)
                print("Once All Those Are Done Go Back To The First Room")
                t.sleep(1)
                print()
                tutorial_text_box_white()

def tutorial_text_box_white():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    printed_text_white = False
    while True:
        if text_tutorial_back == True and text_tutorial_forward == True and text_tutorial_chest == True:
            print("Well Done You Completed The First Tutorial Section")
            t.sleep(1)
            text_tutorial_done = True
            print()
            return
        print("You Find Yourself In A White Room")
        t.sleep(1)
        print("You Can Move To The 'GREEN' Room, 'RED' Room Or 'BLUE' Room")
        tutorial_room_move = str(input())
        print()
        t.sleep(1)
        if tutorial_room_move == "GREEN":
            tutorial_text_box_green()
        elif tutorial_room_move == "RED":
            tutorial_text_box_red()
        elif tutorial_room_move == "BLUE":
            tutorial_text_box_blue()
        elif tutorial_room_move == "CHEST":
            print("You Found This Chest")
            t.sleep(1)
            print("Well Done")
            text_tutorial_chest = True
            print()
            t.sleep(1)
        else:
            print("That's Not An Option")
            t.sleep(1)
            print("Try Again")
            print()
            t.sleep(1)

def tutorial_text_box_green():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    while True:
        print("You Find Yourself In A Green Room")
        if text_tutorial_forward == False:
            t.sleep(1)
            print("Well Done")
            t.sleep(1)
            print("You Went To A New Room")
            text_tutorial_forward = True
        t.sleep(1)
        print("You Can Move To The 'PURPLE' Room, 'BROWN' Room Or Go 'BACK'")
        tutorial_room_move = str(input())
        print()
        t.sleep(1)
        if tutorial_room_move == "PURPLE":
            print("This Door Is Locked")
            print()
            t.sleep(1)
        elif tutorial_room_move == "BROWN":
            print("You Enter The Brown Room")
            t.sleep(1)
            print("An Overwhelming Stench Takes Over You As You Run Back To The Green Room")
            t.sleep(2)
            print()
        elif tutorial_room_move == "BACK":
            return
        else:
            print("Well Done")
            t.sleep(1)
            print("You Went Back Without Typing 'BACK'")
            print()
            text_tutorial_back = True
            t.sleep(1)
            return  

def tutorial_text_box_red():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    while True:
        print("You Find Yourself In A Red Room")
        if text_tutorial_forward == False:
            t.sleep(1)
            print("Well Done")
            t.sleep(1)
            print("You Went To A New Room")
            text_tutorial_forward = True
        t.sleep(1)
        print("You Can Move To The 'YELLOW' Room, 'ORANGE' Room Or Go 'BACK'")
        tutorial_room_move = str(input())
        print()
        t.sleep(1)
        if tutorial_room_move == "YELLOW":
            print("As You Open The Door A Heat Greater Than A Millon Suns Hit You")
            t.sleep(1)
            print("You Rush To Close The Door")
            print()
            t.sleep(1)
        elif tutorial_room_move == "ORANGE":
            print("You Enter The Orange Room")
            t.sleep(1)
            print("The Room Is Filled With Oranges")
            t.sleep(1)
            print("Unfortunatly You Are Deadly Allergic To Oranges So You Go Back")
            t.sleep(2)
            print()
        elif tutorial_room_move == "BACK":
            return
        else:
            print("Well Done")
            t.sleep(1)
            print("You Went Back Without Typing 'BACK'")
            print()
            text_tutorial_back = True
            t.sleep(1)
            return  
   
def tutorial_text_box_blue():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    while True:
        print("You Find Yourself In A Blue Room")
        if text_tutorial_forward == False:
            t.sleep(1)
            print("Well Done")
            t.sleep(1)
            print("You Went To A New Room")
            text_tutorial_forward = True
        t.sleep(1)
        print("You Can Move To The 'AQUA' Room, 'LILAC' Room Or Go 'BACK'")
        tutorial_room_move = str(input())
        print()
        t.sleep(1)
        if tutorial_room_move == "AQUA":
            print("As You Open The Door Water Floods In")
            t.sleep(1)
            print("You Rush To Close The Door")
            print()
            t.sleep(1)
        elif tutorial_room_move == "LILAC":
            print("You Enter The Lilac Room")
            t.sleep(1)
            print("The Air Smells Of A Scent Of Flowers")
            t.sleep(1)
            print("The Air Was So Good You Fell Asleep And Found Yourself Back In The Blue Room")
            t.sleep(2)
            print(1)
        elif tutorial_room_move == "BACK":
            return
        else:
            print("Well Done")
            t.sleep(1)
            print("You Went Back Without Typing 'BACK'")
            print()
            text_tutorial_back = True
            t.sleep(1)
            return  

def fight_tutorial():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    while True:
        white_box_health = 5
        print(f"You Are Fighing A Mystical White Box Which Has {white_box_health} Health")
        crit_attack = False
        print()
        t.sleep(1)
        while white_box_health > 0:
            if health <= 0:
                print("Try Again")
                health = 30
            t.sleep(1)
            if fight_tutorial_attack == True and fight_tutorial_dodge == True and fight_tutorial_crit == True:
                print("Well Done")
                t.sleep(1)
                print("You Have Completed The Fight Tutorial")
                fight_tutorial_done = True
                crit_attack = False
                print()
                t.sleep(1)
                return
            action = r.choice(["attack", "dodge"])
            if action == "dodge":
                t.sleep(1)
                print()
                print("The Box Is Attacking")
                if quick_time_event(3, "random", "Dodge the Attack") == True:
                    t.sleep(0.5)
                    print("The Box Misses and Hits The Wall Behind You")
                    if fight_tutorial_dodge == False:
                        print("Well Done You Dodge An Attack")
                        fight_tutorial_dodge = True
                    crit_attack = False
                else:
                    damage_taken = 2 / damage_resistence
                    health -= damage_taken
                    t.sleep(0.5)
                    print(f"The Box Hit You For {damage_taken} Health. You Now Have {health} Health Left")
                    crit_attack = False
            else:
                if crit_attack == True:
                    print()
                    t.sleep(1)
                    print("Your Turn To Attack")
                    print("You Have a Chance for a Critical Hit")
                    if quick_time_double(2, "random", "random", "Critical Hit the Baby Dragon") == True:
                        t.sleep(0.5)
                        white_box_health_taken = 2 * damage
                        white_box_health -= white_box_health_taken
                        print(f"You Attacked the White Box with a Critical Hit For {white_box_health_taken} Damage. It Now Has {white_box_health} Health Left")
                        if fight_tutorial_crit == False:
                            print("Well Done You Hit A Critical Attack")
                            fight_tutorial_crit = True
                            crit_attack = False
                    else:
                        print("You Missed Your Attack")
                        crit_attack = False
                else:  
                    print()
                    t.sleep(1)
                    print("Your Turn To Attack")
                    if quick_time_event(3, "random", "Attack the White Box") == True:
                        t.sleep(0.5)
                        white_box_health_taken = 1 * damage
                        white_box_health -= white_box_health_taken
                        print(f"You Attacked the White Box For {white_box_health_taken} Damage. It Now Has {white_box_health} Health Left")
                        crit_attack = True
                        if fight_tutorial_attack == False: 
                            fight_tutorial_attack = True
                            print("Well Done You Hit A Normal Attack")
                    else:
                        print("You Missed Your Attack")
                        crit_attack = False
        if white_box_health >= 0:
            t.sleep(1)
            print("You Defeated the White Box But Not Complete The Task")
            t.sleep(1)
            print("Restarting")
            crit_attack = False
            print()
            t.sleep(1)

def menu_tuorial_part_1(): 
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    while menu_tutorial_done == False:
        print("Hello. Respond With 'HI', 'GO AWAY' OR 'I HATE YOU'")
        menu_1_option = str(input())
        print()
        t.sleep(1)
        if menu_1_option == "HI":
            print("Thank You.")
            t.sleep(1)
            print("But You Failed The Objective. :(")
            t.sleep(1)
            print("Try Again")
            t.sleep(1)
            print()
        elif menu_1_option == "GO AWAY":
            print("What Have I Done")
            t.sleep(1)
            print("Doesn't Matter Because You Failed The Objective.")
            t.sleep(1)
            print("Try Again")
            t.sleep(1)
            print()
        elif menu_1_option == "I HATE YOU":
            print("Well That Was Very Mean")
            t.sleep(1)
            print("And You Didn't Even Complete The Objective.")
            t.sleep(1)
            print("So You Have Try Again Which You Deserve")
            t.sleep(1)  
            print()
        elif menu_1_option == "MENU":
            menu_tutorial_part_2()
        
def menu_tutorial_part_2():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    while True:
        if menu_tutorial_access == True and menu_tutorial_basic == True and menu_tutorial_save == True:
            print("Well Done You Completed The Menu Tutorial")
            menu_tutorial_done = True
            t.sleep(1)
            print()
            return
        print("Accessing Menu")
        t.sleep(1)
        print("Well Done You Completed The First Objective")
        menu_tutorial_access = True
        t.sleep(1)
        print("You Can View 'BASIC', 'ARMOUR', 'CLASS' Or 'WEATHER' Information")
        t.sleep(1)
        print("Or You Can 'SAVE' Your Data")
        menu_2_option = str(input())
        print()
        t.sleep(1)
        if menu_2_option == "BASIC":
            print("Well Done You Viewed Your Basic Information")
            t.sleep(1)
            menu_tutorial_basic = True
            print("Going Back To Menu")
            t.sleep(1)
            print()
        elif menu_2_option == "ARMOUR" or menu_2_option == "CLASS" or menu_2_option == "WEATHER":
            print(f"Well Done You Viewed Your Some Information On")
            t.sleep(1)
            print("But It Wasn't Nessecary For The Objective")
            t.sleep(1)
            print("Going Back To Menu")
            t.sleep(1)
            print()
        elif menu_2_option == "SAVE":
            print("Well Done You Saved Your Data")
            t.sleep(1)
            print("You Completed An Objective")
            menu_tutorial_save = True
            t.sleep(1)
            print()
        
def beach():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    last_checkpoint = beach
    while True:
        if beach_discovered == False:
            rp("You Wake Up Confused Lying On The Floor", 1)
            rp("Sand Grains Irritate Your Skin And Seep Into Your Clothes", 1)
            rp("Sand, What. You Should Be On A Ship", 1)
            rp("You Stand Up And Realise Your On A Beach", 1)
            rp("You Try To Think Of Why You Are Here", 1)
            rp("But Cannot Remember Anything Else But The Ship", 1)
            rp("With Nothing Else To Do", 1)
            rp("You Start Looking For Resources", 1)
            beach_option_1 = ci("You Can 'DIG' or 'WANDER' To Look For Resourses", beach, "DIG", "WANDER")
            if beach_option_1 == "option_1":
                beach_dig()
            elif beach_option_1 == "option_2":
                beach_wander()
            elif beach_option_1 == "back":
                ending_1()
        else:
            rp("You Are Back On The Beach You Woke Up On", 1)
            if "fishing_rod" in inventory:
                beach_option_2 = ci("You Can 'WANDER', 'DIG', or 'FISH' Or Travel To The 'FOREST', 'FIELD' Or 'OVERHANG' ", beach, "WANDER", "DIG", "FISH", "FOREST", "FIELD", "OVERHANG")
                if beach_option_2 == "option_1":
                    beach_wander()
                elif beach_option_2 == "option_2":
                    beach_dig()
                elif beach_option_2 == "option_3":
                    beach_fish()
                elif beach_option_2 == "option_4":
                    forest()
                elif beach_option_2 == "option_5":
                    field()
                elif beach_option_2 == "option_6":
                    overhang()
                else:
                    rp("Not A Valid Option Try Again", 1, True)
                    beach()
            else:
                beach_option_3 = ci("You Can 'WANDER' Or 'DIG' Or Travel To The 'FOREST', 'FIELD' Or 'OVERHANG' ", beach, "WANDER", "DIG", "FOREST", "FIELD", "OVERHANG")
                if beach_option_3 == "option_1":
                    beach_wander()
                elif beach_option_2 == "option_2":
                    beach_dig()
                elif beach_option_2 == "option_3":
                    forest()
                elif beach_option_2 == "option_4":
                    field()
                elif beach_option_2 == "option_5":
                    overhang()
                else:
                    rp("Not A Valid Option Try Again", 1, True)

def beach_wander():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    while True:
        if beach_discovered == False:
            rp("You Start Strolling Down The Beach", 1)
            fishing_rod_time = r.choice([6, 7, 8, 9, 10])
            rp("Looking For Resources That Down With The Boat", fishing_rod_time)
            rp(f"After {fishing_rod_time} Seconds You Find A Fishing Rod", 1)
            inventory.append("fishing_rod")
            energy_lost_beach_wander_fish_rod = 1 * energy_efficenty
            energy -= energy_lost_beach_wander_fish_rod
            rp("This Will Be Handy", 1)
            rp("Fishing Rod Added To Inventory", 1)
            rp(f"You Lost {energy_lost_beach_wander_fish_rod} Energy. You Are Now On {energy}", 1)
            beach_discovered = True
            game_started = True
            beach_wander_option_1 = ci("Do You Want To Keep Wandering? 'YES'/'NO'", beach_wander, "YES", "NO")
            if beach_wander_option_1 != "option_1":
                return
        else:
            wander_pause_time = r.choice([6, 7, 8, 9, 10, 11])
            rp("You Start Strolling Down The Coast Line", wander_pause_time)
            loot = r.choice(beach_wander_loot)
            if loot == "plank":
                loot_name = "Plank"
            elif loot == "rock":
                loot_name = "Rock"
            elif loot == "rubbish":
                loot_name = "Piece Of Rubbish"
            elif loot == "gold":
                loot_name = "Gold Coin"
            elif loot == "gold_chest":
                loot_name = "Gold Chest"
            rp(f"After {wander_pause_time} Seconds You Found A {loot_name}", 1)
            if loot == "plank" or loot == "rock":
                beach_wander_option_2 = ci(f"Do You Want To Keep The {loot_name} 'YES'/'NO'", beach_wander, "YES", "NO")
                if beach_wander_option_2 == "option_1":
                    inventory.append(loot)
                    rp(f"{loot_name} Added To Inventory", 1)
                else:
                    rp(f"You Left The {loot_name}", 1)
            elif loot == "gold":
                gold_amount = r.choice([1, 2, 3])
                gold += gold_amount
                rp(f"{gold_amount} Gold Was Put In Your Gold Pouch. You Are Now On {gold} Gold", 1)
            elif loot == "gold_chest":
                gold_chest_amount = r.choice([30, 35, 40, 45, 50])
                gold += gold_chest_amount
                rp(f"{gold_chest_amount} Was Added To Your Gold Pouch. You Are Now On {gold} Gold", 1)
            else:
                rp(f"The {loot_name} Wasn't Worth Keeping So You Threw It Away", 1)
            energy_lost_beach_wander = int( 1 / energy_efficenty )
            energy -= energy_lost_beach_wander
            rp(f"You Lost {energy_lost_beach_wander_fish_rod} Energy. You Are Now On {energy}", 1)
            beach_wander_option_3 = ci("Would You Like To Wander Again 'YES'/'NO'", beach_wander, "YES", "NO")
            if beach_wander_option_3 != "option_1":
                beach_wander()

def beach_dig():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    while True:
        if beach_discovered == False:
            rp("You Start Digging The Sand Beneathe You", 1)
            rp("To Hopefully Find An Item", 1)
            rp("That Will Help You Suvive", 1)
            rp("On This Unknown Land", 1)
            while not "fishing_rod" in inventory:
                fishing_rod_dig = quick_time_spam(20, "random", "random", "Dig")
                if fishing_rod_dig == True:
                    rp("You Hit A Solid Wooden Pole", 1)
                    rp("It's A Fishing Rod", 1)
                    rp("This Will Be Handy", 1)
                    energy_lost_beach_dig_fish_rod = int ( 1 * energy_efficenty)
                    energy -= energy_lost_beach_dig_fish_rod
                    rp(f"You Lost {energy_lost_beach_dig_fish_rod} Energy. You Are Now On {energy}", 1)
                    inventory.append("fishing_rod")
                    beach_discovered = True
                    game_started = True
                    keep_digging_1 = ci("Do You Want To Keep Digging? 'YES/'NO'", beach_dig, "YES", "NO")
                    if keep_digging_1 != "option_1":
                        return
                else:
                    rp("You Only Ended Up Only Scraping Up A Thin Layer Of Sand Beneathe You", 1, True)
        else:
            rp("You Start Digging Down Into The Sand", 1)
            dig_spam_event = quick_time_spam(20, "random", "random", "Dig")
            if dig_spam_event == True:
                loot = r.choice(beach_dig_loot)
                if loot == "plank":
                    loot_name = "Plank"
                elif loot == "rock":
                    loot_name = "Rock"
                elif loot == "bone":
                    loot_name = "Bone"
                elif loot == "rubbish":
                    loot_name = "Piece Of Rubbish"
                elif loot == "gold":
                    loot_name = "Gold Coin"
                elif loot == "gold_chest":
                    loot_name = "Gold Chest"
                elif loot == "rock_dweller":
                    loot_name = "Rock Dweller"
                rp(f"You Hit A {loot_name}", 1)
                if loot == "plank" or loot == "rock" or loot == "bone":
                    beach_dig_option_1 = ci(f"Do You Want To Keep The {loot_name} 'YES'/'NO'", beach_dig, "YES", "NO")
                    if beach_dig_option_1 == "option_1":
                        inventory.append(loot)
                        rp(f"{loot_name} Added To Inventory", 1)
                    else:
                        rp(f"You Left The {loot_name}", 1)
                elif loot == "gold":
                    gold_amount = r.choice([1, 2, 3])
                    gold += gold_amount
                    rp(f"{gold_amount} Gold Was Put In Your Gold Pouch. You Are Now On {gold} Gold", 1)
                elif loot == "gold_chest":
                    gold_chest_amount = r.choice([30, 35, 40, 45, 50])
                    gold += gold_chest_amount
                    rp(f"{gold_chest_amount} Was Added To Your Gold Pouch. You Are Now On {gold} Gold", 1)
                elif loot == "rock_dweller":
                    rp("Do You Want To Set The Rock Dweller As Your Companion.", 1)
                    rock_dweller_select = ci("Else It Is Added To Your Inventory 'YES'/'NO'", beach_dig, "YES", "NO")
                    if rock_dweller_select == "option_1":
                        companion = "rock_dweller"
                        rp("Rock Dweller Set As Companion", 1)
                    else:
                        companion_available.append("rock_dweller")
                        rp("Rock Dweller Added To Inventory", 1)
                else:
                    rp(f"The {loot_name} Wasn't Worth Keeping So You Threw It Away", 1)
            else:
                rp("You Failed To Dig Deep Enough", 1)
        energy_lost_beach_dig = 1 * energy_efficenty
        energy -= energy_lost_beach_dig
        rp(f"You Lost {energy_lost_beach_dig} Energy. You Are Now On {energy}", 1)
        beach_dig_option_2 = ci("Would You Like To Dig Again 'YES'/'NO'", beach_dig, "YES", "NO")
        if beach_dig_option_2 != "option_1":
            return

def beach_fish():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    while True:
        if "fishing_rod" in inventory:
            pause_time = r.choice([6, 7, 8, 9, 10, 11])
            rp("You Throw Your Hook Into The Sea", pause_time)
            rp(f"After {pause_time} Seconds Something Hooked Onto Your Fishing Rod")
            fish_spam_event = quick_time_spam(10, "random", "random/2", "Pull Up The Fish")
            if fish_spam_event == True:
                loot = r.choice(beach_fishing_loot)
                if loot == "plank":
                    loot_name = "Plank"
                elif loot == "rock":
                    loot_name = "Rock"
                elif loot == "fish":
                    loot_name = "Fish"
            elif loot == "rubbish":
                loot_name = "Piece Of Rubbish"
            elif loot == "gold":
                loot_name = "Gold Coin"
            elif loot == "gold_chest":
                loot_name = "Gold Chest"
            elif loot == "fish_scaling":
                loot_name = "Fish Scale Base"
            else:
                rp("You Failed To Pull Anythng Up", 1)
            rp(f"You Fished Up A {loot_name}", 1)
            if loot == "plank" or loot == "rock" or loot == "bone":
                beach_fish_option_1 = ci(f"Do You Want To Keep The {loot_name} 'YES'/'NO'", beach_fish, "YES", "NO")
                if beach_fish_option_1 == "option_1":
                    inventory.append(loot)
                    rp(f"{loot_name} Added To Inventory", 1)
                else:
                    rp(f"You Left The {loot_name}", 1)
            elif loot == "gold":
                gold_amount = r.choice([1, 2, 3])
                gold += gold_amount
                rp(f"{gold_amount} Gold Was Put In Your Gold Pouch. You Are Now On {gold} Gold", 1)
            elif loot == "gold_chest":
                gold_chest_amount = r.choice([30, 35, 40, 45, 50])
                gold += gold_chest_amount
                rp(f"{gold_chest_amount} Was Added To Your Gold Pouch. You Are Now On {gold} Gold", 1)
            elif loot == "fish_scaling":
                rp("Do You Want To Set The Fish Scaling As Your Armour Base.", 1)
                fish_scale_select = ci("Else It Is Added To Your Inventory 'YES'/'NO'", beach_fish, "YES", "NO")
                if fish_scale_select == "option_1":
                    armour_base = "fish_scaling"
                    rp("Scale Plating Set As Armour Base", 1)
                else:
                    armour_base_available.append("fish_scaling")
                    rp("Scale Plating Added To Inventory", 1)
            else:
                rp(f"The {loot_name} Wasn't Worth Keeping So You Threw It Away", 1)
        else:
            rp("You Don't Even Have A Fishing Rod", 1, True)
            beach()
            energy_lost_beach_fish = 2 * energy_efficenty
            energy -= energy_lost_beach_fish
            rp(f"You Lost {energy_lost_beach_fish} Energy. You Are Now On {energy}", 1)
            beach_fish_option_2 = ci("Would You Like To Fish Again 'YES'/'NO'", beach_fish, "YES", "NO")
            if beach_fish_option_2 != "option_1":
                return

def overhang():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    while True:
        if overhang_discovered == False:
            rp("As You Walk Of The Gritty Sand You Find A Small Overhang", 1)
            rp("The Smooth Rock Facing Towards The Calming Sea Would Be A Good Place To Rest", 1)
            rp("To Gain 1 Energy It Takes 2 Minutes Of Rest.", 1) 
            rp("A New Energy Will Start Regain Automatically Once One Is Done", 1, True)
            overhang_discovered = True
        else:
            if energy == 30:
                rp("You Don't Need To Rest", 1)
                rp("You Are At Full Energy", 1, True)
                return
            else:
                overhang_choice = ci("You Can Rest Here. 'YES' / 'NO'", overhang, "YES", "NO")
                if overhang_choice == "option 1":
                    rest()
                    return
                else:
                    return
           
def field():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    while True:
        last_checkpoint = field
        if field_discovered == False:
            rp("You Step Of The Irritating Sand And Onto The Lucious Grass", 1)
            rp("You Hear The Mooing Of Cows In The Background", 1)
            rp("The Relaxing Peace Is Quickly Broken By A Man", 1)
            rp("This Is The First Human Interaction You Have Had Since The Ship Wreck", 1)
            rp("As You Go To Great The Man A Flaming Fire Ball Skims Past Your Face", 1)
            rp("This Isn't A Man, Its A Wizard And He Isnt Happy", 1, True)
            wizard_fight()
        elif field_discovered2 == False:
            rp("With The Wizard Gone The Field Feels More Relaxing", 1)
            rp("Some Animals Have Started To Come Back", 1)
            field_optionxtr = ci("You Can 'HUNT' or 'EXPLORE'", field, "HUNT", "EXPLORE")
            if field_optionxtr == "option 1":
                hunt(field)
                field_discovered2 = True
            elif field_optionxtr == "option 2": 
                rp("As You Wander Through The Fresh Lucious Grass", 1)
                rp("You Are Stopped By A Big Towering Mountain", 1)
                rp("With A Dark Gaping Hole That Tunnels Down Deep", 1 )
                rp("And A Contrast Of A Cheerful Village Nearby", 1, True)
                field_discovered2 = True
        else:
            rp("You Can Go To The 'VILLAGE', Climb The 'MOUNTAIN'")
            field_option = ci("Explore The 'CAVE' Or 'HUNT' The Animals", field, "VILLAGE", "MOUNTAIN", "CAVE", "HUNT")
            if field_option == "option 1":
                village()
            elif field_option == "option 2":
                mountain()
            elif field_option == "option 3":
                cave()
            elif field_option == "option 4":
                hunt(field)
            elif field_option == "back":
                return
       
def forest():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    while True:
        last_checkpoint = forest
        if forest_discovered == False:
            rp("The Disctint Salty Smell Of The Beach Fades Away", 1)
            rp("Into The Leafy Scent Of The Forest", 1)
            rp("The Tall Trees And Their Bushy Leaves Block Out Much Of The Sunlight", 1)
            rp("The Floor Is Covered In A Range Of Moss, Fungi, Leaves, And Animals")
            rp("The Sticks Look Dry And Flammable", 1, True)
            forest_discovered = True
        elif village_discovered == True and forest_monster_killed == False:
            rp("You Should Have Take Then Villager's Warning", 1)
            werewolf_fight()
        elif "villager's_axe" in inventory and inventory.count("villager's_log") < 30:
            rp("You Are Here To Gather Logs For The Villagers")
            chop(forest, 'villager job')
        elif "villager's_axe" in inventory or "axe" in inventory:
            forest_choice = ci("You Can 'GATHER' Resources, 'CHOP' Logs Or Go To The 'RIVER', 'SWAMP' Or  A Loneley 'HUT'", forest, "GATHER", "CHOP", "RIVER", "SWAMP", "HUT")
            if forest_choice == "option 1":
                gather(forest)
            elif forest_choice == "option 2":
                chop(forest, 'normal')
            elif forest_choice == "option 3":
                river()
            elif forest_choice == "option 4":
                swamp()
            elif forest_choice == "option 5":
                hut()
            elif forest_choice == "back":
                return
        else:   
            forest_choice = ci("You Can 'GATHER' Resources Or Go To The 'RIVER', 'SWAMP' Or A Lonely 'HUT", forest, "GATHER", "RIVER", "SWAMP", "HUT")
            if forest_choice == "option 1":
                gather(forest)
            elif forest_choice == "option 2":
                river()
            elif forest_choice == "option 3":   
                swamp()
            elif forest_choice == "option 4":
                hut()
            elif forest_choice == "back":
                return

def village():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    while True:
        last_checkpoint = village
        if village_discovered == False:
            rp("As You Walk Into The First Civilisation", 1)
            rp("You Have Seen Since You Landed Here", 1)
            rp("The Bustling Town Awaken A Long Forgetton Feeling", 1)
            rp("Of Belonging But Also Hard Labour", 1)
            rp("However You Don't Have Long Before You Are Noticed", 1)
            rp("They Don't Trust You But Are Willing To With Proof", 1)
            rp("Take This Axe And Collect 30 Logs From The Forest", 1)
            rp("And Then Come Back And Delieve Them To Earn Their Trust", 1)
            if "villager's_axe" not in inventory:
                inventory.append("villager's_axe")
                rp("Villager's Axe Added To Inventory", 1, True)
            else:
                print()
            village_discovered = True
            return
        elif village_first_job == False:
            if inventory.count("villager's_log") < 30:
                rp("You Don't Have Enough Logs Yet", 1, True)
                return
            elif inventory.count("villager's_log") >= 30:
                log_taken = inventory.count("villager's_log")
                for count in range(1, log_taken + 1):
                    inventory.remove("villager's_log")
                rp("The Villagers Are Thankful For Your Help", 1)
                rp("They Can Now Stay Warm And Away From The Monster In The Woods", 1)
                rp("You Didn't See Any Monster?", 1)
                rp("Villager Discovered. Come Back Her For Trading and Working", 1, True)
                village_first_job = True
        elif forest_monster_killed == True and monster_responce == False:
            rp("The Villagers See You Walk Back Clothes Ripped And Slashed", 1)
            rp("And Your Weapon Covered In Blood", 1)
            rp("They Are Suprised To Learn You You Killed The Werewolf", 1)
            if cursed == True:
                rp("But Are Significantly Worried About Your New Tail And Sharp Teeth", 1)
                rp("Their Medical Team Will Sort That Out For You For A Bit Of Gold Later", 1)
            rp("However They Do Not Know What The Orb Is Either. They Suggest Looking Up The Mountain", 1, True)
            monster_responce == True
        elif village_purged == True:
            rp("Here Lie The Remainents Of The Only Civilisation On This Island", 1)
            rp("That You Killed", 1)
            rp("Anyway Other Locations Non-Exsitant Yet", 1)
            rp("Back To Field")
            return
        else:
            rp("Welcome To The Village")
            village_choice = ci("You Can 'TRADE', 'WORK', 'MASSACRE' {NOT AVAILABLE YET}, 'HEAL' or {NEW LOCATIONS NOT AVAILALE YET}", village, "TRADE", "WORK", "MASSACRE", "HEAL", "CHEST")
            if village_choice == "option_1":
                trade()
            elif village_choice == "option_2":
                work()
            elif village_choice == "option_3":
                massacre()
            elif village_choice == "option_4":
                heal()
            elif village_choice == "option_5" and village_chest == False:
                rp("You Walk Into A Random Villagers House And Loot It", 1)
                rp("You Got 5 Gold And 1 Bread", 1)
                inventory.append("bread")
                gold += 5
            else:
                return

def mountain(): 
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    while True:
        print("THIS AREA IS NOT AVAILABLE YET")
        print("RETURNING TO FIELD")
        return
        rp("Climbing The Mountain Has Become Exhasting And Difficult")
        climbed_mountain == False
        climb_left1 = quick_time_event(2, "random", "Lift Your Left Foot Up")
        if climb_left1 == True:
            climb_right1 = quick_time_event(2, "random", "Lift Your Right Foot Up")
            if climb_right1 == True:
                climb_left2 = quick_time_event(2, "random", "To Lift Your Left Foot Up")
                if climb_left2 == True:
                    climb_right2 = quick_time_event(2, "random", "Lift Your Right Foot Up")
                    if climb_right2 == True:
                        climb_left3 = quick_time_event(2, "random", "Lift Your Left Foot Up")
                        if climb_left3 == True:
                            climb_right3 = quick_time_event(2, "random", "Lift Your Left Foot Up")
                            if climb_right3 == True:
                                climbed_mountain = True
                                rp("The Climb Was Exhasting", 1)
                                energy_lost = 10 / energy_efficenty
                                energy -= energy_lost
                                rp(f"You Lost {energy_lost} Energy. You Are Now On {energy}",  1, True)
        if climbed_mountain == False:
            rp("You Gave Up And Fell Back Down The Mountain", 1)
            energy_lost = 8 / energy_efficenty
            energy -= energy_lost
            rp(f"You Lost {energy_lost} Energy. You Are Now On {energy}", 1, True)
            return
        rp("You Managed To Climb The Mountain", 1)
        if "weird_orb" in inventory:
            rp("The Weird Glowing Orb Lift Away From You", 1)
            rp("It Glides Towards A Seemling Normal Wall", 1)
            rp("Untill The Snow And Ice Cracks Of It", 1)
            rp("Revealing A Mystical Hierlyphic Door", 1)
            inventory.remove('weird_orb')
            rp("Opening It Revealing A Weird Temple", 1)
            mountain_door = True 
        if montain_discovered == False:
            rp("You Hear A Loud Roar With A Wave Heat Soon After", 1)
            rp("And The Audioable Flapping", 1)
            dragon_fight()
        else:


def cave():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    while True:
        print("THIS AREA IS NOT AVAILABLE YET")
        print("RETURNING TO FIELD")
        return

def river():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    while True:
        print("THIS AREA IS NOT AVAILABLE YET")
        print("RETURNING TO FOREST")
        return

def swamp():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    while True:
        print("THIS AREA IS NOT AVAILABLE YET")
        print("RETURNING TO FOREST")
        return

def hut():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    while True:
        print("THIS AREA IS NOT AVAILABLE YET")
        print("RETURNING TO FOREST")
        return

def ending_1():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    rp("After Standing Up And Thinking For A Bit", 1)
    rp("You Realise These Are Horrible Terms To Live With", 1)
    rp("So You Lie Back Down And Fall Back To Sleep", 1)
    rp("Allowing Nature To Take Your Body", 1)
    rp("Ending 1 Unlocked!", 1)
    rp("You Unlocked The Ice Thread Armour Lining", 1)
    rp("It Slows Enemies Around You", 1)
    ending_1_choice = ci("Would You Like To Equip It? 'YES' / 'NO'", ending_1, "YES", "NO")
    if ending_1_choice == "option_1":
        if armour_lining != "none":
            armour_lining_available.append(companion)
        armour_lining = "ice_thread"
        rp("Ice Thread Armour Lining Equipped", 1, True)
    else:
        armour_lining_available.append("ice_thread")
        rp("Ice Thread Armour Lining Added To Available Armour Linings", 1, True)   
    return

def ending_2():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    rp("With All Your Planks Your Start Building A Ship", 1, False, True)
    rp("It's How This Journy Started, On The Seas", 1, False, True)
    rp("The Mystery Of The Island Or Your Memory Was Never Discovered", 1, False, True)
    rp("But You Did Feel The Connection In Pirating", 1, False, True)
    rp("Ending 2 Unlocked!", 1, False, True)
    rp("You Unlocked The Parrot Companion", 1, False, True)
    rp("It Copies Your Attacks So You Do Double Damage", 1, False, True)
    ending_2_choice = ci("Would You Like To Equip It? 'YES'/'NO'", ending_2, "YES", "NO")
    if ending_2_choice == "option 1":
        if companion != "none":
            companion_available.append(companion)
        companion = "parrot"
        rp("Parrot Equipped", 1, True, False)
    else:
        companion_available.append("parrot")
        rp("Parrot Added To Available Companions", True, False)
    return

def ending_3():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    rp(f"You Feel Your Mind Fading To The New Animal Nature In Your Body", 1, False, True)
    rp(f"Your Last Thought Before You Become A Creature Of The Night", 1, False, True)
    rp(f"Was The Terror You Felt Looking At The Werewolf", 1, False, True)
    rp(f"Knowing You Were About To Become One", 1, False, True)
    rp(f"Ending 3 Unlocked!", 1, False, True)
    rp(f"You Unlocked The Wolf Companion", 1, False, True)
    rp(f"It Gives A Small Boost To Damage And Resientence", 1, False, True)
    ending_3_choice = ci("Would You Like To Equip It? 'YES'/'NO'", ending_3, "YES", "NO")
    if ending_3_choice == "option 1":
        if companion != "none":
            companion_available.append(companion)
        companion = "wolf"
        rp(f"Wolf Companion Equipped", 1, True)
    else:
        companion_available.append("wolf")
        rp("Wolf Added To Available Companions", 1, True)
    rp(f"You Did Die Though", 1)
    health = 0
    refresh_all(False, True)
    return


def wizard_fight():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    fight_signal()
    while wiz_health > 0 and health > 0:
        wiz_ran = r.choice(["attack", "defend"])
        if wiz_ran == "attack":
            wiz_crit = r.choices(
                [True, False],
                weights = [crit_chance, 100],
                ) 
            if wiz_crit == True:
                wiz_crit_attack = quick_time_double(5, "random", "random", "Critical Attack The Wizard")
                t.sleep(1)
                if wiz_crit_attack == True:
                    rp("You Landed A Critical Hit On The Wizard", 1, False, True)
                    crit_wiz_damage = damage * crit_multiplier
                    wiz_health -= crit_wiz_damage
                    rp(f"You Did {crit_wiz_damage} Damage. The Wizard Now Has {wiz_health} Health Left", 1, True, True)
                else:
                    rp("You Missed Your Critical Hit On The Wizard", 1, True, True)
            else:
                wiz_attack = quick_time_event(5, "random", "Attack The Wizard")
                t.sleep(1)
                if wiz_attack == True:
                    rp("You Landed An Attack On The Wizard", 1)
                    wiz_damage = damage
                    wiz_health -= wiz_damage
                    rp(f"You Did {wiz_damage} Damage. The Wizard Now Has {wiz_health} Health Left", 1, False, True)
                else:
                    rp("You Missed Your Attack On The Wizard", 1, True, True)
        else:
            dodge_wiz = quick_time_event(5, "random", "Dodge The Incoming Fireball")
            t.sleep(1)
            if dodge_wiz == True:
                rp("You Dodged The Incoming Fireball", 1, True, True)
            else:
                rp("You Gazed Into The Flaming Ball Of Fire As It Came Crashing Down On You", 1, False, True)
                wiz_health_lost = int ( 2 / damage_resistence )
                health -= wiz_health_lost
                rp(f"You Lost {wiz_health_lost} Damage. You Now Have {health} Health Left", 1, True, True)
        if wiz_health <= 0:
            rp("You Defeated The Wizard", 1)
            rp("Unexpectedly Before His Body Falls To The Ground", 1)
            rp("His Entire Body Fades Away Into Thin Air", 1)
            rp("Leaving Only A Book", 1)
            rp("The Book Contains Spells But Is Missing Many Pages", 1)
            rp("You Have Unlocked The Class Wizard", 1)
            rp("You Have Unlocked The Spell Fireball", 1)
            rp("Would Like To Equip It? 'YES' / 'NO'", 1)
            wiz_activate = str(input())
            print()
            t.sleep(1)
            if wiz_activate == "YES":
                class_ = "wizard"
                class_available.append("fighter")
                weapon_available.append("none")
                spell = "fireball"
                rp("Wizard Class Equipped With Fireball Spell", 1)
            else:
                class_available.append("wizard")
                spell_available.append("fireball")
                rp("Wizard Class And Fireball Spell Added To Available Classes And Spells", 1)
            t.sleep(1)
            print()
            field_discovered = True
            field()
        if health <= 0:
            rp("You Have Been Defeated By The Wizard", 1)

def werewolf_fight():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global splash_range, splash_damage, piercing
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    rp("As A Full Moons Reveals Itself Through The Thick Branches", 1, False, True)
    rp("You Hear A Loud Howling Coming Towards You", 1, False, True)
    fight_signal()
    werewolf_health = 50
    werewolf_effects = []
    cursed = []
    prev_attack = False
    while werewolf_health > 0 and health > 0:
        if "level-10" in cursed:
            ending_3()
            return
        elif "level-9.5" in cursed:
            cursed.append("level-10")
        elif "level-9" in cursed:
            rp("Fur Starts To Poke And Shred Throught Your Skin", 1, False, True)
            health -= 3
            rp(f"You Lost 3 Health. You Are Now On {health} Health", True, True)
            cursed.append("level-9.5")
        elif "level-8.5" in cursed:
            cursed.append("level-9")
        elif "level-8" in cursed:
            rp("You Teeth Morph And Sharpen Within Your Own Mouth Leaving It Disfigued", False, True)
            health -= 3
            rp(f"You Lost 3 Health. You Are Now On {health} Health", False, True)
            cursed.append("level-8.5")
        elif "level-7.5" in cursed:
            cursed.append("level-8")
        elif "level-7" in cursed:
            rp("Your Bones Crack And Your Skin Streches As Your Grow", 1, False, True)
            health -= 3
            rp(f"You Lost 3 Health. You Are On {health} Health.", 1, True, True)
            cursed.append("level-7.5")
        elif "level-6.5" in cursed:
            cursed.append("level-7")
        elif "level-6" in cursed:
            rp(f"Sharp Claws Grow Out Of Your Hands And Feet Popping Your Nails Of In The Process", 1, False, True)
            health -= 2
            rp(f"You Lost 2 Health. You Are On {health} Health.", 1, True, True)
            cursed.append("level-6.5")
        elif "level-5.5" in cursed:
            cursed.append("level-6")
        elif "level-5" in cursed:
            rp(f"A Tail Starts To Poke Through Your Tail Bone Ripping The Skin Along The Way", 1, False, True)
            health -= 2
            rp(f"You Lost 2 Health. You Are On {health} Health.", 1, True, True)
            cursed.append("level-5.5")
        elif "level-4.5" in cursed:
            cursed.append("level-5")
        elif "level-4" in cursed:
            rp("Your Nose Starts To Extend Out Of Your Face Into The Shape Of An Animal", 1, False, True)
            health -= 1
            rp(f"You Lost 1 Health. You Are On {health} Health", 1, True, True)
            cursed.append("level-4.5")
        elif "level-3.5" in cursed:
            cursed.append("level-4")
        elif "level-3" in cursed:
            rp("Without Relising It You Start Running On All Fours", 1, False, True)
            health -= 1
            rp(f"You Lost 1 Health. You Are On {health} Health.", 1, True, True)
            cursed.append("level-3.5")
        elif "level-2.5" in cursed:
            cursed.append("level-3")
        elif "level-2" in cursed:
            rp(f"The Colour From Your Eyes Fade Into The Shade Of The Glistening Moon", 1, False, True)
            health -= 1
            rp(f"You Lost 1 Health. You Are Now On {health} Health", 1, True, True)
            cursed.append("level-2.5")
        elif "level-1.5" in cursed:
            cursed.append("level-2")
        elif "level-1" in cursed:
            cursed.append("level-1.5")
        ww_aod = r.choice(["attack", "defend"])
        if len(werewolf_effects) > 0:
            if "burning" in werewolf_effects:
                werewolf_health -= 3
                rp(f"The Werewolf Took 3 Damage From The Flames. It Now Has {werewolf_health} Health", 1, False, True)
                if this_weather == "raining":
                    werewolf_effects.remove("burning")
                    rp(f"The Rain Put Out The Flames On The Werewolf", 1, False, True)
                elif this_weather == "snowing":
                    werewolf_effects.remove("burning")
                    rp(f"The Snow Put Out The Flames On The Werewolf", 1, False, True)
                elif this_weather == "thunderstorming":
                    werewolf_effects.remove("burning")
                    rp(f"The Thunderstorm Put Out The Flames On The Werewolf", 1, False, True)
                else:
                    recover = r.choice([True, False])
                    if recover == True:
                        werewolf_effects.remove("burning")
                        rp(f"The Werewolf Recovered From Being Posioned", 1, False, True)
            if "freezing" in werewolf_effects:
                if this_weather != "heatwave":
                    ww_aod = r.choice(["attack", "attack", "attack", "defend"])
                    if ww_aod == "attack":
                        rp(f"The Werewolf Is Frozen In Place. Your Turn To Attack", 1, False, True)
                else: 
                    werewolf_effects.remove("freezing")
                    rp(f"The Heatwave Defrosted The Werewolf", 1, False, True)
            if "posioning" in werewolf_effects:
                werewolf_health -= 1
                rp(f"The Werewolf Took 1 Damage From The Posion")
                recover = r.choice([True, False, False, False])
                if recover == True:
                    werewolf_effects.remove("posioning")
                    rp(f"The Werewolf Recovered From Being Frozen")
            if "shocking" in werewolf_effects:
                if prev_attack == False:
                    ww_aod = "attack"
                else:
                    ww_aod = r.choice(["attack", "attack", "defend"])
                if ww_aod == "attack":
                    rp(f"The Werewolf Was Stunned. Your Turn To Attack")
                werewolf_effects.remove("shocked")
        if ww_aod == "defend":
            ww_attack = r.choice(["charge", "pounce", "summon"])
            if ww_attack == "charge":
                dodge = quick_time_event(3, "random", "Roll Away From The Charge Path")
                if dodge == True:
                    counter = r.choice([True, False, False])
                    if counter == True:
                        counter = quick_time_event(4, "random", "Hit A Counter Attack")
                        if counter == True:
                            werewolf_health -= damage
                            werewolf_effects.extend(damage_affects)
                            prev_attack = True
                            rp("You Dodged The Werewolf's Charge", 1, False, True)
                            rp("And Landed A Counter Hit", 1, False, True)
                            rp(f"The Werewold Lost {damage} Health. It Now Has {werewolf_health} Health", 1, False, True)
                            if len(werewolf_effects) > 0:
                                rp(f"You Applied {damage_affects} To The Werewolf", False, True)
                        elif counter == False:
                            rp("You Dodged The Werewolf's Charge But Missed The Counter", 1, False, True)
                    elif counter == False:
                        rp("You Dodged The Werewolf's Charge", 1, False, True)
                        prev_attack = False
                elif dodge == False:
                    damage_done = 8 / damage_resistence
                    health -= damage_done
                    rp(f"The Werewolf Charged Into You Dealing {damage_done} Health. You Have {health} Health Left", 1, False, True)
                    prev_attack = False
            elif ww_attack == "pounce":
                get_of_me = quick_time_spam(4, "random", r.choice([25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), "Get The Werewolf Of You As It Tries To Bite Your Head Of")
                if get_of_me == True:
                    rp("You Pushed The Wolf Off You Saving You From It's Bite", 1, False, True)
                else:
                    damage_done = 12 / damage_resistence
                    health -= damage_done
                    rp(f"The Werewolf Bit You For {damage_done} Health. You Have {health} Health Left.", 1, False, True)
                    if "level-1" not in cursed:
                        rp(f"You Feel Something Weird Flowing Through Your Blood", 1, False, True)
                        rp(f"Something Animlistic", 1, False, True)
                        rp(f"But There Isn't Time To Investigate It During This Fight", 1, False, True)
                prev_attack = False
            elif ww_attack == "summon":
                wolf_1 = 5
                wolf_2 = 5
                rp("The Werewolf Has Summoned 2 Wolfs To Attack You", 1, False, True)
                rp("Each One Has 2 Health", 1, False, True)
                while ( wolf_1 > 0 or wolf_2 > 0 ) and health > 0:
                    if wolf_1 > 0 and wolf_2 > 0:
                        l_or_r = quick_time_choice(4, "random", "random", "Target The Left One", "Target The Right One")
                        if l_or_r == "Option 1":
                            attack_left = quick_time_event(3, "random", "Attack The Left Wolf")
                            if attack_left == True:
                                wolf_1 -= damage
                                rp(f"You Did {damage} Damage To Wolf 1. It Has {wolf_1} Health Left", 1, False, True)
                                if splash_range >= 2:
                                    wolf_2 -= splash_damage
                                    rp(f"You Did {splash_damage} Splash Damage To Wolf 2. It Has {wolf_2} Health Left", 1, False, True)
                                elif piercing >= 2:
                                    wolf_2 -= damage
                                    rp(f"You Did {splash_damage} Piercing Damage To Wolf 2. It Has {wolf_2} Health Left", 1, False, True)
                            else:
                                damage_done = 7 / damage_resistence
                                health -= damage_done
                                rp(f"You Missed Your Attack And Both Wolfs Attacked You For {damage_done} Health", 1, False, True)
                                rp(f"You Are Now On {health} Health", 1, False, True)
                        elif l_or_r == "Option 2":
                            attack_right = quick_time_event(3, "random", "Attack The Right Wolf")
                            if attack_right == True:
                                wolf_2 -= damage
                                rp(f"You Did {damage} Damage To Wolf 2. It Has {wolf_2} Health Left", 1, False, True)
                                if splash_range >= 2:
                                    wolf_1 -= splash_damage
                                    rp(f"You Did {splash_damage} Damage To Wolf 1. It Has {wolf_1} Health Left", 1, False, True)
                                elif piercing >= 2:
                                    wolf_2 -= damage
                                    rp(f"You Did {splash_damage} Piercing Damage To Wolf 2. It Has {wolf_2} Health Left", 1, False, True)
                            else:
                                damage_done = 7 / damage_resistence
                                health -= damage_done
                                rp(f"You Missed Your Attack And Both Wolfs Attacked You For {damage_done} Health", 1, False, True)
                                rp(f"You Are Now On {health} Health", 1, False, True)
                        else:
                            damage_done = 7 / damage_resistence
                            health -= damage_done
                            rp(f"You Couldn't Choose Before They Attacked You For {damage_done} Health", 1, False, True)
                            rp(f"You Are Now On {health} Health", 1, False, True)
                    elif wolf_1 <= 0 and wolf_2 > 0:  
                        attack_right = quick_time_event(3, "random", "Attack The Right Wolf")
                        if attack_right == True:
                            wolf_2 -= damage
                            rp(f"You Did {damage} To Wolf 2. It Now Has {wolf_2} Health", 1, False, True)
                        else:
                            damage_done = 3 / damage_resistence
                            health -= damage_done
                            rp(f"You Missed Your Attack And Got Hit For {damage_done} Health", 1, False, True)
                            rp(f"You Are Now On {health} Health", 1, False, True)
                    elif wolf_2 <= 0 and wolf_1 > 0:
                        attack_left = quick_time_event(3, "random", "Attack The Left Wolf", 1, False, True)
                        if attack_left == True:
                            wolf_1 -= damage_done
                            rp(f"You Did {damage} To Wolf 1. It Now Has {wolf_1} Health", 1, False, True)
                        else:
                            damage_done = 3 / damage_resistence
                            health -= damage_done
                            rp(f"You Missed Your Attack And Got Hit For {damage_done} Health", 1, False, True)
                            rp(f"You Are Now On {health} Health", 1, False, True)
                    print()
                if wolf_1 <= 0 and wolf_2 <= 0:
                    rp(f"You Deafeated The Two Wolves")
                    prev_attack = False
        elif ww_aod == "attack":
            crit_yn = r.randint(1, 100)
            if prev_attack == True and crit_yn <= crit_chance: 
                crit_attack = quick_time_double(4, "random", "random", "Critical Hit The Werewolf")
                if crit_attack == True:
                    damage_done = damage * crit_multiplier
                    werewolf_health -= damage_done
                    rp(f"You Critical Hit The Wolf For {damage_done}. It Now Has {werewolf_health} Health", 1, False, True)
                    if len(damage_affects) > 0:
                        werewolf_effects.extend(damage_affects)
                        rp(f"You Applied {damage_affects} To The Werewolf", 1, False, True)
                    prev_attack = False
                else:
                    rp(f"You Missed Your Critical Hit", 1, False, True)
                    prev_attack = False
            else:
                attack = quick_time_event(3, "random", "Attack The Werewolf")
                if attack == True:
                    werewolf_health -= damage
                    rp(f"You Hit The Werewolf For {damage}. It Now Has {werewolf_health} Health", 1, False, True)
                else:
                    rp("You Missed Your Attack", 1, False, True)
        print()
    if werewolf_health <= 0:
        rp(f"You Defeated The Werewolf", 1, False, True)
        rp(f"It Transfers Back Into A Regular Human", 1, False, True)
        rp(f"As It Falls To The Ground It Drops A Weird Shimmering Sphere", 1, False, True)
        rp(f"Maybe The Villagers Know What To Do With It", 1, False, True)
        if len(cursed) > 0:
            rp(f"Talking About That You Still Feel The Animilisic Urge Within You", 1, False, True)
            rp(f"Something To Get Sorted Before It Goes To Far", 1, True)
            cursed = True
        print()
        inventory.append("weird_orb")
        forest_monster_killed = True
        return
    if health <= 0:
        rp(f"The Werewold Killed You", 1, False, True)
        refresh_all(False, True)
        return

def dragon_fight():
    fight_signal()
    dragon_health = 100
    dragon_effects = []
    while dragon_health

def hunt(previous_location):
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global splash_range, splash_damage, piercing
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    keep_hunt = "option 1"
    rp("You Are Hunting", 1)
    while keep_hunt == "option 1":
        if previous_location == field:
            animal = r.choice(["Cow", "Sheep", "Rabbit"])
        if animal == "Cow":
            animal_health = 5
        elif animal == "Sheep":
            animal_health = 4
        elif animal == "Rabbit":
            animal_health = 2
        rp(f"You Encounter A {animal}. It Has {animal_health} Health", 1)
        while animal_health > 0:
            attack = waitandhit("random", "random", f"Attack The {animal}")
            if attack == True:
                animal_health -= damage
                if animal_health <= 0:
                    animal_health = 0
                rp(f"You Did {damage} Damage. The {animal} Now Has {animal_health} Health Left", 1)
            else:
                rp(f"You Missed Your Attack On The {animal}", 1)
        rp(f"You Defeated The {animal}", 1)
        if animal == "Cow":
            if "burning" in damage_affects:
                rp(f"Your Weapon Cooked The {animal}", 1)
                inventory.append("cooked_beef")
                rp("Cooked Beef Added To Inventory", 1)
            else:
                inventory.append("raw_beef")
                rp("Raw Beef Added To Inventory", 1)
            inventory.append("leather")
            rp("Leather Added To Inventory", 1, True)
        elif animal == "Sheep":
            if "burning" in damage_affects:
                rp(f"Your Weapon Cooked The {animal}", 1)
                inventory.append("cooked_mutton")
                rp("Cooked Mutton Added To Inventory", 1)
            else:
                inventory.append("raw_mutton")
                rp("Raw Mutton Added To Inventory", 1)
            inventory.append("wool")
            rp("Wool Added To Inventory", 1, True)
        elif animal == "Rabbit":
            rp(f"There Wasn't Enough Meat On The {animal}", 1)
            inventory.append("rabbit_hide")
            rp("Rabbit Hide Added To Inventory", 1, True)
        keep_hunt = ci("Do You Want To Keep Hunting? 'YES' / 'NO'", hunt, "YES", "NO")
    return

def gather(previous_location): 
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global splash_range, splash_damage, piercing
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done 
    keep_gather = "option_1"
    rp("You Are Gathering Resources", 1)
    if previous_location == forest:
        resources = ["stick", "leaf", "mushroom", "honey"]
    gather_choice = cfl(resources, f"You Can Gather {resources}", forest)
    while keep_gather == "option_1":
        if gather_choice == "stick":
            correct_option = r.choice(["option 1", "option 2"])
            if correct_option == "option 1":
                stick_pickup = quick_time_choice(3, "random", "random", "Pick Up The Stick", "Step On The Stick")
                if stick_pickup == "option 1":
                    inventory.append("stick")
                    rp("You Picked Up A Stick. It Has Been Added To Your Inventory", 1)
                    if inventory.count("stick") == 1:
                        rp(f"You Now Have 1 Stick In Your Inventory", 1, True)
                    else:
                        rp(f"You Have {inventory.count("stick")} In Your Inventory")
                elif stick_pickup == "option 2":
                    rp("You Crushed The Stick", 1, True)
                else:
                    rp("You Missed The Stick Before A Bird Took It", 1, True)
            elif correct_option == "option 2":
                stick_pickup = quick_time_choice(3, "random", "random", "Step On The Stick", "Pick Up The Stick")
                if stick_pickup == "option 1":
                    rp("You Crushed The Stick", 1, True)
                elif stick_pickup == "option 2":
                    inventory.append("stick")
                    rp("You Picked Up A Stick. It Has Been Added To You Inventory", 1)
                    if inventory.count("stick") == 1:
                        rp("You Now Have 1 Stick In Your Inventory", 1, True)
                    else:
                        rp(f"You Have {inventory.count("stick")} Sticks", 1, True)
        elif gather_choice == "honey":
            honey_pickup = countspam(r.choices([5, 6, 7, 8, 9, 10]), "random", "Grab Honey Before The Bees Push You Out")
            for amount in range(0, honey_pickup):
                inventory.append("honeycomb")
            rp(f"You Gathered {honey_pickup} Honeycombs Before You Were Pushed Out", 1)
            rp(f"You Now Have {inventory.count("honeycomb")} In Your Inventory", 1, True)
        elif gather_choice == "mushroom":
            rp("You Are Hunting For Mushrooms")
            mushroom_count = int(input("How Many Mushrooms Would You Like To Gather: "))
            rp("Key:", 0.5)
            rp("Spotty: Poisonous If Paired With Another Poisonous Trait", 1)
            rp("Streaky: Completely Safe To Eat", 1)
            rp("Tiger Patturn: Completely Posionous", 1)
            rp("No Patturns: No Correlation To Posion", 1)
            rp("Red: Poisonous If Paired With Another Poisonous Trait", 1)
            rp("Brown: Safe Unless Paried With A Completly Posionous Trait", 1)
            rp("White: No Correlation", 1)
            mushrooms = ["Spotty Red", "Spotty Brown", "Spotty White", "Streaky Red", "Streaky Brown", "Streaky White", "Tiger Stripes Red"]
            poisionous = ["Spotty Red", "Tiger Stripes Red", "Tiger Stripes Brown", "Tiger Stripes White",]
            safe = ["Spotty Brown", "Spotty White", "Streaky Red", "Streaky Brown", "Streaky White", "Patturnless Red", "Patturnless Brown", "Patturnless White"]
            total_mushrooms_picked = 0
            safe_mushrooms_picked = 0
            poisionous_muchrooms_picked = 0
            mushrooms_failed = 0
            for count in range(1, mushroom_count + 1):
                correct_option = r.choice(["option 1", "option 2"])
                if correct_option == "option 1":
                    option_1 = r.choice(safe)
                    option_2 = r.choice(poisionous)
                elif correct_option == "option 2":
                    option_1 = r.choice(poisionous)
                    option_2 = r.choice(safe)
                forage = quick_time_choice(5, "random", "random", f"Forage A {option_1}", f"Forage A {option_2}")
                if forage == "Option 1":
                    total_mushrooms_picked += 1
                    if option_1 in safe:
                        safe_mushrooms_picked += 1
                        inventory.append("safe_mushroom")
                        rp("You Picked A Safe Mushroom", 1)
                    elif option_1 in poisionous:
                        poisionous_muchrooms_picked += 1
                        inventory.append("poisionous_mushrooms")
                        rp("You Picked A Poisionous Mushroom", 1)
                elif forage == "Option 2":
                    total_mushrooms_picked += 1
                    if option_2 in safe:
                        safe_mushrooms_picked += 1
                        inventory.append("safe_mushroom")
                        rp("You A Picked A Safe Mushroom", 1)
                    elif option_2 in poisionous:
                        poisionous_muchrooms_picked += 1
                        inventory.append("posisonous_muchroom")
                        rp("You Picked A Posionous Mushroom", 1)
                elif forage == False:
                    mushrooms_failed += 1
                    rp("You Failed To Choose A Mushroom", 1)
                print()
            rp(f"You Picked {total_mushrooms_picked} Mushrooms", 1)
            rp(f"{safe_mushrooms_picked} Of Which Were Safe", 1)
            rp(f"And {poisionous_muchrooms_picked} Were Posisionous", 1)
            rp(f"You Failed To Pick Up {mushrooms_failed} Mushrooms", 1, True)
        elif gather_choice == "leaf":
            leaf_count = 0
            amount = int(input("How Many Handfuls Of Leaves Do You Want To Grab: "))
            for count in range(1, amount + 1):
                jump = quick_time_event(2, "random", "Jump")
                if jump == True:
                    grab = quick_time_event(2, "random", "Grab The Leaves")
                    if grab == True:
                        added = r.choice([3, 4, 5, 6, 7, 8])
                        leaf_count += added
            for count in range(1, leaf_count + 1):
                inventory.append("leaf")
            rp(f"{leaf_count} Leaves Added To Your Inventory")
        keep_gather = ci("Do You Want Keep Hunting. 'YES'/'", gather, "YES", "NO")
    return

def chop(previous_location, mode):
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global splash_range, splash_damage, piercing
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    if mode == "villager job":
        amount_to_chop = 30 - inventory.count("villager's_logs")
        rp("You Are Chopping Logs For The Villagers", 1)
    elif mode == "normal":
        amount_to_chop = int(input("How Many Logs Do You Want To Chop: "))
        rp("You Are Chopping Logs For Yourself")
    rp("You Must Spam The Correct Key At Least 30 Time", 1)
    rp("And Hit Another Key At The Perfect Time", 1)
    rp("To Cut The Log", 1, True)
    for count in range(1, amount_to_chop + 1):
        strength = countspam(7, "random", "Charge The Swing Of The Axe")
        rp("Wait", r.choice([3, 4, 5, 6, 7, 8]))
        chop = quick_time_event(1, "random", "Chop Now")
        if strength >= 30 and chop == True:
            rp("You Successfully Chopped Through The Log", 1)
            if mode == "villager job":
                inventory.append("villager's_log")
                rp("1 Villager's Log Added To Inventory", 1, True)
            elif mode == "normal":
                inventory.append("log")
                rp("1 Log Added To Inventory", 1, True)
        elif strength < 30 and chop == True:
            rp("You Hit The Log But It Didn't Cut Through", 1, True)
        elif strength >= 30 and chop == False:
            rp("You Swing Was Strong But You Missed The Log", 1, True)
        elif strength < 30 and chop == False:
            rp("You Swing Was Bad And You Missed The Log", 1)
            health -= 1
            rp("Your Bad Technique Cost You 1 Health", 1, True)
    return

def trade():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global splash_range, splash_damage, piercing
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    trade_list_food = ["bread", "berries", "soup", "sweets"]
    trade_list_weapon = ["spear", "mace", "frozen_arrow", "drill_arrow"]
    trade_list_class = ["archer"]
    trade_list_item = ["stick", "rock", "plank"]
    continue_ = True
    if gold <= 0:
        rp(f"You Have {gold}. Not Enough")
        village()
    while continue_ == True:
        if class_ == "archer" or "archer" in class_available:
            trade_list = [r.choice(trade_list_food), r.choice(trade_list_weapon), r.choice(trade_list_item)]
        else: 
            trade_list = [r.choice(trade_list_food), r.choice(trade_list_weapon), r.choice(trade_list_item), r.choice(trade_list_class),]
        rp(f"Selection From:", 0.5)
        if trade_list[0] == "bread":
            rp(f"{trade_list[0]} - 2 Gold", 0.5)
        elif trade_list[0] == "berries":
            rp(f"{trade_list[0]} - 1 Gold", 0.5)
        elif trade_list[0] == "soup":
            rp(f"{trade_list[0]} - 3 Gold", 0.5)
        elif trade_list[0] == "sweets":
            rp(f"{trade_list[0]} - 1 Gold", 0.5)
        if trade_list[1] == "spear":
            rp(f"{trade_list[1]} - 2 Gold", 0.5)
        elif trade_list[1] == "mace":
            rp(f"{trade_list[1]} - 3 Gold", 0.5)
        elif trade_list[1] == "frozen_arrow":
            rp(f"{trade_list[1]} - 5 Gold", 0.5)
        elif trade_list[1] == "drill_arrow":
            rp(f"{trade_list[1]} - 11 Gold", 0.5)
        if trade_list[2] == "stick":
            rp(f"{trade_list[2]} - 1 Gold", 0.5)
        elif trade_list[2] == "rock":
            rp(f"{trade_list[2]} - 1 Gold", 0.5)
        elif trade_list[2] == "plank":
            rp(f"{trade_list[2]} - 2 Gold", 0.5)
        if len(trade_list) >= 4 :
            rp(f"{trade_list[3]} - 20 Gold", 0.5)
        print()
        item_chosen = cfl(trade_list, "Choose An Item (Type 'BACK' To Leave)", village)
        if item_chosen != "back":
            if item_chosen == "bread" or item_chosen == "plank":
                if gold >= 2:
                    inventory.append(item_chosen)
                    rp(f"{item_chosen} Added To Inventory", 1)
                    gold -= 2
                else:
                    rp("Not Enough Gold")
            elif item_chosen == "berries" or item_chosen == "sweets" or item_chosen == "stick" or item_chosen == "rock":
                if gold >= 1:
                    inventory.append(item_chosen)
                    rp(f"{item_chosen} Added To Inventory", 1)
                    gold -= 1
                else:
                    rp("Not Enough Gold")                    
            elif item_chosen == "soup":
                if gold >= 3:
                    inventory.append(item_chosen)
                    rp(f"{item_chosen} Added To Inventory", 1)
                    gold -= 3
                else:
                    rp("Not Enough Gold")            
            elif item_chosen == "spear":
                if gold >= 2:
                    weapon_available.append("spear")
                    rp(f"{item_chosen} Added To Available Weapons", 1)
                    gold -= 2
                else:
                    rp("Not Enough Gold")
            elif item_chosen == "mace":
                if gold >= 3:
                    weapon_available.append("mace")
                    rp(f"{item_chosen} Added To Available Weapons", 1)
                    gold -= 3
                else:
                    rp("Not Enough Gold")                
            elif item_chosen == "frozen_arrow":
                if gold >= 5:
                    arrow_available.append("frozen")
                    rp(f"{item_chosen} Added To Available Arrows", 1)
                    gold -= 5  
                else:
                    rp("Not Enough Gold")
            elif item_chosen == "drill_arrow":
                if gold >= 11:
                    arrow_available.append("drill")
                    rp(f"{item_chosen} Added To Available Arrows", 1)
                    gold -= 11     
                else:
                    rp("Not Enough Gold") 
            elif item_chosen == "archer":
                if gold >= 20:
                    class_available.append("archer")
                    rp(f"{item_chosen} Added To Available Arrows", 1)
                    gold -= 20
                else:
                    rp("Not Enough Gold")
            rp(f"You Now Have {gold} Gold", 1, True)
        else:
            rp("Returning To Village", 1, True)  
    return
            

def work():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global splash_range, splash_damage, piercing
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    work_ = r.choice(["chop", "forage", "hunt"])
    if work_ == "chop":
        chopped = 0
        rp(f"You Are Going To Chop 30 Logs. You Need 20 To Suceed")
        for count in range(1, 30 + 1):
            strength = countspam(7, "random", "Charge The Swing Of The Axe")
            rp("Wait", r.choice([3, 4, 5, 6, 7, 8]))
            chop = quick_time_event(1, "random", "Chop Now")
            if strength >= 30 and chop == True:
                rp("You Successfully Chopped Through The Log", 1)
                chopped += 1
            elif strength < 30 and chop == True:
                rp("You Hit The Log But It Didn't Cut Through", 1, True)
            elif strength >= 30 and chop == False:
                rp("Your Swing Was Strong But You Missed The Log", 1, True)
            elif strength < 30 and chop == False:
                rp("Your Swing Was Bad And You Missed The Log", 1)
                health -= 1
                rp("Your Bad Technique Cost You 1 Health", 1, True)
        if chopped >= 20:
            rp(f"Well Done You Did The Job", 1)
            gold += 10
            rp(f"You Got 10 Gold. You Are Now On {gold} Gold", 1, True)
        else:
            rp(f"You Failed The Job", 1, True)
    if work_ == "forage":  
            rp("You Are Forageing For Mushrooms", 1)
            rp("You Are Going To Pick 30 Mushroom. 20 Must Be Safe", 1, True)
            rp("Key:", 0.5)
            rp("Spotty: Poisonous If Paired With Another Poisonous Trait", 1)
            rp("Streaky: Completely Safe To Eat", 1)
            rp("Tiger Patturn: Completely Posionous", 1)
            rp("No Patturns: No Correlation To Posion", 1)
            rp("Red: Poisonous If Paired With Another Poisonous Trait", 1)
            rp("Brown: Safe Unless Paried With A Completly Posionous Trait", 1)
            rp("White: No Correlation", 1)
            mushrooms = ["Spotty Red", "Spotty Brown", "Spotty White", "Streaky Red", "Streaky Brown", "Streaky White", "Tiger Stripes Red"]
            poisionous = ["Spotty Red", "Tiger Stripes Red", "Tiger Stripes Brown", "Tiger Stripes White",]
            safe = ["Spotty Brown", "Spotty White", "Streaky Red", "Streaky Brown", "Streaky White", "Patturnless Red", "Patturnless Brown", "Patturnless White"]
            total_mushrooms_picked = 0
            safe_mushrooms_picked = 0
            poisionous_muchrooms_picked = 0
            mushrooms_failed = 0
            for count in range(1, 30 + 1):
                correct_option = r.choice(["option 1", "option 2"])
                if correct_option == "option 1":
                    option_1 = r.choice(safe)
                    option_2 = r.choice(poisionous)
                elif correct_option == "option 2":
                    option_1 = r.choice(poisionous)
                    option_2 = r.choice(safe)
                forage = quick_time_choice(5, "random", "random", f"Forage A {option_1}", f"Forage A {option_2}")
                if forage == "Option 1":
                    total_mushrooms_picked += 1
                    if option_1 in safe:
                        safe_mushrooms_picked += 1
                        rp("You Picked A Safe Mushroom", 1)
                    elif option_1 in poisionous:
                        poisionous_muchrooms_picked += 1
                        rp("You Picked A Poisionous Mushroom", 1)
                elif forage == "Option 2":
                    total_mushrooms_picked += 1
                    if option_2 in safe:
                        safe_mushrooms_picked += 1
                        rp("You A Picked A Safe Mushroom", 1)
                    elif option_2 in poisionous:
                        poisionous_muchrooms_picked += 1
                        rp("You Picked A Posionous Mushroom", 1)
                elif forage == False:
                    mushrooms_failed += 1
                    rp("You Failed To Choose A Mushroom", 1)
                print()
            rp(f"You Picked {total_mushrooms_picked} Mushrooms", 1)
            rp(f"{safe_mushrooms_picked} Of Which Were Safe", 1)
            rp(f"And {poisionous_muchrooms_picked} Were Posisionous", 1)
            rp(f"You Failed To Pick Up {mushrooms_failed} Mushrooms", 1, True)
            if safe_mushrooms_picked >= 20:
                rp(f"Well Done You Did The Job", 1)
                gold += 10
                rp(f"You Got 10 Gold. You Are Now On {gold} Gold", 1, True)
            else:\
                rp(f"You Failed The Job", 1, True)
    elif work_ == "hunt":
        rp("You Are Hunting Animals", 1)
        rp("You Are Going To Get 10 Dead Animal Back")
        animals = 0
        for count in range(1, 10 + 1):
            animal = r.choice("Cow", "Sheep", "Rabbit")
            if animal == "Cow":
                animal_health = 5
            elif animal == "Sheep":
                animal_health = 4
            elif animal == "Rabbit":
                animal_health = 2
            rp(f"You Encounter A {animal}. It Has {animal_health} Health", 1)
            while animal_health > 0:
                attack = waitandhit("random", "random", f"Attack The {animal}")
                if attack == True:
                    animal_health -= damage
                    if animal_health <= 0:
                        animal_health = 0
                    rp(f"You Did {damage} Damage. The {animal} Now Has {animal_health} Health Left", 1)
                else:
                    rp(f"You Missed Your Attack On The {animal}", 1)
            rp(f"You Defeated The {animal}", 1)
            if animal == "Cow":
                rp("Cow Carcuss Added To Villager Meats", 1)
                animals += 1
            elif animal == "Sheep":
                rp("Sheep Carcuss Added To Villager Meats", 1)
                animals += 1
            elif animal == "Rabbit":
                rp("Rabbit Carcuss Added To Villager Meats", 1)
                animals += 1
        if animals >= 10:
            rp(f"Well Done You Did The Job", 1)
            gold += 10
            rp(f"You Got 10 Gold. You Are Now On {gold} Gold", 1, True)
        else:
            rp(f"You Failed The Job", 1, True)
    return

def heal():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global splash_range, splash_damage, piercing
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    pay = ci("Pay 15 Gold To Heal. 'YES'/'NO'", village, "YES", "NO")
    if pay == "option_1":
        if gold >= 15:
            gold -= 15
            health = 30
            energy = 30
            rp(f"You Spent 15 Gold. You Have {gold} Gold", 1)
            if cursed == True:
                cursed = False
                rp(f"Health At {health}, Energy At {energy} And Cursed Unapplied", 1)
            else:
                rp(f"Health At {health} And Energy At {energy}", 1)
        else: 
            rp("Not Enough Gold", 1, True)
    rp("Returning To Village", 1, True)
    return

def massacre():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global splash_range, splash_damage, piercing
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done
    rp("Not Availble Yet.", 1)
    overcome = quick_time_spam(5, "random", 50, "Overcome Your Goodwill")
    if overcome == False:
        rp("Your Too Good To Do This", 1)
        return
    else:
        rp("You Start Too") 
    
def temp():
    global health, energy, damage, inventory, gold
    global armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global armour_affects
    global event_speed, energy_efficenty, damage_resistence
    global crit_chance, crit_attack, crit_multiplier
    global splash_range, splash_damage, piercing
    global damage_affects, energy_timer, cursed
    global class_, spell, weapon, arrow, skill
    global class_available, spell_available, weapon_available, arrow_available, skill_available
    global companion, companion_available
    global game_started, beach_discovered, field_discovered, field_discovered2
    global forest_discovered, overhang_discovered, village_discovered
    global village_first_job, forest_monster_killed, monster_responce
    global village_purged, village_chest, last_checkpoint, save_dir
    global beach_fishing_loot, beach_dig_loot, beach_wander_loot
    global weather_chance, thunderstrike_chance, warmth, in_shelter
    global last_weather_effect_refesh, last_weather_change_refesh, weather_change_addtitional_time
    global neg2_weather, last_weather, this_weather, next_weather
    global tutorial_done, text_tutorial_chest, text_tutorial_back, text_tutorial_forward, text_tutorial_done
    global fight_tutorial_dodge, fight_tutorial_attack, fight_tutorial_crit, fight_tutorial_done
    global menu_tutorial_save, menu_tutorial_basic, menu_tutorial_access, menu_tutorial_done

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

cursed = False
monster_responce = False
village_purged = False
village_chest = False

#pet
companion = "none"
companion_available = []

#discovered areas
game_started = False
beach_discovered = False
field_discovered = False
field_discovered2 = False
forest_discovered = False
overhang_discovered = False
village_discovered = False
village_first_job = False
forest_monster_killed = False
mountain_discovered = False
moutain_door = False

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

splash_range = 0
splash_damage = 0
piercing = 0

neg2_weather = "cloudy"
last_weather = "cloudy"
this_weather = "cloudy"
new_weather = "cloudy"

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

if o.path.exists(save_dir):
    load_save()
    
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
        if __name__ == "__main__":
            tutorial()
    else:
        print("Welcome")
        t.sleep(1)
        load_save()
        t.sleep(1)
        print("Returning To Beach")
        t.sleep(1)
        print()
        beach()
else:
      print("LEARN TO SPELL")