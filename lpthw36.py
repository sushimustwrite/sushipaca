from sys import exit

def start():
    print """You face an aged wizard in front of a gate.
    What do you do?"""

    do = raw_input("> ")

    if "talk" in do or "speak" in do or "say" in do:
        password()
    elif "fight" in do or "duel" in do:
        fight()
    elif "flee" in do or "run" in do:
        print dead("An alpaca with an anvil strapped to it falls from the sky and hits you on the head.")
    else:
        start()

def fight():
    print "The wizard casts a confusion spell on you."
    print "Do you wait for the spell to wear off or"
    print "do you do a rain dance?"
    
    spell = raw_input("> ")
    
    if "wait" in spell:
        start()
    elif "dance" in spell or "do" in spell:
        dead("Your dance brings a storm of alpacas to the scene. You get struck by lightning.")
    else:
        dead("You really shouldn't have done that.")
        
def password():
    print "The wizard asks you for a password. What do you tell him?"
    gate_opened = False
    
    while True:
        pw = raw_input("> ")
        if pw == "alpaca" and gate_opened == False:
            print "The wizard steps aside. You can open the gate now."
            gate_opened = True
        elif pw == "open gate" or pw == "open door" and gate_opened == True:
            castle()
        else:
            dead("YOU SHALL NOT PASS! The wizard turns you into a newt.")
    
def castle():
    print "You stand in the foyer of a castle."
    print "There is a door straight ahead, and there are doors to your left and right."
    print "Which way do you go?"
    
    while True:
        go = raw_input("> ")
        if go == "left":
            left()
        elif go == "right":
            right()
        elif go == "straight":
            dead("A ninja sneaks up behind you and cuts you.")
        else:
            print "I'm sorry, but you can't do that."

def left():
    print "A sushi chef stands behind a counter preparing sushi."
    print "He offers you a roll."
    print "Do you eat the sushi? (y/n)"
    
    while True:
        sushi = raw_input("> ")
        if sushi == "y" or sushi == "yes":
            print "The sushi's soul screams as you enjoy your food."
            dead("You vomit the sushi on the floor and continue vomiting until you've exhausted your body of fluids.")
        elif sushi == "n" or sushi == "no":
            print "Good job! Sushis don't like being eaten. You win!"
            exit(0)
        else:
            print "Dude, you gonna eat the sushi or not?"
        
def right():
    print "A teleporter sits in front of you."
    print "Use the numeric keypad to enter your password."
    
    while True: 
        right = raw_input("> ")
        if right.isdigit() == False:
            print "You gonna put a number in or what?"
        elif int(right) % 2 == 0:
            left()
        elif int(right) % 2 == 1:
            dead("A ninja sneaks up behind you and cuts you.")
        else:
            print "You gonna put a number in or what?"
        
def dead(why):
    print why, "Your adventure ends here."
    exit(0)
    
start()