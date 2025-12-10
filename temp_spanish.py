#IMPORTS
import time as t
import random as r
import json as j
import os

#QUESTION SETS

questions = {
    "Quiero ser medico, cuando sea mayor.": "I want to be a docter when I grow up",
    "En el futuro, me gustaria viajar por el mundo.": "In the future, I would like to travel the world",
    "Me no gustaria ser contable porque es muy aburrido": "I wouldn't like to be an accountant because it's very boring",
    "Mi hermano trabaja mecanico y trabaja en un garaje.": "My brother works as a mechanic and works in a garage",
    "Mi madre es enfermera y trabaja en un hospital.": "My mother is a nurse and works in a hospital",
    "Mi profesor no quiero ser profesor porque nostros muy perezosos.": "My teacher doesn't want to be a teacher because we are very lazy",
    "Hola, mi llamo NAME y trabajo recepconista": "Hello, my name is NAME y I work as a recepsonist",
    "En mi trabaja, ayudo los clientos": "In my job, I help customers",
    "En el futuro, quisiera ser abogado": "In the future, I would like to be a lawyer",
    "Mi primo como es jardinero pero no el gusta": "My cousin works as a gardener but he doesn't like it",
    "Odio mi trabaja porque es muy aburrido": "I hate my job because it is very boring",
    "Trabajo dependiente en el tiende de ropa": "I work as a shop assistane in a clothes store",
    "Para ayudar mi comunidad, mi trabaja de sueno es ser policia": "In order to help my community my dream job is to be a police officer",
    "Me encanta mi trabajo porque es no repetivto": ""
    }

spanish_sentaces = []
english_sentaces = []

for spanish in questions.keys():
    spanish_sentaces.append(spanish)
for english in questions.values():
    english_sentaces.append(english)

#BLUEPRINT FOR WEAPONS

class weapons:
    def __init__(self, name, type, damage, affects, rarity, duplicates):
        self.name = name
        self.type = type
        self.damage = damage
        self.affects = affects
        self.rarity = rarity
        self.duplicates = duplicates
    def add_affect(self, affect):
        self.affects.append(affect)
    def add_duplicates(self, number):
        self.duplicates += number
    def refresh_rarity(self, name, rarity, damage):
        if name == "Year 7 Tie":
            if rarity == "common":
                self.damage *= 1
            elif rarity == "uncommon":
                self.damage = int (self.damage * 1.25) 
            elif rarity == "rare":
                self.damage = int (self.damage * 1.5)
        elif name == "Year 8 Tie":
            if rarity == "common":
                self.damage *= 1
            elif rarity == "uncommon":
                self.damage = int (self.damage * 1.25) 
            elif rarity == "rare":
                self.damage = int (self.damage * 1.5)
            elif rarity == "epic":
                self.damage = int (self.damage * 1.75)
        elif name == "Year 9 Tie":
            if rarity == "uncommon":
                self.damage *= 1
            elif rarity == "rare":
                self.damage = int (self.damage * 1.25) 
            elif rarity == "epic":
                self.damage = int (self.damage * 1.5)
            elif rarity == "legendary":
                self.damage = int (self.damage * 1.75)
        elif name == "Year 10 Tie":
            if rarity == "rare":
                self.damage *= 1
            elif rarity == "epic":
                self.damage = int (self.damage * 1.25) 
            elif rarity == "legendary":
                self.damage = int (self.damage * 1.5)
        elif name == "Year 11 Tie":
            if rarity == "epic":
                self.damage *= 1
            elif rarity == "legendary":
                self.damage = int (self.damage * 1.25)  
        elif name == "shank":
            if rarity == "rare":
                self.damage *= 1
            elif rarity == "epic":
                self.damage = int (self.damage * 1.25) 
            elif rarity == "legendary":
                self.damage = int (self.damage * 1.5)
        elif name == "Mr Sargeant's Chair":
            if rarity == "epic":
                self.damage *= 1
            elif rarity == "legendary":
                self.damage = int (self.damage * 1.25)
        elif name == "Wooden Fork":
            if rarity == "common":
                self.damage *= 1
            elif rarity == "uncommon":
                self.damage = int (self.damage * 1.25) 
            elif rarity == "rare":
                self.damage = int (self.damage * 1.5)
        elif name == "Lexie Malkin's Grenade":
            if rarity == "rare":
                self.damage *= 1
            elif rarity == "epic":
                self.damage = int (self.damage * 1.25) 
            elif rarity == "legendary":
                self.damage = int (self.damage * 1.5)
        elif name == "Rory's Glock 19":
            if rarity == "epic":
                self.damage *= 1
            elif rarity == "legendary":
                self.damage = int (self.damage * 1.25)
        elif name == "Haris's Litter Picker":
            if rarity == "rare":
                self.damage *= 1
            elif rarity == "epic":
                self.damage = int (self.damage * 1.25) 
            elif rarity == "legendary":
                self.damage = int (self.damage * 1.5)
        elif name == "Gas From Locker 122":
            if rarity == "epic":
                self.damage *= 1
            elif rarity == "legendary":
                self.damage = int (self.damage * 1.25)
        elif name == "Mr Pope's Cheese":
            if rarity == "uncommon":
                self.damage *= 1
            elif rarity == "rare":
                self.damage = int (self.damage * 1.25) 
            elif rarity == "epic":
                self.damage = int (self.damage * 1.5)
    def add_rarity(self, name, type, rarity, duplicates):
        if type == "none":
            if name == "none":
                return
        elif type == "tie":
            if name == "Year 7 Tie":
                if rarity == "common":
                    if duplicates >= 6:
                        self.rarity = "uncommon"
                        duplicates -= 5
                elif rarity == "uncommon":
                    if duplicates >= 11:
                        self.rarity = "rare"
                        duplicates -= 10
            elif name == "Year 8 Tie":
                if rarity == "common":
                    if duplicates >= 4:
                        self.rarity = "uncommon"
                        duplicates -= 3
                elif rarity == "uncommon":
                    if duplicates >= 8:
                        self.rarity = "rare"
                        duplicates -= 7
                elif rarity == "rare":
                    if duplicates >= 16:
                        self.rarity = "epic"
                        duplicates -= 15
            elif name == "Year 9 Tie":
                if rarity == "uncommon":
                    if duplicates >= 3:
                        self.rarity = "rare"
                        duplicates -= 2
                elif rarity == "rare":
                    if duplicates >= 6:
                        self.rarity = "epic"
                        duplicates -= 5
                elif rarity == "epic":
                    if duplicates >= 12:
                        self.rarity = "legendary"
                        duplicates -= 11
            elif name == "Year 10 Tie":
                if rarity == "rare":
                    if duplicates >= 2:
                        self.rarity = "epic"
                        duplicates -= 1
                elif rarity == "epic":
                    if duplicates >= 4:
                        self.rarity = "legendary"
                        duplicates -= 3
            elif name == "Year 11 Tie":
                if rarity == "epic":
                    if duplicates >= 3:
                        self.rarity = "legendary"
                        duplicates -= 2
            elif type == "melee":
                if name == "shank":
                    if rarity == "rare":
                        if duplicates >= 4:
                            self.rarity = "epic"
                            duplicates -= 3
                    elif rarity == "epic":
                        if duplicates >= 8:
                            self.rarity = "legendary"
                            duplicates -= 7
                elif name == "Haris's Litter Picker":
                    if rarity == "rare":
                        if duplicates >= 4:
                            self.rarity = "epic"
                            duplicates -= 3
                    elif rarity == "epic":
                        if duplicates >= 8:
                            self.rarity = "legendary"
                            duplicates -= 7
                elif name == "Wooden Fork":
                    if rarity == "common":
                        if duplicates >= 6:
                            self.rarity = "uncommon"
                            duplicates -= 5
                    elif rarity == "uncommon":
                        if duplicates >= 11:
                            self.rarity = "rare"
                            duplicates -= 10
            elif type == "throwable":
                if name == "Mr Sargeant's Chair":
                    if rarity == "epic":
                        if duplicates >= 5:
                            self.rarity = "legendary"
                            duplicates -= 4
                elif name == "Lexie Malkin's Grenade":
                    if rarity == "rare":
                        if duplicates >= 4:
                            self.rarity = "epic"
                            duplicates -= 3
                    elif rarity == "epic":
                        if duplicates >= 8:
                            self.rarity = "legendary"
                            duplicates -= 7
                elif name == "Gas From Locker 122":
                    if rarity == "epic":
                        if duplicates >= 5:
                            self.rarity = "legendary"
                            duplicates -= 4
                elif name == "Mr Pope's Cheese":
                    if rarity == "uncommon":
                        if duplicates >= 6:
                            self.rarity = "rare"
                            duplicates -= 5
                    elif rarity == "rare":
                        if duplicates >= 11:
                            self.rarity = "epic"
                            duplicates -= 10
    def __str__(self):
        return f"Weapon: {self.name}, Damage: {self.damage}, Rarity: {self.rarity}, Duplicates: {self.duplicates}, Affects: {', '.join(self.affects)}"

#WEAPONS

none = weapons("none", "none", 1, [], "common", 1)
 
year_7_tie = weapons("Year 7 Tie", "tie", 5, [], "common", 0)
year_8_tie = weapons("Year 8 Tie", "tie", 10, [], "common", 0)
year_9_tie = weapons("Year 9 Tie", "tie", 15, [], "uncommon", 0)
year_10_tie = weapons("Year 10 Tie", "tie", 20, [], "rare", 0)
year_11_tie = weapons("Year 11 Tie", "tie", 30, [], "epic", 0)

shank = weapons("Shank", "melee", 20, [], "rare", 0)
mr_sargeants_chair = weapons("Mr Sargeant's Chair", "throwable", 25, [], "epic", 0)
wooden_fork = weapons("Wooden Fork", "melee", 5, [], "common", 0)
lexie_malkins_grenade = weapons("Lexie Malkin's Grenade", "throwable", 25, ["exploding"], "rare", 0)
rorys_glock_19 = weapons("Rory's Glock 19", "firearm", 40, [], "epic", 0)
hariss_litter_picker = weapons("Haris's Litter Picker", "melee", 20, ["grab"], "rare", 0)
gas_from_locker_122 = weapons("Gas From Locker 122", "throwable", 35, ["posion", "exploding"], "epic", 0)
mr_popes_cheese = weapons("Mr Pope's Cheese", "throwable", 30, [], "uncommon", 0)

#STATS

health = 100
inventory = []
late_coins = 0
areas_discovered = []
equipped_weapon = none

#ASKS THE QUESTIONS
def ask_question():
    global mode
    if mode == 1:
        question = r.choice(spanish_sentaces)
        incorrect_answers = r.choices(english_sentaces, k = 4)
        correct_answer = questions[question]
        print("Translate the following sentence to English:")
        t.sleep(1)
        print(question)
        t.sleep(1)
        options = incorrect_answers + [correct_answer]
        r.shuffle(options)
        option_1 = options[0]
        option_2 = options[1]
        option_3 = options[2]   
        option_4 = options[3]
        option_5 = options[4]
        print()
        print("1.", option_1)
        t.sleep(1)
        print("2.", option_2)
        t.sleep(1)
        print("3.", option_3)
        t.sleep(1)
        print("4.", option_4)
        t.sleep(1)
        print("5.", option_5)
        t.sleep(1)
        print()
        user_choice = int(input("Type the number of your answer: "))
        if user_choice == 1 and option_1 == correct_answer:
            print("Correct!")
            return True
        elif user_choice == 2 and option_2 == correct_answer:
            print("Correct!")
            return True
        elif user_choice == 3 and option_3 == correct_answer:
            print("Correct!")
            return True
        elif user_choice == 4 and option_4 == correct_answer:
            print("Correct!")
            return True
        elif user_choice == 5 and option_5 == correct_answer:
            print("Correct!")
            return True   
        else:
            print("Incorrect. The correct answer was:", correct_answer)
            return False
        
    else:
        question = r.choice(english_sentaces)
        incorrect_answers = r.choices(spanish_sentaces, k = 4)
        correct_answer = [key for key, value in questions.items() if value == question][0]
        print("Translate the following sentence to Spanish:")
        t.sleep(1)
        print(question)
        t.sleep(1)
        options = incorrect_answers + [correct_answer]
        r.shuffle(options)
        option_1 = options[0]
        option_2 = options[1]
        option_3 = options[2]   
        option_4 = options[3]
        option_5 = options[4]
        print()
        print("1.", option_1)
        t.sleep(1)
        print("2.", option_2)
        t.sleep(1)
        print("3.", option_3)
        t.sleep(1)
        print("4.", option_4)
        t.sleep(1)
        print("5.", option_5)
        t.sleep(1)
        print()
        user_choice = int(input("Type the number of your answer: "))
        if user_choice == 1 and option_1 == correct_answer:
            print("Correct!")
            return True
        elif user_choice == 2 and option_2 == correct_answer:
            print("Correct!")
            return True
        elif user_choice == 3 and option_3 == correct_answer:
            print("Correct!")
            return True
        elif user_choice == 4 and option_4 == correct_answer:
            print("Correct!")
            return True
        elif user_choice == 5 and option_5 == correct_answer:
            print("Correct!")
            return True   
        else:
            print("Incorrect. The correct answer was:", correct_answer)
            return False

#SAVE AND LOAD FUNCTIONS
    
game_dir = os.path.dirname(os.path.abspath(__file__))
save_name = "save_file.json"      #Retrives Path For Save File
save_dir = f"{game_dir}/{save_name}"

def save_data():
    '''Retrives Character Data And Updates The Save Data With It
    Is A Silent Task
    Returns To The Specified Location Or Menu

    >>> save_data()
    Would Save Data Silently And Return To The Previous Location
    '''
    if not os.path.exists(save_dir):
        open(save_dir, "w").close()
    data = {
        "health": health,
        "inventory": inventory,
        'year_7_tie.rarity': year_7_tie.rarity,
        "year_7_tie.duplicates": year_7_tie.duplicates,
        "year_7_tie_affects": year_7_tie.affects,
        "year_8_tie.rarity": year_8_tie.rarity,
        "year_8_tie.duplicates": year_8_tie.duplicates,
        "year_8_tie_affects": year_8_tie.affects,
        "year_9_tie.rarity": year_9_tie.rarity,
        "year_9_tie.duplicates": year_9_tie.duplicates,
        "year 9_tie_affects": year_9_tie.affects,
        "year_10_tie.rarity": year_10_tie.rarity,
        "year_10_tie.duplicates": year_10_tie.duplicates,
        "year_10_tie_affects": year_10_tie.affects,
        "year_11_tie.rarity": year_11_tie.rarity,
        "year_11_tie": year_11_tie.duplicates,
        "year_11_tie_affects": year_11_tie.affects,
        "shank.rarity": shank.rarity,
        "shank.duplicates": shank.duplicates,
        "shank_affects": shank.affects,
        "mr_sargeants_chair.rarity": mr_sargeants_chair.rarity,
        "mr_sargeants_chair.duplicates": mr_sargeants_chair.duplicates,
        "mr_sargeants_chair_affects": mr_sargeants_chair.affects,
        "wooden_fork.rarity": wooden_fork.rarity,
        "wooden_fork.duplicates": wooden_fork.duplicates,
        "wooden_fork_affects": wooden_fork.affects,
        "lexie_malkins_grenade.rarity": lexie_malkins_grenade.rarity,
        "lexie_malkins_grenade.duplicates": lexie_malkins_grenade.duplicates,
        "lexie_malkins_grenade_affects": lexie_malkins_grenade.affects,
        "rorys_glock_19.rarity": rorys_glock_19.rarity,
        "rorys_glock_19.duplicates": rorys_glock_19.duplicates,
        "rorys_glock_19_affects": rorys_glock_19.affects,
        "hariss_litter_picker.rarity": hariss_litter_picker.rarity,
        "hariss_litter_picker.duplicates": hariss_litter_picker.duplicates,
        "hariss_litter_picker_affects": hariss_litter_picker.affects,
        "gas_from_locker_122.rarity": gas_from_locker_122.rarity,
        "gas_from_locker_122.duplicates": gas_from_locker_122.duplicates,
        "gas_from_locker_122_affects": gas_from_locker_122.affects,
        "mr_popes_cheese.rarity": mr_popes_cheese.rarity,
        "mr_popes_cheese.duplicates": mr_popes_cheese.duplicates,
        "mr_popes_cheese_affects": mr_popes_cheese.affects,
        "areas_discovered": areas_discovered,
        "eqipped_weapon": eqipped_weapon.name,
    }
    
    with open(save_dir, "w") as a:
        j.dump(data, a)
    return

def load_save():
    global health, inventory, areas_discovered, eqipped_weapon
    global year_7_tie, year_8_tie, year_9_tie, year_10_tie, year_11_tie
    global shank, mr_sargeants_chair, wooden_fork, lexie_malkins_grenade
    global rorys_glock_19, hariss_litter_picker, gas_from_locker_122, mr_popes_cheese
    '''Retrives Data From The Save Data And Updates The Character Information
    Is A Silent Task
    Returns To The Previous Location
   
    >>> load_save()
    Would Update Character Data From Save File And Return To Previous Location
    '''
    with open(save_dir, "r") as f:
        data = j.load(f)
    health = data["health"]
    inventory = data["inventory"]
    year_7_tie.rarity = data["year_7_tie.rarity"]
    year_7_tie.duplicates = data["year_7_tie.duplicates"]
    year_7_tie.affects = data["year_7_tie_affects"]
    year_8_tie.rarity = data["year_8_tie.rarity"]
    year_8_tie.duplicates = data["year_8_tie.duplicates"]
    year_8_tie.affects = data["year_8_tie_affects"]
    year_9_tie.rarity = data["year_9_tie.rarity"]
    year_9_tie.duplicates = data["year_9_tie.duplicates"]
    year_9_tie.affects = data["year 9_tie_affects"]
    year_10_tie.rarity = data["year_10_tie.rarity"]
    year_10_tie.duplicates = data["year_10_tie.duplicates"]
    year_10_tie.affects = data["year_10_tie_affects"]       
    year_11_tie.rarity = data["year_11_tie.rarity"]
    year_11_tie.duplicates = data["year_11_tie"]
    year_11_tie.affects = data["year_11_tie_affects"]
    shank.rarity = data["shank.rarity"]
    shank.duplicates = data["shank.duplicates"]
    shank.affects = data["shank_affects"]
    mr_sargeants_chair.rarity = data["mr_sargeants_chair.rarity"]
    mr_sargeants_chair.duplicates = data["mr_sargeants_chair.duplicates"]
    mr_sargeants_chair.affects = data["mr_sargeants_chair_affects"]
    wooden_fork.rarity = data["wooden_fork.rarity"]
    wooden_fork.duplicates = data["wooden_fork.duplicates"]
    wooden_fork.affects = data["wooden_fork_affects"]
    lexie_malkins_grenade.rarity = data["lexie_malkins_grenade.rarity"]
    lexie_malkins_grenade.duplicates = data["lexie_malkins_grenade.duplicates"]
    lexie_malkins_grenade.affects = data["lexie_malkins_grenade_affects"]
    rorys_glock_19.rarity = data["rorys_glock_19.rarity"]
    rorys_glock_19.duplicates = data["rorys_glock_19.duplicates"]
    rorys_glock_19.affects = data["rorys_glock_19_affects"]
    hariss_litter_picker.rarity = data["hariss_litter_picker.rarity"]
    hariss_litter_picker.duplicates = data["hariss_litter_picker.duplicates"]
    hariss_litter_picker.affects = data["hariss_litter_picker_affects"]
    gas_from_locker_122.rarity = data["gas_from_locker_122.rarity"]
    gas_from_locker_122.duplicates = data["gas_from_locker_122.duplicates"]
    gas_from_locker_122.affects = data["gas_from_locker_122_affects"]
    mr_popes_cheese.rarity = data["mr_popes_cheese.rarity"]
    mr_popes_cheese.duplicates = data["mr_popes_cheese.duplicates"]
    mr_popes_cheese.affects = data["mr_popes_cheese_affects"]
    areas_discovered = data["areas_discovered"]
    eqipped_weapon.name = data["eqipped_weapon"]
    return data

def student_entrance():
    if "student_entrance" not in areas_discovered:
        print("Welcome To Madeley School ")
        t.sleep(1)
        print("Senor Hawkins Has Enlisted You To Save The School")
        t.sleep(1)
        print("It Is Infested With Many Monstrousities, Students And 'Hotel Bravo'")
        t.sleep(1)
        print()
        print("As You Walk Into The School, You See Three Tiny Creatinous Year 7s")
        t.sleep(1)
        three_year7s_fight()
    else:
        print("You Walk Into The Humanities Corridor")
        t.sleep(1)
        if "maths_cleared" in areas_discovered and "student_services" not in areas_discovered:
            print("You Notice The Student Services Door Is Now Open")
            t.sleep(1)
            print("You Feel Compelled To Enter It ")
        elif "maths_cleared" in areas_discovered and "student_services" in areas_discovered:
            print("")
        else:
            print("Student Services Is Still Closed")
            t.sleep(1)
            print("You Can:")
            t.sleep(0.25)
            print("'1' to '6' - Enter The Room Corresponding To The Number")
            t.sleep(0.25)
            print("'MATHS' - Walk Up The Stairs To The Maths Corrider")
            t.sleep(0.25)
            print("'MAIN' - Walk To The Main Entrance")
            t.sleep(0.25)
            print("'TOLIET' - Enter The Year 8-9 Toliets")
            humananities_corridor_move = input("")
            print()
            t.sleep(1)
            if humananities_corridor_move == "1":
                room_1()
            elif humananities_corridor_move == "2":
                room_2()
            elif humananities_corridor_move == "3":
                room_3()
            elif humananities_corridor_move == "4":
                room_4()
            elif humananities_corridor_move == "5":
                room_5()
            elif humananities_corridor_move == "6":
                room_6()
            elif humananities_corridor_move.upper() == "MATHS":
                maths_corridor()
            elif humananities_corridor_move.upper() == "MAIN":
                main_entrance
            elif humananities_corridor_move.upper() == "TOLIET":
                y8and9_toliet()
            else:
                print("Not A Valid Option. Try Again")
                t.sleep(1)
                print()
                student_entrance()

def main_entrance():
    if "main_entrance" not in areas_discovered:
        print("Mrs Downie Was Waiting For You")
        t.sleep(1)
        print("You Were Late So She Has Decided To Give You")
        t.sleep(1)
        print("An AI Generated, Cypto Currency Late Coin")
        t.sleep(1)
        print()
        late_coins += 1
        mrs_downie_fight
        
def maths_corridor():
    print()

def room_1():
    print()
    
def room_2():
	print()
 
def room_3():
	print()

def room_4():
	print()
 
def room_5():
	print()
 
def room_6():
	print()

def y8and9_toliet():
    print()

def three_year7s_fight():
    neg2_a_or_d = none
    prev_a_or_d = none
    a_or_d = none
    global health, equipped_weapon, areas_discovered
    global year7s_health_1, year7s_health_2, year7s_health_3
    year7s_health_1 = 5
    year7s_health_2 = 5
    year7s_health_3 = 5
    year7s_affects = []
    print("The Year 7s Look Hungry. They Haven't Eaten For Years")
    t.sleep(1)
    print("The Are 3 Of Them With 5 Health Each")
    t.sleep(1)
    print("They Begin Running Towards And Attacking")
    t.sleep(1)
    print()
    while year7s_health_1 > 0 or year7s_health_2 > 0 or year7s_health_3 > 0 or health > 0:
        year7_damage = 0
        year7_alive = 0
        neg2_a_or_d = prev_a_or_d
        prev_a_or_d = a_or_d
        a_or_d = r.choice (["attack", "defend"])
        if "grabbed" in year7s_affects:
            print("The Year 7s Are Unable To Attack As You Have Them Grabbed")
            t.sleep(1)
            a_or_d = "attack"
        elif "frozen" in year7s_affects:
            print("The Year 7s Can't Attack Because They Are Frozen")
            t.sleep(1)
            a_or_d = "attack"
        if "poisoned" in year7s_affects:
            year7s_health_1 -= 1
            year7s_health_2 -= 1
            year7s_health_3 -= 1
            print("You Did You 1 Damage To All The Year 7s From Posioning")
            t.sleep(1)
            print(f"Year 7 1: {year7s_health_1} Health, 2: {year7s_health_2} Health, 3: {year7s_health_3} Health")
            t.sleep(1)
        if "burned" in year7s_affects:
            year7s_health_1 -= 1
            year7s_health_2 -= 1
            year7s_health_3 -= 1
            print("You Did You 1 Damage To All The Year 7s From Burning")
            t.sleep(1)
            print(f"Year 7 1: {year7s_health_1} Health, 2: {year7s_health_2} Health, 3: {year7s_health_3} Health")
            t.sleep(1)
        if prev_a_or_d == "defend" and neg2_a_or_d == "defend":
            a_or_d = "attack"
        elif prev_a_or_d == "attack" and neg2_a_or_d == "attack":
            a_or_d = "defend"
        if a_or_d == "attack":
            print("Its Your Turn To Attack")
            t.sleep(1)
            attack_success = ask_question()
            t.sleep(1)
            print()
            if attack_success == True:
                if equipped_weapon.type == "explosive" or "lingering" in equipped_weapon.affects:
                    year7s_health_1 -= equipped_weapon.damage
                    year7s_health_2 -= equipped_weapon.damage
                    year7s_health_3 -= equipped_weapon.damage
                    year7s_affects.append(equipped_weapon.affects)
                    refresh_y7_health()
                    print(f"You Attack All Three Year 7s For {equipped_weapon.damage} Damage Each")
                    t.sleep(1)
                    print(f"Year 7 1: {year7s_health_1} Health, 2: {year7s_health_2} Health, 3: {year7s_health_3} Health")
                    if len(equipped_weapon.affects) != 0:
                        t.sleep(1)
                        print(f"You Applied {equipped_weapon.affects} To All Of The Year 7s")
                else:
                    whichy7 = choose_year7()
                    if whichy7 == 1:
                        year7s_health_1 -= equipped_weapon.damage
                        year7s_affects.append(equipped_weapon.affects)
                        refresh_y7_health()
                        print(f"You Dealt {equipped_weapon.damage} Damage To The First Year 7")
                        t.sleep(1)
                        print(f"Year 7 1: {year7s_health_1} Health, 2: {year7s_health_2} Health, 3: {year7s_health_3} Health")
                        if len(equipped_weapon.affects) != 0:
                            t.sleep(1)
                            print(f"You Applied {equipped_weapon.affects} To All Of The Year 7")
                    elif whichy7 == 2:
                        year7s_health_2 -= equipped_weapon.damage
                        year7s_affects.append(equipped_weapon.affects)
                        refresh_y7_health()
                        print(f"You Dealt {equipped_weapon.damage} Damage To The Second Year 7")
                        t.sleep(1)
                        print(f"Year 7 1: {year7s_health_1} Health, 2: {year7s_health_2} Health, 3: {year7s_health_3} Health")
                        if len(equipped_weapon.affects) != 0:
                            t.sleep(1)
                            print(f"You Applied {equipped_weapon.affects} To All Of The Year 7")
                    elif whichy7 == 3:
                        year7s_health_3 -= equipped_weapon.damage
                        year7s_affects.append(equipped_weapon.affects)
                        refresh_y7_health()
                        print(f"You Dealt {equipped_weapon.damage} Damage To The Third Year 7")
                        t.sleep(1)
                        print(f"Year 7 1: {year7s_health_1} Health, 2: {year7s_health_2} Health, 3: {year7s_health_3} Health")
                        if len(equipped_weapon.affects) != 0:
                            t.sleep(1)
                            print(f"You Applied {equipped_weapon.affects} To All Of The Year 7")     
            else:
                print("You Missed Your Attack")
            t.sleep(1)
            print()
        else:
            if year7s_health_1 > 0:
                year7_damage += 2
                year7_alive += 1
            if year7s_health_2 > 0:
                year7_damage += 2
                year7_alive += 1
            if year7s_health_3 > 0:
                year7_damage += 2
                year7_alive += 1
            if year7_alive == 1:
                print("The 1 Remaining Year 7 Is Attacking")
            else:
                print(f"The {year7_alive} Year 7s Are Attacking")
            t.sleep(1)
            print()
            dodge_success = ask_question()
            if dodge_success == True:
                print("You Dodged The Year 7s Attack")
            else:
                health -= year7_damage
                if year7_alive == 1:
                    print("The One Year 7 Successfully Attacked You")
                    t.sleep(1)
                    print(f"It Did {year7_damage} Damage. You Have {health} Health Left")
                else:
                    print(f"The {year7_alive} Year 7s Successfully Attacked You")
                    t.sleep(1)
                    print(f"They Did {year7_damage} Damage. You Have {health} Health Left")
                    t.sleep(1)
                    print("They Did 2 Damage Each")
            t.sleep(1)
            print()     
    if year7s_health_1 <= 0 and year7s_health_2 <= 0 and year7s_health_3 <= 0:
        year_7_tie.add_duplicates(3)
        print("You Defeated All The 3 Foot Monsters")
        t.sleep(1)
        print("You Take All Three Of Their Ties For Weapons")
        areas_discovered.append("student_entrance")
        t.sleep(1)
        print()
        print("Now That The Student Entrance Is Clear")
        t.sleep(1)
        student_entrance()
    if health <= 0:
        print("You Have Died")
        t.sleep(1)
        heath = 100
        inventory = []
        equipped_weapon = "none"
        print("Health, Inventory and Equipped Weapon Have Been Reset")
        t.sleep(1)
        print()
        student_entrance()
                     
def choose_year7():
    global year7s_health_1, year7s_health_2, year7s_health_3
    attack_which = int(input("Which Year 7 Do You Want To Attack? 1/2/3 "))
    t.sleep(1)
    if attack_which == 1 and year7s_health_1 >= 0:
        return 1
    elif attack_which == 2 and year7s_health_2 >= 0:
        return 2
    elif attack_which == 3 and year7s_health_3 >= 0:
        return 3
    else:
        print("Not A Valid Option. Try Again")
        t.sleep(1)
        choose_year7()
    
def refresh_y7_health():
    global year7s_health_1, year7s_health_2, year7s_health_3
    if year7s_health_1 <= 0:
        year7s_health_1 = 0
    elif year7s_health_1 >= 5:
        year7s_health_1 = 5
    if year7s_health_2 <= 0:
        year7s_health_2 = 0
    elif year7s_health_2 >= 5:
        year7s_health_2 = 5
    if year7s_health_3 <= 0:
        year7s_health_3 = 0
    elif year7s_health_3 >= 5:
        year7s_health_3 = 5
        
def mrs_downie_fight():
    global mrs_downie_health, mrs_downie_affects, health, equipped_weapon
    mrs_downie_health = 10
    print("You Are Fighting Mrs Downie")
    mrs_downie_affects = []
    t.sleep(1)
    print("She Has 10 Health")
    t.sleep(1)
    print("The More Rounds You Survive The More Damage She Does")
    t.sleep(1)
    print("eg  First Round You Have 1 Late Coin She Does 1 Damage, 10th Round She Does 10 Damage")
    t.sleep(1)
    print("Late Coins Go Over Fights And Can Be Used In The Shop")
    t.sleep(1)
    print()
    while mrs_downie_health > 0 and health > 0:
        a_or_d = r.choice(["attack", "defend"])
        if "grabbed" in mrs_downie_affects:
            print("Mrs Downie Can Not Attack Because You Have Her Grabbed")
            t.sleep(1)
            a_or_d = "attack"
        elif "frozen" in mrs_downie_affects:
            print("Mrs Downie Can Not Attack Because She Is Frozen")
            t.sleep(1)
            a_or_d = "attack"
        if "poisioned" in mrs_downie_affects:
            mrs_downie_health -= 1
            mrs_downie_health_refresh()
            print(f"Mrs Downie Has Lost 1 Health From Posion")
            t.sleep(1)
            print(f"She Is On {mrs_downie_health} Health")
        if "burned" in mrs_downie_affects:
            mrs_downie_health -= 1
            mrs_downie_health_refresh()
            print("Mrs Downie Has Lost 1 Health From Burning")
            t.sleep(1)
            print(f"She Is On {mrs_downie_health} Health")
        if a_or_d == "attack":
            print("Its You Turn To Attack")
            t.sleep(1)
            print()
            attack_sucess = ask_question()
            print()
            t.sleep(1)
            if attack_sucess == True:
                mrs_downie_health -= equipped_weapon.damage
                mrs_downie_health_refresh()
                print(f"You Hit Mrs Downie For {equipped_weapon.damage}")
                t.sleep(1)
                print(f"She Now Has {mrs_downie_health}")
                if len(equipped_weapon.affects) > 0:
                    t.sleep(1)
                    print(f"You Have Applied {equipped_weapon.affects} To Mrs Downie")
            else:
                print("You Missed Your Attack")
        else:
            print("Mrs Downie Is Attacking")
            t.sleep(1)
            print()
            dodge_success = ask_question()
            if dodge_success == True:
                print("You Dodge Mrs Downie's Attack")
            else:
                health -= late_coins
                print(f"Mrs Downie Hit Her Attack For {late_coins} Damage")
                t.sleep(1)
                print(f"You Have {health} Health")
        t.sleep(1)
        print()
        late_coins *= 2
        print("You Late Coins Have Doubled")
        t.sleep(1)
        print(f"You Have {late_coins} Late Coins")
        t.sleep(1)
        print()            
    if mrs_downie_health <= 0:
        print("You Have Defeated Mrs Downie")
        t.sleep(1)
        print("You Get To Keep Your Late Coins")
        t.sleep(1)
        print("You Have Unlocked The Late Shop")
        t.sleep(1)
        print("In The Shop You Can But Ties")
        areas_discovered.append("main_entrance")
        t.sleep(1)
        print()
        main_entrance()
    if health <= 0:
        print("You Have Died")
        t.sleep(1)
        heath = 100
        inventory = []
        equipped_weapon = "none"
        print("Health, Inventory and Equipped Weapon Have Been Reset")
        t.sleep(1)
        print()
        main_entrance
               
def mrs_downie_health_refresh():
    global mrs_downie_health
    if mrs_downie_health <= 0:
        mrs_downie_health = 0
    elif mrs_downie_health >= 10:
        mrs_downie_health = 10
        
               
def revision():
    amount_of_times = int(input("How Many Times Do You Want To Play The Game? "))
    mode = int(input("Choose 1. Spanish To English Or 2. English To Spanish. Use The Number Only: "))
    for times in range(1, amount_of_times + 1):
        ask_question()
        
if __name__ == "__main__":
    print("Type 1 To Revise Spanish To English Or 2 For English To Spanish")
    mode = int(input())
    if mode != 1:
        mode = 2
    print("Would You Like To Play Story Mode Or Revision Mode? 1. Story Mode 2. Revision Mode")
    game_mode = int(input())
    print()
    t.sleep(1)
    if game_mode == 1:
        student_entrance()
    else:
        revision()