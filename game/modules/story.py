import time as t
import os as o
import random as r
import keyboard as k
import json as j 

def beach():
    global beach_discovered, energy, game_started
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
            beach_wander()
        elif beach_option_1 == "option_2":
            beach_dig()
        elif beach_option_1 == "back":
            ending_1()
    else:
        rp("You Are Back On The Beach You Woke Up On", 1)
        last_checkpoint = beach
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
                beach()

def beach_wander():
    global beach_discovered, energy, game_started, gold
    global beach_wander_loot, energy_efficenty, inventory
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
        beach_wander_option_1 = ci("Do You Want To Keep Wandering? 'YES'/'NO'", beach_wander, "YES", "NO")
        if beach_wander_option_1 == "option_1":
            beach_wander()
        else:
            beach()
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
        if beach_wander_option_3 == "option_1":
            beach_wander()
        else:
            beach()

def beach_dig():
    global beach_discovered, energy, game_started, companion
    global beach_dig_loot, energy_efficenty, inventory, companion_available 
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
                keep_digging_1 = ci("Do You Want To Keep Digging? 'YES/'NO'", beach_dig, "YES", "NO")
                if keep_digging_1 == "option_1":
                    beach_dig()
                else:
                    beach()

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
    if beach_dig_option_2 == "option_1":
        beach_dig()
    else:
        beach()

def beach_fish():
    global beach_discovered, energy, game_started, armour_base, armour_base_available, gold
    global beach_fishing_loot, energy_efficenty, inventory
    if "fishing_rod" in inventory:
        pause_time = r.choice([6, 7, 8, 9, 10, 11])
        rp("You Throw Your Hook Into The Sea", pause_time)
        rp(f"After {pause_time} Seconds Something Hooked Onto Your Fishing Rod")
        fish_spam_event = quick_time_spam(10, "random", "random/2", "Pull Up The Fish", 1)
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
    if beach_fish_option_2 == "YES":
        beach_fish()
    else:
        beach()

def overhang():
    if overhang_discovered == False:
        rp("As You Walk Of The Gritty Sand You Find A Small Overhang", 1)
        rp("The Smooth Rock Facing Towards The Calming Sea Would Be A Good Place To Rest", 1)
        rp("To Gain 1 Energy It Takes 2 Minutes Of Rest.", 1) 
        rp("A New Energy Will Start Regain Automatically Once One Is Done", 1, True)
        overhang_discovered = True
        overhang()
    else:
        if energy == 30:
            rp("You Don't Need To Rest", 1)
            rp("You Are At Full Energy", 1, True)
            beach()
        else:
            overhang_choice = ci("You Can Rest Here. 'YES' / 'NO'", overhang, "YES", "NO")
            if overhang_choice == "YES":
                rest()
                beach()
            else:
                beach()
           
def field():
    if field_discovered == False:
        rp("You Step Of The Irritating Sand And Onto The Lucious Grass", 1)
        rp("You Hear The Mooing Of Cows In The Background", 1)
        rp("The Relaxing Peace Is Quickly Broken By A Man", 1)
        rp("This Is The First Human Interaction You Have Had Since The Ship Wreck", 1)
        rp("As You Go To Great The Man A Flaming Fire Ball Skims Past Your Face", 1)
        rp("This Isn't A Man, Its A Wizard And He Isnt Happy", 1, True)
        wizard_fight()
    else:
        print("THIS AREA IS NOT AVAILABLE YET")
        print("RETURNING TO BEACH")
        beach()
       
def forest():
        print("THIS AREA IS NOT AVAILABLE YET")
        print("RETURNING TO BEACH")
        beach()

def ending_1():
      rp("After Standing Up And Thinking For A Bit", 1)
      rp("You Realise These Are Horrible Terms To Live With", 1)
      rp("So You Lie Back Down And Fall Back To Sleep", 1)
      rp("Allowing Nature To Take Your Body", 1)
      rp("Ending 1 Unlocked!", 1)
      rp("You Unlocked The Sleepy Armour Lining", 1)
      rp("It Doubles Your Health & Energy Regenration ", 1)
      ending_1_choice = ci("Would You Like To Equip It? 'YES' / 'NO'", ending_1, "YES", "NO")
      if ending_1_choice == "option_1":
          armour_lining = "sleepy"
          rp("Sleepy Armour Lining Equipped", 1, True)
      else:
          armour_lining_available.append("sleepy")
          rp("Sleepy Armour Lining Added To Available Armour Linings", 1, True)   
      beach()

def ending_2():
    rp("With All Your Planks Your Start Building A Ship", 1)
    rp("It's How This Journy Started, On The Seas", 1)
    rp("The Mystery Of The Island Or Your Memory Was Never Discovered", 1)
    rp("But You Did Feel The Connection In Pirating", 1)
    rp("Ending 2 Unlocked!", 1)
    rp("You Unlocked The Parrot Companion", 1)
    rp("It Copies Your Attacks So You Do Double Damage", 1)
    ending_2_choice = ci("Would You Like To Equip It? 'YES'/'NO'", ending_2, "YES", "NO")
    if ending_2_choice == "YES":
        if companion != "none":
            companion_available.append(companion)
        companion = "parrot"
        rp("Parrot Equipped", 1, True)
    else:
        companion_available.append("parrot")
        rp("Parrot Added To Available Companions", 1)

def wizard_fight():
    fight_signal()
    wiz_ran = r.choice["attack", "defend"]
    while wiz_health > 0 and health > 0:
        if wiz_ran == "attack":
            wiz_crit = r.choices(
                [True, False],
                weights = [crit_chance, 100],
                ) 
            if wiz_crit == True:
                wiz_crit_attack = quick_time_double(5, "random", "random", "Critical Attack The Wizard")
                t.sleep(1)
                if wiz_crit_attack == True:
                    rp("You Landed A Critical Hit On The Wizard", 1)
                    crit_wiz_damage = damage * crit_multiplier
                    wiz_health -= crit_wiz_damage
                    rp(f"You Did {crit_wiz_damage} Damage. The Wizard Now Has {wiz_health} Health Left", 1, True)
                else:
                    rp("You Missed Your Critical Hit On The Wizard", 1, True)
            else:
                wiz_attack = quick_time_event(5, "random", "Attack The Wizard")
                t.sleep(1)
                if wiz_attack == True:
                    rp("You Landed An Attack On The Wizard", 1)
                    wiz_damage = damage
                    wiz_health -= wiz_damage
                    rp(f"You Did {wiz_damage} Damage. The Wizard Now Has {wiz_health} Health Left", 1)
                else:
                    rp("You Missed Your Attack On The Wizard", 1, True)
        else:
            dodge_wiz = quick_time_event(5, "random", "Dodge The Incoming Fireball")
            t.sleep(1)
            if dodge_wiz == True:
                rp("You Dodged The Incoming Fireball", 1, True)
            else:
                rp("You Gazed Into The Flaming Ball Of Fire As It Came Crashing Down On You", 1)
                wiz_health_lost = int ( 2 / damage_resistence )
                health -= wiz_health_lost
                rp(f"You Lost {wiz_health_lost} Damage. You Now Have {health} Health Left", 1, True)
        if wiz_health <= 0:
            print("You Defeated The Wizard")
            t.sleep(1)
            print("Unexpectedly Before His Body Falls To The Ground")
            t.sleep(1)
            print("His Entire Body Fades Away Into Thin Air")
            t.sleep(1)
            print("Leaving Only A Book")
            t.sleep(1)
            print("The Book Contains Spells But Is Missing Many Pages")
            t.sleep(1)
            print("You Have Unlocked The Class Wizard")
            t.sleep(1)
            print("You Have Unlocked The Spell Fireball")
            t.sleep(1)
            print("Would Like To Equip It? 'YES' / 'NO'")
            wiz_activate = str(input())
            print()
            t.sleep(1)
            if wiz_activate == "YES":
                class_ = "wizard"
                spell = "fireball"
                print("Wizard Class Equipped With Fireball Spell")
            else:
                class_available.append("wizard")
                spell_available.append("fireball")
                print("Wizard Class And Fireball Spell Added To Available Classes And Spells")
            t.sleep(1)
            print()
            field_discovered = True
            field()
        if health <= 0:
            print("You Have Been Defeated By The Wizard")
            t.sleep(1)
            print("Returning To Start")
            t.sleep(1)
            health = 30
            energy = 30
            armour_base = "none"
            armour_plate = "none"
            armour_lining = "none"
            print("You Have Reset Your Health, Energy, Inventory And Armour")
            t.sleep(1)
            print()
            beach()

def game_start():
    beach()