def fight_signal():
    global class_
    global weapon
    '''Prints A Statement To Signal A Fight
    Takes Class and Weapon And Changes It Accordingly'''
    if class_ == "fighter" and not weapon == "none":
        rp("You Raise You Weapon A Fight", 1,)
    elif ( class_ == "fighter" and weapon == "none" ) or class_ == "brawler":
        rp("You Clench You Fists For A Fight", 1)
    elif class_ == "wizard":
        rp("You Start Chanting Battle Preperation Spells", 1)
    elif class_ == "archer":
        rp("You Load An Arrow Into Your Bow", 1)
    else:
        rp("You Prepare For A Fight", 1)

def weather_change():
    global last_weather_effect_done, neg2_weather, last_weather, this_weather, next_weather
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
        elif this_weather == "hail_storm":
            new_weather = "snowing"
        elif this_weather == "heatwave":
            new_weather = "sunny"
    neg2_weather = last_weather
    last_weather = this_weather
    if heatwave_activate == True:
        next_weather = "heatwave"
    elif thunder_activate == True:
        next_weather = "thundering"
    elif hail_activate == True:
        next_weather = "hail_storm"
    this_weather = new_weather

def refresh_class():
    global class_, weapon, spell, arrow, skill, crit_chance, piercing
    global splash_damage, splash_range, damage, damage_affects
    '''Checks For Current Value Of 'class_'
    Then Checks For Current Value Of 'weapon', 'spell', 'arrow', Or 'skill'
    Adjusts Stats Accordingly
    '''
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
    global armour_base, damage_resistence, event_speed, armour_affects
    '''Checks For Current Value Of 'armour_base'
    Adjusts Stats Accordingly
    '''
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
    global armour_plate, energy_efficenty, damage_resistence, armour_affects
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
            armour_affects.pop("shining_glamour")
            armour_affects.append("shining_strength")
        else:
            armour_affects.append("shining_glamour")

def refresh_armour_lining():
    global armour_lining, armour_affects, damage, crit_multiplier, crit_chance
    '''Checks For Current Value of 'armour_lining'
    Adjusts Stats Accordingly
    '''
    if armour_lining == "none":
        ...
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
    global companion, damage, damage_resistence
    '''Checks For Current Value Of 'companion'
    Adjusts Stats Accordingly
    '''
    if companion == "parrot":
        damage *= 2
    elif companion == "rock_dweller":
        damage_resistence += 3

def weather_effect_refresh():
    global last_weather_effect_refesh, this_weather, health, warmth
    global in_shelter, damage_resistence, armour_affects, energy_efficenty
    global weather_effect_done, thunderstrike_chance
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

def refresh_all():
    global health, energy, armour_base, armour_plate, armour_lining
    global last_weather_change_refesh, weather_change_addtitional_time
    '''Refreshes All Stats And Values That Need Refreshing
    Health And Energy Are Capped At 30
    If Health Is 0 Or Below The Player Dies And Is Returned To Last Checkpoint
    Weather Change Is Checked And Changed If Needed
    All Refresh Functions Are Called
    Data Is Saved At The End
    '''
    check_stats()
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