def tutorial():
    global tutorial_done, menu_tutorial_done, fight_tutorial_done, text_tutorial_done
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
            game_start()
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
            beach()
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
    global text_tutorial_back, text_tutorial_forward, text_tutorial_chest, text_tutorial_done
    if text_tutorial_back == True and text_tutorial_forward == True and text_tutorial_chest == True:
        print("Well Done You Completed The First Tutorial Section")
        t.sleep(1)
        text_tutorial_done = True
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
    global text_tutorial_back, text_tutorial_forward, text_tutorial_done
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
    global text_tutorial_back, text_tutorial_forward, text_tutorial_done
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
    global text_tutorial_back, text_tutorial_forward, text_tutorial_done
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
    global fight_tutorial_attack, fight_tutorial_dodge, fight_tutorial_crit, fight_tutorial_done, health
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
                if quick_time_event(3, "random", "Attack the White Box") == True:
                    t.sleep(0.5)
                    white_box_health_taken = 1 * damage
                    white_box_health -= white_box_health_taken
                    print(f"You Attacked the White Box For {white_box_health_taken} Damage. It Now Has {white_box_health} Health Left")
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

def menu_tuorial_part_1(): 
    global menu_tutorial_access, menu_tutorial_basic, menu_tutorial_save
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
        menu_tuorial_part_1()
    elif menu_1_option == "GO AWAY":
        print("What Have I Done")
        t.sleep(1)
        print("Doesn't Matter Because You Failed The Objective.")
        t.sleep(1)
        print("Try Again")
        t.sleep(1)
        print()
        menu_tuorial_part_1()
    elif menu_1_option == "I HATE YOU":
        print("Well That Was Very Mean")
        t.sleep(1)
        print("And You Didn't Even Complete The Objective.")
        t.sleep(1)
        print("So You Have Try Again Which You Deserve")
        t.sleep(1)  
        print()
        menu_tuorial_part_1()
    elif menu_1_option == "MENU":
        menu_tutorial_part_2()
        
def menu_tutorial_part_2():
    global menu_tutorial_access, menu_tutorial_basic, menu_tutorial_save, menu_tutorial_done
    if menu_tutorial_access == True and menu_tutorial_basic == True and menu_tutorial_save == True:
        print("Well Done You Completed The Menu Tutorial")
        menu_tutorial_done = True
        t.sleep(1)
        print()
        tutorial()
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
        menu_tutorial_part_2()
    elif menu_2_option == "ARMOUR" or menu_2_option == "CLASS" or menu_2_option == "WEATHER":
        print(f"Well Done You Viewed Your Some Information On")
        t.sleep(1)
        print("But It Wasn't Nessecary For The Objective")
        t.sleep(1)
        print("Going Back To Menu")
        t.sleep(1)
        print()
        menu_tutorial_part_2()
    elif menu_2_option == "SAVE":
        print("Well Done You Saved Your Data")
        t.sleep(1)
        print("You Completed The Menu Tutorial")
        menu_tutorial_save = True
        print()
        tutorial()
    if menu_tutorial_access == True and menu_tutorial_basic == True and menu_tutorial_save == True:
        print("Well Done You Completed The Menu Tutorial")
        menu_tutorial_done = True
        t.sleep(1)
        print()
        tutorial()