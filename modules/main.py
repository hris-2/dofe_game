import time as t
import os as o
import random as r
import keyboard as k
import json as j

start_load = t.time() #records time at start of loading to see how long it takes to load

game_dir = o.path.dirname(o.path.abspath(__file__))
save_name = "save_file.json"      #Retrives Path For Save File
save_dir = f"{game_dir}/{save_name}"

def save_data():
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
    return

def load_save():
    global health, energy, gold, inventory, armour_base, armour_plate, armour_lining
    global armour_base_available, armour_plate_available, armour_lining_available
    global companion, companion_available, class_, weapon, spell, arrow, skill
    global class_available, weapon_available, spell_available, arrow_available, skill_available
    global neg2_weather, last_weather, this_weather, next_weather
    global last_weather_change_refesh, last_weather_effect_refeshsS
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

def check_stats():
    if health >= 30:
        health = 3-
    elif health <= 0:
        print("You Died")
        t.sleep(1)
        print("Resettng, Health, Energy, Weapon, Armour, Totem & Companion")
        t.sleep(1)
        print("You Have Lost The Equipped Items")
        health = 30
        energy = 30
        equipped_weapon = "none"
        armour_base = "none"
        armour_plate = "none"
        armour_lining = "none"
        totem = "none"
        companion = "none"
        checkpoint()
    if energy >= 30:
        energy = 30
    elif energy <=0 :
        if energy_refresh_time + 180 < t.time()
        print("You Have Lost 1 Health To Lack Of Energy")
        t.sleep(1)
        print(f"You Are On {health} Health")
        t.sleep(1)

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

def rp(print: str, wait: int = 0, nl: bool = False) -> None:
    '''Refreshs Everything While Printing
    Optional Wait And Newline Featute
    '''
    refresh_all()
    print(print)
    if wait is not 0:
        t.sleep(wait)
    if nl is True:
        print()
        
def ci(prompt: str = "", this_location = "", option_1: str = "", option_2: str = "", option_3: str = "", option_4: str = "", option_5: str = "", option_6: str = "") -> str:
    rp(prompt)
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