import time as t
import os as o
import random as r
import keyboard as k
import json as j

start_load = t.time() #records time at start of loading to see how long it takes to load

game_dir = o.path.dirname(o.path.abspath(__file__))
save_name = "save_file.json"      #Retrives Path For Save File
save_dir = f"{game_dir}/{save_name}"

def save_data(next_location):
    global health, energy, gold, inventory, armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global companion, companion_available, class_, weapon, spell, arrow, skill
    global class_available, weapon_available, spell_available, arrow_available, skill_available
    global neg2_weather, last_weather, this_weather, next_weather
    global last_weather_change_refesh, last_weather_effect_refesh
    global beach_discovered, field_discovered, forest_discovered, overhang_discovered
    global tutorial_done, save_dir
    '''Retrives Character Data And Updates The Save Data With It
    Is A Silent Task
    Returns To The Specified Location Or Menu

    >>> save_data(menu)
    Would Save Data Silently And Return To The Menu
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
        "next_weather": next_weather,
        "last_weather_refresh_time": last_weather_change_refesh,
        "last_weather_effect_time": last_weather_effect_refesh,
        "class_available": class_available,
        "weapon_available": weapon_available,
        "spell_available": spell_available,
        "arrow_available": arrow_available,
        "skill_available": skill_available,
        "beach_discovered": beach_discovered,
        "field_discovered": field_discovered,
        "forest_discovered": forest_discovered,
        "overhang_discovered": overhang_discovered,
        "tutorial_done": tutorial_done
    }
    with open(save_dir, "w") as a:
        j.dump(data, a)
    next_location()

def load_save():
    global health, energy, gold, inventory, armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global companion, companion_available, class_, weapon, spell, arrow, skill
    global class_available, weapon_available, spell_available, arrow_available, skill_available
    global neg2_weather, last_weather, this_weather, next_weather
    global last_weather_change_refesh, last_weather_effect_refesh
    global beach_discovered, field_discovered, forest_discovered, overhang_discovered
    global tutorial_done, save_dir
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
    beach_discovered = data.get("beach_discovered", False)
    field_discovered = data.get("field_discovered", False)
    forest_discovered = data.get("forest_discovered", False)
    overhang_discovered = data.get("overhang_discovered", False)
    tutorial_done = data.get("tutorial_done", False)
    return data

def quick_time_event(time_allowed, prompt_key, keyword):
    global event_speed
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
    global event_speed
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
    global event_speed
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
    global event_speed
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
        return True
    else:
        print(f"You Hit '{prompt_key}' {key_pressed} Times")
        return False

def fight_signal():
    global class_
    global weapon
    '''Prints A Statement To Signal A Fight
    Takes Class and Weapon And Changes It Accordingly'''
    if class_ == "fighter" and not weapon == "none":
        print("You Raise You Weapon A Fight")
    elif ( class_ == "fighter" and weapon == "none" ) or class_ == "brawler":
        print("You Clench You Fists For A Fight")
    elif class_ == "wizard":
        print("You Start Chanting Battle Preperation Spells")
    elif class_ == "archer":
        print("You Load An Arrow Into Your Bow")
    else:
        print("You Prepare For A Fight")

def weather_change():
    '''Takes Current Weather And Changes Weather Based On It
    Weather Can Change, Advance, Devance Or Stay The Same
    Some Weathers Can Advance Into Extereme Weathers'''
    heatwave_activate = False
    thunder_activate = False
    hail_activate = False
    fog_activate = False
    weather_effect_done = False
    if this_weather == "sunny" and last_weather == "sunny" and neg2_weather == "sunny":
        heatwave_activate = r.choices(
            [True, False],
            weights = [100, heatwave_chance * 5],
            k = 1
        )
    elif this_weather == "sunny" and last_weather == "sunny":
        heatwave_activate = r.choices(
            [True, False],
            weights = [100, heatwave_chance * 2],
            k = 1
        )
    elif this_weather == "sunny":
        heatwave_activate = r.choices(
            [True, False],
            weights = [100, heatwave_chance],
            k = 1
        )
    else:
        heatwave_activate = False
    if this_weather == "raining" and last_weather == "raining" and neg2_weather == "raining":
        thunder_activate = r.choices(
            [True, False],
            weights = [100, thunderstorm_chance * 5],
            k = 1
        )
    elif this_weather == "raining" and last_weather == "raining":
        thunder_activate = r.choices(
            [True, False],
            weights = [100, thunderstorm_chance * 2],
            k = 1
        )
    elif this_weather == "raining":
        thunder_activate = r.choices(
            [True, False],
            weights = [100, thunderstorm_chance],
            k = 1
        )
    else:
        thunder_activate = False
    if this_weather == "snowing" and last_weather == "snowing" and neg2_weather == "snowing":
        thunder_activate = r.choices(
            [True, False],
            weights = [100, hailstone_storm_chance * 5],
            k = 1
        )
    elif this_weather == "snowing" and last_weather == "snowing":
        thunder_activate = r.choices(
            [True, False],
            weights = [100, hailstone_storm_chance * 2],
            k = 1
        )
    elif this_weather == "snowing":
        hail_activate = r.choices(
            [True, False],
            weights = [100, hailstone_storm_chance],
            k = 1
        )
    else:
        hail_activate = False
    if this_weather == "cloudy" and last_weather == "cloudy" and neg2_weather == "cloudy":
        fog_activate = r.choices(
            [True, False],
            weights = [100, hailstone_storm_chance * 5],
            k = 1
        )
    elif this_weather == "cloudy" and last_weather == "cloudy":
        fog_activate = r.choices(
            [True, False],
            weights = [100, fog_chance * 2],
            k = 1
        )
    elif this_weather == "cloudy":
        fog_activate = r.choices(
            [True, False],
            weights = [100, fog_chance],
            k = 1
        )
    else:
        fog_activate = False
    if this_weather == "foggy" or this_weather == "heatwave" or this_weather == "hail_storm" or this_weather == "thundering":
        new_weather_decide = r.choices(
            ["new", "same", "calm"],
            weights = [5, 80, 15]
        )    
    new_weather_decide = r.choices(
        ["new", "same", "increase", "decrease"],
        weights = [15, 15, 35, 35]
    )
    if new_weather_decide == "new":
        new_weather = r.choice[weather_chance]
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
        elif this_weather == "foggy":
            new_weather = "cloudy"
        elif this_weather == "hail_storm":
            new_weather = "snowing"
        elif this_weather == "heatwave":
            new_weather = "sunny"
    neg2_weather = last_weather
    last_weather = this_weather
    if heatwave_activate == True:
        this_weather = "heatwave"
    elif thunder_activate == True:
        this_weather = "thundering"
    elif hail_activate == True:
        this_weather = "hail_storm"
    elif fog_activate == True:
        this_weather = "foggy"
    else:
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
    damage_affects.pop(damage_affects)
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
    armour_affects.pop(armour_affects)
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
            armour_affects.pop("shining_glamour")
            armour_affects.append("shining_strength")
        else:
            armour_affects.append("shining_glamour")

def refresh_armour_lining():
    if armour_lining == "none":
        t.sleep(0)
    elif armour_lining == "ice_thread":
        if "freezing_aura" in armour_affects:
            armour_affects.pop("freezing_aura")
            armour_affects.append("freezing_gaze")
        else:
            armour_affects.append("freezing_aura")
    elif armour_lining == "fire_thread":
        if "burning_aura" in armour_affects:
             armour_affects.pop("burning_aura")
             armour_affects.append("burning_roar")
        else:
            armour_affects.append("burning_aura")
    elif armour_lining == "conductive_thread":
        if "shocking_aura" in armour_affects:
            armour_affects.pop("shocking_aura")
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
    if companion == "parrot":
        damage *= 2
    elif companion == "rock_dweller":
        damage_resistence += 3

def weather_effect_refresh():
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
        

def refresh_all():
    if last_weather_change_refesh + weather_change_addtitional_time < t.time():
        weather_change()
        weather_change_addtitional_time = r.choice[300, 360, 420, 480, 540, 600]
    refresh_class()
    refresh_armour_base()
    refresh_armour_lining()
    refresh_armour_plating()
    refresh_companion()
    weather_effect_refresh()
    save_data()

def menu_home(previous_location_function):
    infinte_time = 100
    print("Menu:")
    t.sleep(0.5)
    print("Press 'a' For Basic Information Like Health and Inventory")
    t.sleep(0.5)
    print("Press 'b' For Your Armour Information")
    t.sleep(0.5)
    print("Press 'c' For Your Class, Weapon And Companion")
    t.sleep(0.5)
    print("Press 'd' For Current Weather Effects")
    t.sleep(0.5)
    print("Or Press 'e' To Go Back")
    t.sleep(1)
    print()
    while infinte_time == 100:
        if k.is_pressed("a"):
            menu_basic(previous_location_function)
        elif k.is_pressed("b"):
            menu_armour(previous_location_function)
        if k.is_pressed("c"):
            menu_class(previous_location_function)
        elif k.is_pressed("d"):
            menu_weather(previous_location_function)
        elif k.is_pressed("e"):
            previous_location_function()

def menu_basic(previous_location_function):
    print("Basic Information:")
    t.sleep(0.5)
    print(f"Health: {health}")
    t.sleep(0.5)
    print(f"Energy: {energy}")
    t.sleep(0.5)
    print(f"Gold: {gold}")
    t.sleep(0.5)
    print(f"Inventory: {inventory}")
    t.sleep(0.5)
    print()
    menu_home(previous_location_function)

def menu_armour(previous_location_function):
    print("Armour Information:")
    t.sleep(0.5)
    print(f"Armour Base: {armour_base}")
    t.sleep(0.5)
    print(f"Armour Plating: {armour_plate}")
    t.sleep(0.5)
    print(f"Armour Lining: {armour_lining}")
    print()
    t.sleep(1)
    print("Would You Like To Change Your Armour 'BASE', 'PLATING', 'LINING' Or 'EXIT'")
    armour_change = str(input())
    if armour_change == "BASE":
        print(f"You Have {armour_base_available} Armour Bases Available")
        t.sleep(1)
        print("To Select An Armour Please Type It How It Shown Above Else Type 'EXIT'")
        select_armour_base = str(input())
        print()
        t.sleep(1)
        if select_armour_base in armour_base_available:
            armour_base_available.append(armour_base)
            armour_base = select_armour_base
            armour_base_available.pop(select_armour_base)
            print(f"{select_armour_base} Has Been Applied")
            t.sleep(1)
            print()
            menu_armour(previous_location_function)
        else:
            menu_armour(previous_location_function)
    if armour_change == "PLATING":
        print(f"You Have {armour_plate_available} Armour Platings Available")
        t.sleep(1)
        print("To Select An Armour Please Type It How It Shown Above Else Type 'EXIT'")
        select_armour_plate = str(input())
        print()
        t.sleep(1)
        if select_armour_plate in armour_plate_available:
            armour_plate_available.append(armour_plate)
            armour_plate = select_armour_plate
            armour_plate_available.pop(select_armour_plate)
            print(f"{select_armour_plate} Has Been Applied")
            t.sleep(1)
            print()
            menu_armour(previous_location_function)
        else:
            menu_armour(previous_location_function)
    if armour_change == "BASE":
        print(f"You Have {armour_lining_available} Armour Bases Available")
        t.sleep(1)
        print("To Select An Armour Please Type It How It Shown Above Else Type 'EXIT'")
        select_armour_lining = str(input())
        print()
        t.sleep(1)
        if select_armour_lining in armour_lining_available:
            armour_lining_available.append(armour_lining)
            armour_lining = select_armour_lining
            armour_lining_available.pop(select_armour_lining)
            print(f"{select_armour_lining} Has Been Applied")
            t.sleep(1)
            print()
            menu_armour(previous_location_function)
        else:
            menu_armour(previous_location_function)
    else:
        print(menu_home(previous_location_function))

def menu_class(previous_location_function):
    if class_ == "wizard":
        print("You Are A Wizard")
        t.sleep(1)
        print("You Fight With Spells")
        t.sleep(1)
        if spell == "fireball":
            print("Your Selected Spell Is Fireball")
        elif spell == "iceball":
            print("Your Selected Spell Is Iceball")
        elif spell == "time_freeze":
            print("Your Selected Spell Is Time Freeze")
        elif spell == "bludgeon":
            print("Your Selected Spell If Bludgeon")
        elif spell == "electric":
            print("Your Selected Spell Is Electric")
        elif spell == "poison":
            print("Your Selected Spell If Poison")
        t.sleep(1)
    elif class_ == "fighter":
        print("You Are A Fighter")
        t.sleep(1)
        print("You Fight With Unique Weapons")
        t.sleep(1)
        if weapon == "none":
            print("Your Selected Weapon Is Your Fists")
        elif spell == "sword":
            print("Your Selected Weapon Is A Sword")
        elif spell == "spear":
            print("Your Selected Weapon Is A Spear")
        elif spell == "dagger":
            print("Your Selected Weapon Is A Dagger")
        elif spell == "mace":
            print("Your Selected Weapon Is A Mace")
        elif spell == "nunchuncks":
            print("Your Selected Weapon Is Nunchuncks")
        t.sleep(1)  
    elif class_ == "brawler":
        print("You Are A Brawler")
        t.sleep(1)
        print("You Fight With Unique Moves")
        t.sleep(1)
        if arrow == "none":
            print("Your Selected Move Is A Basic Punch")
        elif arrow == "fly_kick":
            print("Your Selected Arrow Is A Flying Kick")
        elif arrow == "1inch_punch":
            print("Your Selected Arrow Is The One Inch Punch")
        elif arrow == "flurry_punch":
            print("Your Selected Arrow Is A Flurry Of Punches")
        elif arrow == "flip_kick":
            print("Your Selected Arrow Is A Flip Kick")
        elif arrow == "sweep_kick":
            print("Your Selected Arrow Is A Sweeping Kick")
        t.sleep(1)
    elif class_ == "archer":
        print("You Are An Archer")
        t.sleep(1)
        print("You Fight With Unique Arrows")
        t.sleep(1)
        if arrow == "none":
            print("Your Selected Arrow Is A Basic Tip")
        elif arrow == "poison":
            print("Your Selected Arrow Is A Poison Tip")
        elif arrow == "flame":
            print("Your Selected Arrow Is A Flaming Arrow")
        elif arrow == "frozen":
            print("Your Selected Arrow Is A Freezing Tip")
        elif arrow == "conductor":
            print("Your Selected Arrow Is A Conductive Tip")
        elif arrow == "drill":
            print("Your Selected Arrow Is A Drill Tip")
        t.sleep(1)
    print("To Change Class Type 'CLASS' or Spell Type 'SPELL' Otherwise Type 'BACK'")
    class_choice = str(input())
    print()
    t.sleep(1)
    if class_choice == "CLASS":
        menu_class_change(previous_location_function)
    elif class_choice == "SPELL":
        menu_class_weapon_change(previous_location_function)
   
def menu_class_change(previous_location_function):
    print(f"You Are Currently A {class_}")
    t.sleep(1)
    if len(class_available) == 0:
        print("You Have No Available Classes To Change Too")
        t.sleep(1)
        print("Going Back")
        t.sleep(1)
        print()
        menu_class(previous_location_function)
    else:
        print(f"You Can Change Into: {class_available}")
        t.sleep(1)
        print("To Change Class Type It As Seen Above")
        change_class = str(input())
        print()
        t.sleep(1)
        if change_class in class_available:
            class_available.append(class_)
            class_ = change_class
            class_available.pop(change_class)
            print(f"You Are Now A {class_}")
            t.sleep(1)
            print("Going Back")
            t.sleep(1)
            print()
            menu_class(previous_location_function)
        else:
            print("That Wasn't An Option")
            t.sleep(1)
            print("Going Back")
            t.sleep(1)
            print()
            menu_class(previous_location_function)
           
def menu_class_weapon_change(previous_location_function):
    if class_ == "wizard":
        if len(spell_available) == 0:
            print("You Have No Available Spells")
            t.sleep(1)
            print("Going Back")
            t.sleep(1)
            print()
            menu_class(previous_location_function)
        else:
            print(f"You Can Change To: {spell_available}")
            t.sleep(1)
            print("To Change Spell Type It As Seen Above")
            change_skill = str(input())
            print()
            t.sleep(1)
            if change_skill in spell_available:
                spell_available.append(class_)
                spell = change_skill
                spell_available.pop(change_skill)
                print(f"You Are Now Use {spell}")
                t.sleep(1)
                print("Going Back")
                t.sleep(1)
                print()
                menu_class(previous_location_function)
            else:
                print("That Wasn't An Option")
                t.sleep(1)
                print("Going Back")
                t.sleep(1)
                print()
            menu_class(previous_location_function)
    if class_ == "fighter":
        if len(weapon_available) == 0:
            print("You Have No Available Weapons")
            t.sleep(1)
            print("Going Back")
            t.sleep(1)
            print()
            menu_class(previous_location_function)
        else:
            print(f"You Can Change To: {weapon_available}")
            t.sleep(1)
            print("To Change Weapon Type It As Seen Above")
            change_skill = str(input())
            print()
            t.sleep(1)
            if change_skill in weapon_available:
                weapon_available.append(class_)
                weapon = change_skill
                weapon_available.pop(change_skill)
                print(f"You Are Now Use {weapon}")
                t.sleep(1)
                print("Going Back")
                t.sleep(1)
                print()
                menu_class(previous_location_function)
            else:
                print("That Wasn't An Option")
                t.sleep(1)
                print("Going Back")
                t.sleep(1)
                print()
            menu_class(previous_location_function)
    if class_ == "archer":
        if len(arrow_available) == 0:
            print("You Have No Available Arrows")
            t.sleep(1)
            print("Going Back")
            t.sleep(1)
            print()
            menu_class(previous_location_function)
        else:
            print(f"You Can Change To: {arrow_available}")
            t.sleep(1)
            print("To Change Arrow Type It As Seen Above")
            change_skill = str(input())
            print()
            t.sleep(1)
            if change_skill in arrow_available:
                arrow_available.append(class_)
                arrow = change_skill
                arrow_available.pop(change_skill)
                print(f"You Are Now Use {arrow}")
                t.sleep(1)
                print("Going Back")
                t.sleep(1)
                print()
                menu_class(previous_location_function)
            else:
                print("That Wasn't An Option")
                t.sleep(1)
                print("Going Back")
                t.sleep(1)
                print()
            menu_class(previous_location_function)
    if class_ == "brawler":
        if len(weapon_available) == 0:
            print("You Have No Available Moves")
            t.sleep(1)
            print("Going Back")
            t.sleep(1)
            print()
            menu_class(previous_location_function)
        else:
            print(f"You Can Change To: {skill_available}")
            t.sleep(1)
            print("To Change Weapon Type It As Seen Above")
            change_skill = str(input())
            print()
            t.sleep(1)
            if change_skill in skill_available:
                skill_available.append(class_)
                skill = change_skill
                skill_available.pop(change_skill)
                print(f"You Are Now Use {skill}")
                t.sleep(1)
                print("Going Back")
                t.sleep(1)
                print()
                menu_class(previous_location_function)
            else:
                print("That Wasn't An Option")
                t.sleep(1)
                print("Going Back")
                t.sleep(1)
                print()
            menu_class(previous_location_function)

def menu_weather(previous_location):
    print(f"Its {this_weather}")

def tutorial():
    if tutorial_done == True:
        print("Tutorial Done")
        t.sleep(1)
        print("Starting Game")
        print()
        t.sleep(1)
        beach()
    else:
        if menu_tutorial == True:
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
            print("They Are One Dash Away From Enemies But Their Weapons Can Do Great Damage")
            t.sleep(2)
            print("There Is Also Wizard Where You Collect Spell Book Pages")
            t.sleep(2)
            print("To Use Them Against Your Enemies Like Frost or Fire Ball")
            t.sleep(2)
            print("You Can Level Up These Classes And Find New Items For Them By Playing Them")
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
        elif fight_tutorial == True:
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
            print("")
            beach()
        elif text_tutorial == True:
            print("Now You Know How To Navigate The Game")
            t.sleep(1)
            print("You Need To Know How To Fight")
            t.sleep(1)
            print("Fights Are Turned Based And It's Random Who Turn It Is")
            t.sleep(1)
            print("The System Is That Between You And The Enemy There Is By Default 1 Dash")
            t.sleep(2)
            print("If You Are Within 1 Dash The Next Attack Can Damage You Or You Can Damage Them")
            t.sleep(2)
            print("Without A Special Power Or Weapon This Is The Default")
            t.sleep(2)
            print("The Fights Are Quick Time Based. A Random Key Will Be Selected For You To Press")
            t.sleep(2)
            print("If You Get To Attack 2 Times In A Row And The First Attack Was Successful")
            t.sleep(2)
            print("Then You Get To Do A Critical Hit By Pressing 2 Keys At The Same Time")
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
    if text_tutorial_back == True and text_tutorial_forward == True and text_tutorial_chest == True:
        print("Well Done You Completed The First Tutorial Section")
        t.sleep(1)
        text_tutorial = True
        print()
        tutorial()
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
        tutorial_text_box_white()
    else:
        print("That's Not An Option")
        t.sleep(1)
        print("Try Again")
        print()
        t.sleep(1)
        tutorial_text_box_white()

def tutorial_text_box_green():

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
        tutorial_text_box_green()
    elif tutorial_room_move == "BROWN":
        print("You Enter The Brown Room")
        t.sleep(1)
        print("An Overwhelming Stench Takes Over You As You Run Back To The Green Room")
        t.sleep(2)
        print()
        tutorial_text_box_green()
    elif tutorial_room_move == "BACK":
        tutorial_text_box_white()
    else:
        print("Well Done")
        t.sleep(1)
        print("You Went Back Without Typing 'BACK'")
        print()
        text_tutorial_back = True
        t.sleep(1)
        tutorial_text_box_white()  

def tutorial_text_box_red():

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
        tutorial_text_box_red()
    elif tutorial_room_move == "ORANGE":
        print("You Enter The Orange Room")
        t.sleep(1)
        print("The Room Is Filled With Oranges")
        t.sleep(1)
        print("Unfortunatly You Are Deadly Allergic To Oranges So You Go Back")
        t.sleep(2)
        print(1)
        tutorial_text_box_red()
    elif tutorial_room_move == "BACK":
        tutorial_text_box_white()
    else:
        print("Well Done")
        t.sleep(1)
        print("You Went Back Without Typing 'BACK'")
        print()
        text_tutorial_back = True
        t.sleep(1)
        tutorial_text_box_white()  
   
def tutorial_text_box_blue():
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
        tutorial_text_box_blue()
    elif tutorial_room_move == "LILAC":
        print("You Enter The Lilac Room")
        t.sleep(1)
        print("The Air Smells Of A Scent Of Flowers")
        t.sleep(1)
        print("The Air Was So Good You Fell Asleep And Found Yourself Back In The Blue Room")
        t.sleep(2)
        print(1)
        tutorial_text_box_blue()
    elif tutorial_room_move == "BACK":
        tutorial_text_box_white()
    else:
        print("Well Done")
        t.sleep(1)
        print("You Went Back Without Typing 'BACK'")
        print()
        text_tutorial_back = True
        t.sleep(1)
        tutorial_text_box_white()  

def fight_tutorial():
    white_box_health = 5
    print(f"You Are Fighing A Mystical White Box Which Has {white_box_health} Health")
    crit_attack = False
    print()
    t.sleep(1)
    while white_box_health > 0:
        if health <= 0:
            print("Try Again")
            health = 30
            fight_tutorial()
        t.sleep(1)
        if fight_tutorial_attack == True and fight_tutorial_dodge == True and fight_tutorial_crit == True:
            print("Well Done")
            t.sleep(1)
            print("You Have Completed The Fight Tutorial")
            fight_tutorial_done = True
            crit_attack = False
            print()
            t.sleep(1)
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
                if quick_time_event(3, "random", "Attack the Baby Dragon") == True:
                    t.sleep(0.5)
                    white_box_health_taken = 1 * damage
                    white_box_health -= white_box_health_taken
                    print(f"You Attacked the Baby Dragon For {white_box_health_taken} Damage. It Now Has {white_box_health} Health Left")
                    crit_attack = True
                else:
                    print("You Missed Your Attack")
                    crit_attack = False
            tutorial()
    if white_box_health >= 0:
        t.sleep(1)
        print("You Defeated the White Box But Not Complete The Task")
        t.sleep(1)
        print("Restarting")
        crit_attack = False
        print()
        t.sleep(1)
        fight_tutorial()

def beach():
    if beach_discovered == False:
        print("You Wake Up Confused Lying On The Floor")
        t.sleep(1)
        print("Sand Grains Irritate Your Skin And Seep Into Your Clothes")
        t.sleep(1)
        print("Sand, What. You Should Be On A Ship")
        t.sleep(1)
        print("You Stand Up And Realise Your On A Beach")
        t.sleep(1)
        print("You Try To Think Of Why You Are Here")
        t.sleep(1)
        print("But Cannot Remember Anything Else But The Ship")
        t.sleep(1)
        print("With Nothing Else To Do")
        t.sleep(1)
        print("You Start Looking For Resources")
        t.sleep(1)
        print("You Can 'DIG' Or 'WANDER' To Look For Resourses")
        beach_option_1 = str(input())
        print()
        t.sleep(1)
        if beach_option_1 == "WANDER":
            beach_wander()
        elif beach_option_1 == "DIG":
            beach_dig()
        elif beach_option_1 == "BACK":
            ending_1()
        else:
            beach()
    else:
        print("You Are Back On The Beach You Woke Up On")
        t.sleep(1)
        if "fishing_rod" in inventory:
            print("You Can 'WANDER', 'DIG', or 'FISH' Or Travel To The 'FOREST', 'FIELD' Or 'OVERHANG' ")
            beach_option_2 = str(input())
            print()
            t.sleep(1)
            if beach_option_2 == "WANDER":
                beach_wander()
            elif beach_option_2 == "DIG":
                beach_dig()
            elif beach_option_2 == "FISH":
                beach_fish()
            elif beach_option_2 == "FOREST":
                forest()
            elif beach_option_2 == "FIELD":
                field()
            elif beach_option_2 == "OVERHANG":
                overhang()
            else:
                print("Not A Valid Option Try Again")
                t.sleep(1)
                beach()
        else:
            print("You Can 'WANDER' Or 'DIG' Or Travel To The 'FOREST', 'FIELD' Or 'OVERHANG' ")
            beach_option_2 = str(input())
            print()
            t.sleep(1)
            if beach_option_2 == "WANDER":
                beach_wander()
            elif beach_option_2 == "DIG":
                beach_dig()
            elif beach_option_2 == "FOREST":
                forest()
            elif beach_option_2 == "FIELD":
                field()
            elif beach_option_2 == "OVERHANG":
                overhang()
            else:
                print("Not A Valid Option Try Again")
                t.sleep(1)
                beach()

def beach_wander():
    if beach_discovered == False:
        print("You Start Strolling Down The Beach")
        t.sleep(1)
        print("Looking For Resources That Down With The Boat")
        fishing_rod_time = r.choice([6, 7, 8, 9, 10])
        t.sleep(fishing_rod_time)
        print(f"After {fishing_rod_time} Seconds You Find A Fishing Rod")
        inventory.append("fishing_rod")
        energy_lost_beach_wander_fish_rod = 1 * energy_efficenty
        energy -= energy_lost_beach_wander_fish_rod
        t.sleep(1)
        print("This Will Be Handy")
        t.sleep(1)
        print("Fishing Rod Added To Inventory")
        t.sleep(1)
        print(f"You Lost {energy_lost_beach_wander_fish_rod} Energy. You Are Now On {energy}")
        t.sleep(1)
        beach_discovered = True
        game_started = True
        print("Do You Want To Keep Wandering? 'YES'/'NO'")
        beach_wander_option_1 = str(input())
        print()
        t.sleep(1)
        if beach_wander_option_1 == "YES":
            beach_wander()
        else:
            beach()
    else:
        print("You Start Strolling Down The Coast Line")
        pause_time = r.choice([6, 7, 8, 9, 10, 11])
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
        t.sleep(pause_time)
        print(f"After {pause_time} Seconds You Found A {loot_name}")
        t.sleep(1)
        if loot == "plank" or loot == "rock":
            print(f"Do You Want To Keep The {loot_name} 'YES'/'NO'")
            beach_wander_option_1 = str(input())
            t.sleep(1)
            if beach_wander_option_1 == "YES":
                inventory.append(loot)
                print(f"{loot_name} Added To Inventory")
            else:
                print(f"You Left The {loot_name}")
        elif loot == "gold":
            gold_amount = r.choice([1, 2, 3])
            gold += gold_amount
            print(f"{gold_amount} Gold Was Put In Your Gold Pouch. You Are Now On {gold} Gold")
        elif loot == "gold_chest":
            gold_chest_amount = r.choice([30, 35, 40, 45, 50])
            gold += gold_chest_amount
            print(f"{gold_chest_amount} Was Added To Your Gold Pouch. You Are Now On {gold} Gold")
        else:
            print(f"The {loot_name} Wasn't Worth Keeping So You Threw It Away")
        t.sleep(1)
        energy_lost_beach_wander = 1 * energy_efficenty
        energy -= energy_lost_beach_wander
        print(f"You Lost {energy_lost_beach_wander_fish_rod} Energy. You Are Now On {energy}")
        t.sleep(1)
        print("Would You Like To Wander Again")
        beach_wander_option_2 = str(input())
        print()
        t.sleep(1)
        if beach_wander_option_2 == "YES":
            beach_wander()
        else:
            beach()

def beach_dig():
    if beach_discovered == False:
        print("You Start Digging The Sand Beneathe You")
        t.sleep(1)
        print("To Hopefully Find An Item")
        t.sleep(1)
        print("That Will Help You Suvive")
        t.sleep(1)
        print("On This Unknown Land")
        t.sleep(1)
        while not "fishing_rod" in inventory:
            fishing_rod_dig = quick_time_spam(20, "random", "random", "Dig")
            if fishing_rod_dig == True:
                print("You Hit A Solid Wooden Pole")
                t.sleep(1)
                print("It's A Fishing Rod")
                t.sleep(1)
                print("This Will Be Handy")
                t.sleep(1)
                energy_lost_beach_dig_fish_rod = 1 * energy_efficenty
                energy -= energy_lost_beach_dig_fish_rod
                print(f"You Lost {energy_lost_beach_dig_fish_rod} Energy. You Are Now On {energy}")
                t.sleep(1)
                t.sleep(1)
                inventory.append("fishing_rod")
                beach_discovered = True
                game_started = True
                print("Do You Want To Keep Digging? 'YES/'NO'")
                keep_digging_1 = str(input())
                print()
                t.sleep(1)
                if keep_digging_1 == "YES":
                    beach_dig()
                else:
                    beach()

            else:
                print("You Only Ended Up Only Scraping Up A Thin Layer Of Sand Beneathe You")
                t.sleep(1)
                print()
                beach_dig()
    else:
        print("You Start Digging Down Into The Sand")
        pause_time = r.choice([6, 7, 8, 9, 10, 11])
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
            t.sleep(pause_time)
            print(f"You Hit A {loot_name}")
            t.sleep(1)
            if loot == "plank" or loot == "rock" or loot == "bone":
                print(f"Do You Want To Keep The {loot_name} 'YES'/'NO'")
                beach_wander_option_1 = str(input())
                t.sleep(1)
                if beach_wander_option_1 == "YES":
                    inventory.append(loot)
                    print(f"{loot_name} Added To Inventory")
                else:
                    print(f"You Left The {loot_name}")
            elif loot == "gold":
                gold_amount = r.choice([1, 2, 3])
                gold += gold_amount
                print(f"{gold_amount} Gold Was Put In Your Gold Pouch. You Are Now On {gold} Gold")
            elif loot == "gold_chest":
                gold_chest_amount = r.choice([30, 35, 40, 45, 50])
                gold += gold_chest_amount
                print(f"{gold_chest_amount} Was Added To Your Gold Pouch. You Are Now On {gold} Gold")
            elif loot == "rock_dweller":
                print("Do You Want To Set The Rock Dweller As Your Companion.")
                t.sleep(1)
                print("Else It Is Added To Your Inventory 'YES'/'NO'")
                rock_dweller_select = str(input())
                t.sleep(1)
                if rock_dweller_select == "YES":
                    companion = "rock_dweller"
                    companion_health = 20
                    print("Rock Dweller Set As Companion")
                else:
                    companion_available.append("rock_dweller")
                    print("Rock Dweller Added To Inventory")
            else:
                print(f"The {loot_name} Wasn't Worth Keeping So You Threw It Away")
        else:
            print("You Failed To Dig Deep Enough")
    t.sleep(1)
    t.sleep(1)
    energy_lost_beach_dig = 1 * energy_efficenty
    energy -= energy_lost_beach_dig
    print(f"You Lost {energy_lost_beach_dig} Energy. You Are Now On {energy}")
    t.sleep(1)
    print("Would You Like To Dig Again")
    beach_wander_option_2 = str(input())
    print()
    t.sleep(1)
    if beach_wander_option_2 == "YES":
        beach_dig()
    else:
        beach()

def beach_fish():
    if "fishing_rod" in inventory:
        print("You Throw Your Hook Into The Sea")
        pause_time = r.choice([6, 7, 8, 9, 10, 11])
        t.sleep(pause_time)
        print(f"After {pause_time} Seconds Something Hooked Onto Your Fishing Rod")
        t.sleep(1)
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
        print(f"You Fished Up A {loot_name}")
        t.sleep(1)
        if loot == "plank" or loot == "rock" or loot == "bone":
            print(f"Do You Want To Keep The {loot_name} 'YES'/'NO'")
            beach_wander_option_1 = str(input())
            t.sleep(1)
            if beach_wander_option_1 == "YES":
                inventory.append(loot)
                print(f"{loot_name} Added To Inventory")
            else:
                print(f"You Left The {loot_name}")
        elif loot == "gold":
            gold_amount = r.choice([1, 2, 3])
            gold += gold_amount
            print(f"{gold_amount} Gold Was Put In Your Gold Pouch. You Are Now On {gold} Gold")
        elif loot == "gold_chest":
            gold_chest_amount = r.choice([30, 35, 40, 45, 50])
            gold += gold_chest_amount
            print(f"{gold_chest_amount} Was Added To Your Gold Pouch. You Are Now On {gold} Gold")
        elif loot == "fish_scaling":
            print("Do You Want To Set The Fish Scaling As Your Armour Base.")
            t.sleep(1)
            print("Else It Is Added To Your Inventory 'YES'/'NO'")
            rock_dweller_select = str(input())
            t.sleep(1)
            if rock_dweller_select == "YES":
                armour_base = "fish_scaling"
                print("Scale Plating Set As Armour Base")
            else:
                armour_base_available.append("fish_scaling")
                print("Scale Plating Added To Inventory")
        else:
            print(f"The {loot_name} Wasn't Worth Keeping So You Threw It Away")
    else:
            print("You Failed To Pull Up The Loot")
    t.sleep(1)
    energy_lost_beach_fish = 1 * energy_efficenty
    energy -= energy_lost_beach_fish
    print(f"You Lost {energy_lost_beach_fish} Energy. You Are Now On {energy}")
    t.sleep(1)
    print("Would You Like To Fish Again")
    beach_wander_option_2 = str(input())
    print()
    t.sleep(1)
    if beach_wander_option_2 == "YES":
        beach_fish()
    else:
        beach()

def overhang():
    if overhang_discovered == False:
        print("As You Walk Of The Gritty Sand You Find A Small Overhang")
        t.sleep(1)
        print("The Smooth Rock Facing Towards The Calming Sea Would Be A Good Place To Rest")
        t.sleep(1)
        print("To Gain 1 Energy It Takes 2 Minutes Of Rest.")
        t.sleep(1)
        print(" A New Energy Will Start Regain Automatically Once One Is Done")
        overhang_discovered = True
        print()
        overhang()
    else:
        print("You Can Rest Here. 'YES' / 'NO'")
        overhang_choice = str(input())
        t.sleep(1)
        print()
        if overhang_choice == "YES":
            rest()
        else:
            beach()
           
def field():
    if field_discovered == False:
        print("You Step Of The Irritating Sand And Onto The Lucious Grass")
        t.sleep(1)
        print("You Hear The Mooing Of Cows In The Background")
        t.sleep(1)
        print("The Relaxing Peace Is Quickly Broken By A Man")
        t.sleep(1)
        print("This Is The First Human Interaction You Have Had Since The Ship Wreck")
        t.sleep(1)
        print("As You Go To Great The Man A Flaming Fire Ball Skims Past Your Face")
        t.sleep(1)
        print("This Isn't A Man, Its A Wizard And He Isnt Happy")
        t.sleep(1)
        wizard_fight()
    else:
        print()
       
def forest():
        print("")

def ending_1():
      print("After Standing Up And Thinking For A Bit")
      t.sleep(2)
      print("You Realise These Are Horrible Terms To Live With")
      t.sleep(2)
      print("So You Lie Back Down And Fall Back To Sleep")
      t.sleep(2)
      print("Allowing Nature To Take Your Body")
      t.sleep(2)
      print("Ending 1 Unlocked!")
      t.sleep(1)
      print("If I Had A Reward I Would Announce It Here")
      t.sleep(1)
      print()
      beach()

def ending_2():
    print("With All Your Planks Your Start Building A Ship")
    t.sleep(2)
    print("It's How This Journy Started, On The Seas")
    t.sleep(2)
    print("The Mystery Of The Island Or Your Memory Was Never Discovered")
    t.sleep(2)
    print("But You Did Feel The Connection In Pirating")
    t.sleep(2)
    print("Ending 2 Unlocked!")
    t.sleep(2)
    print("You Unlocked The Parrot Companion")
    t.sleep(2)
    print("It Copies Your Attacks So You Do Double Damage")
    t.sleep(2)
    print("Would You Like To Equip It? 'YES' / 'NO'")
    parrot_choice = input()
    print()
    t.sleep(1)
    if parrot_choice == "YES":
        companion_available.append(companion)
        companion = "parrot"
        damage *= 2
        print("Parrot Equipped")
    else:
        companion_available.append("parrot")
        print("Parrot Added To Available Companions")


def wizard_fight():
    print("You Pose For A Fight")
    t.sleep(1)
    wiz_ran = r.choice["attack", "defend"]
    if wiz_ran == "attack":
        crit = r.choices["YES", "NO"]


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
    global fire_resistence
    global water_resistence
    global ice_resistence
    global electrictiy_resistence
    global heat_resistence
    global skip_swim
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
    global game_started
    global save_dir
    global companion
    global companion_health
    global companion_available
    global tutorial_done
    global text_tutorial_chest
    global text_tutorial_back
    global text_tutorial_forward
    global text_tutorial
    global fight_tutorial_dodge
    global fight_tutorial_attack
    global fight_tutorial_crit
    global fight_tutorial_done
    global menu_tutorial_armour
    global menu_tutorial_save
    global menu_tutorial_companion
    global menu_tutorial_class
    global menu_tutorial
    global weather_chance
    global heatwave_chance
    global thunderstorm_chance
    global fog_chance
    global hailstone_storm_chance
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

#pet
companion = "none"
companion_available = []

#discovered areas
game_started = False
beach_discovered = False
field_discovered = False
forest_discovered = False
overhang_discovered = False

#loot tables
beach_fishing_loot = ["fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "fish", "plank", "plank", "plank", "plank", "plank", "plank", "plank",  "plank" "plank", "plank", "plank", "plank", "plank", "plank", "plank", "plank",  "plank" "plank", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "fish_scaling"]
beach_dig_loot = ["rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock","rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "plank", "plank", "plank", "plank" "plank", "plank", "plank", "plank" "plank", "plank", "plank", "plank", "plank", "plank", "plank", "plank", "plank", "plank", "plank", "plank", "plank", "plank", "plank", "plank" "plank", "plank", "plank", "plank", "plank", "plank", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "bone", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "gold", "gold", "gold", "gold_chest", "rock_dweller"]
beach_wander_loot = ["plank", "plank", "plank", "plank" "plank", "plank", "plank", "plank" "plank", "plank", "plank", "plank"  "plank", "plank", "plank", "plank" "plank", "plank", "plank", "plank", "plank", "plank", "plank" "plank", "plank", "plank", "plank" "plank", "plank", "plank", "plank"  "plank", "plank", "plank", "plank" "plank", "plank", "plank", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "rubbish", "gold", "gold", "gold_chest"]

#weather system
weather_chance = ["sunny", "sunny", "sunny", "sunny", "sunny", "sunny", "clear", "clear", "clear", "clear", "clear", "clear", "clear", "clear", "cloudy", "cloudy", "cloudy", "cloudy", "cloudy", "cloudy", "cloudy", "cloudy", "cloudy", "cloudy", "cloudy", "cloudy", "cloudy", "cloudy", "drizzling", "drizzling", "drizzling", "drizzling", "drizzling", "drizzling", "raining", "raining", "raining", "raining", "raining", "raining", "raining", "raining", "snowing", "snowing", "snowing", "snowing", "snowing"]
heatwave_chance = 15
thunderstorm_chance = 10
hailstone_storm_chance = 5
fog_chance = 1

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
text_tutorial = False
fight_tutorial_dodge = False
fight_tutorial_attack  = False
fight_tutorial_crit  = False
fight_tutorial_done = False
menu_tutorial_armour = False
menu_tutorial_save = False
menu_tutorial_companion = False
menu_tutorial_class = False
menu_tutorial = False

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
        save_data("new")
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
        beach()
else:
      print("LEARN TO SPELL")
