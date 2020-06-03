import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1.5)


def game_over(level):
    print_pause("Game Over\n")
    print_pause("Try Again?")
    while True:
        restart = input("Enter Y or N\n").lower()
        if restart == "y" or restart == "yes":
            print_pause("Good choice!\n")
            if level == 1:
                level_1(level)
            elif level == 2:
                level_2(level)
            elif level == 3:
                level_3(level)
            elif level == 4:
                level_4(level)
            elif level == 5:
                level_5(level)
        elif restart == "n" or restart == "no":
            print_pause("Thanks for playing, goodbye!\n")
            exit()
        else:
            print_pause("Please make a valid selection.")
    return restart


def intro(level):
    print_pause("Welcome to Legends of the Forbidden Temple!\n")
    print_pause("You have just landed after jumping out of an airplane\n")
    print_pause("into the thick Cambodian jungle.\n")
    print_pause("Your mission, should you choose to accept it:\n")
    print_pause("is to retrieve an ancient relic\n")
    print_pause("deep in the forbidden temple.\n")
    level_1(level)


def level_1(level):
    level = 1
    print_pause("Level " + str(level))
    print_pause("The sun has now set, you need to act quick!\n")
    print_pause("What do you do?")
    while True:
        option = input("1. Look for shelter to rest\n"
                       "2. Press onwards\n")
        if option == '1':
            print_pause("\nYou quickly fall asleep.\n")
            print_pause("You are so glad you got a good nights rest.\n")
            print_pause("Now you have the energy to press on.\n")
            level = 2
            level_2(level)
        elif option == "2":
            print_pause("\nAfter a few hours of hiking by a creek\n")
            print_pause("you draw weary.\n")
            print_pause("You start seeing things that are not really there.\n")
            print_pause("You come to the end of the creek\n")
            print_pause("and find yourself on the side of a mountain.\n")
            print_pause("You try to climb down the mountain\n")
            print_pause("but as you scale downwards you slip\n")
            print_pause("and fall into the deep abyss.\n")
            game_over(level)
        else:
            print_pause("Please make a valid selection")
    return option


def level_2(level):
    level = 2
    print_pause("Level " + str(level))
    print_pause("Up ahead you spot a creek and follow it downstream.\n")
    print_pause("After several more minutes of walking\n")
    print_pause("you come to a fork in the road.\n")
    print_pause("What do you do?")
    while True:
        turn = input("1. Take the Left Path\n"
                     "2. Take the Right Path \n")
        if turn == '1':
            print_pause("\nYou walk on and on...\n")
            print_pause("Hours pass by...\n")
            print_pause("There is no end in sight.\n")
            print_pause("You can't find your way back.\n")
            print_pause("You are lost forever!\n")
            game_over(level)
        elif turn == '2':
            print_pause("\nCongratulations!\n")
            print_pause("You found the entrance to the forbidden temple!\n")
            level_3(level)
        else:
            print_pause("Please make a valid selection")
    return turn


def level_3(level):
    level = 3
    print_pause("Level " + str(level))
    print_pause("However... right in front of you is a deep dark pit.\n")
    print_pause("It's so deep you can't even see the bottom.\n")
    print_pause("What do you do?")
    deep_pit = input("1. You take your chances and try to jump over the pit\n"
                     "2. You take a second to think of other options.\n")
    while True:
        if deep_pit == "1":
            chance = random.randint(1, 2)
            if chance == 1:
                print_pause("\nYou back up a few feet\n")
                print_pause("to get a running start.\n")
                print_pause("You take a deep breath and hold it in.\n")
                print_pause("EXHALE...\n")
                print_pause("You dash down the dirt pathway\n")
                print_pause("You take a giant leap into the air,\n")
                print_pause("jumping across the deep dark pit,\n")
                print_pause("and land safely on the other side!\n")
                print_pause("SUCCESS!\n")
                level_4(level)
            if chance == 2:
                print_pause("\nYou back up a few feet\n")
                print_pause("to get a running start.\n")
                print_pause("You take a deep breath and hold it in.\n")
                print_pause("EXHALE...\n")
                print_pause("You dash down the dirt pathway\n")
                print_pause("mis-calculate your footing,\n")
                print_pause("trip,\n")
                print_pause("and fall head first\n")
                print_pause("into the deep dark pit...\n")
                game_over(level)
        elif deep_pit == '2':
            print_pause("\nYou take a second to think things through.\n")
            print_pause("You notice\n")
            print_pause("right above in the middle of the pit\n")
            print_pause("is an overhand branch from a nearby tree.\n")
            print_pause("You also just remembered\n")
            print_pause("that you still have your parachute rip cord.\n")
            print_pause("You roll up the cord and in a lasso'ing motion\n")
            print_pause("you toss one end and it catches onto the branch.\n")
            print_pause("You tug on the rope.\n")
            print_pause("It appears tightly bound to the branch..\n")
            print_pause("You jump,\n")
            print_pause("swing over the deep dark pit,\n")
            print_pause("and stick the landing on the other side.\n")
            print_pause("Great job!\n")
            level_4(level)
        else:
            print_pause("Please make a valid selection")
    return deep_pit


def level_4(level):
    level = 4
    print_pause("Level " + str(level))
    print_pause("You press onward and enter the tomb.\n")
    print_pause("After several hours of walking\n")
    print_pause("you finally stumble upon\n")
    print_pause("the ancient relic you came searching for.\n")
    print_pause("It's a golden monkey statue!\n")
    print_pause("What do you do?")
    golden_monkey = input("1. You grab the monkey and make a run for it!\n"
                          "2. You take a second to think of other options.\n")
    while True:
        if golden_monkey == '1':
            chance = random.randint(1, 2)
            if chance == 1:
                print_pause("\nYou stand there\n")
                print_pause("holding the golden monkey in your hands.\n")
                print_pause("It's heavy.\n")
                print_pause("And cold.\n")
                print_pause("All of a sudden\n")
                print_pause("you have chills running down your back.\n")
                print_pause("The earth beneath you begins to shake.\n")
                print_pause("The walls around you begin to crumble.\n")
                print_pause("You look up and see a huge rock.\n")
                print_pause("It comes straight for your head.\n")
                print_pause("You quickly side-step\n")
                print_pause("as it crashes onto the floor,\n")
                print_pause("crumbling into a million little pieces,\n")
                print_pause("right where you were standing before.\n")
                print_pause("Congratulations!\n")
                print_pause("You dodged a bullet on this one.\n")
                level_5(level)
            if chance == 2:
                print_pause("\nYou stand there...\n")
                print_pause("holding the golden monkey in your hands.\n")
                print_pause("It's heavy.\n")
                print_pause("And cold.\n")
                print_pause("All of a sudden\n")
                print_pause("you have chills running down your back.\n")
                print_pause("The earth beneath you begins to shake.\n")
                print_pause("The walls around you begin to crumble.\n")
                print_pause("You look up and the last thing you see\n")
                print_pause("is a huge boulder\n")
                print_pause("coming straight for your head.\n")
                game_over(level)
        elif golden_monkey == '2':
            print_pause("\nYou take a second to think things through.\n")
            print_pause("You remember seeing\n")
            print_pause("something like this in a movie before.\n")
            print_pause("You rip off a piece of parachute cloth\n")
            print_pause("load it with a handfull of sand\n")
            print_pause("and tie off the top to make a sandbag.\n")
            print_pause("You grab the monkey\n")
            print_pause("and immediately replace it with the sandbag.\n")
            print_pause("You stand there, in the quiet...\n")
            level_5(level)
        else:
            print_pause("Please make a valid selection")
    return golden_monkey


def level_5(level):
    level = 5
    print_pause("Level " + str(level))
    print_pause("A few seconds later you see a huge round bolder\n")
    print_pause("the size of a massive SUV come rolling down\n")
    print_pause("and you are standing right in it's path.\n")
    print_pause("You make a run for it.\n")
    print_pause("The boulder chases you.\n")
    print_pause("You come out of a tunnel\n")
    print_pause("just barely staying a few feet in front of it.\n")
    print_pause("You come out of the mountain and appear on a cliff.\n")
    print_pause("There is a running river beneath you.\n")
    print_pause("What do you do?")
    jump = input("1. You jump into the river\n"
                 "2. You take a second to think of other options.\n")
    while True:
        if jump == '1':
            print_pause("\nYou jump!\n")
            print_pause(".\n")
            print_pause("...\n")
            print_pause("...\n")
            print_pause("....\n")
            print_pause("You crash into the river\n")
            print_pause("just barely holding onto the golden monkey.\n")
            print_pause("The boulder flys out of the tunnel above\n")
            print_pause("crashing into the river right beind you.\n")
            print_pause("You survived the jump!\n")
            print_pause("You swim to shore\n")
            print_pause("and call your plane to come take you home.\n")
            print_pause("The plane arrives and you get in.\n")
            print_pause("Before you take off, you hear an alarm go off\n")
            print_pause("")
            print_pause("Ring!\n")
            print_pause("Ring!!\n")
            print_pause("Ring!!!\n")
            print_pause("You find yourself, laying in your bed at home.\n")
            print_pause("You reach over to shut off the alarm.\n")
            print_pause("This magical adventure was all a dream.\n")
            print_pause("Thanks for playing.\n")
            print_pause("Have a nice day!\n")
            exit()
        elif jump == '2':
            print_pause("\nYou take a second to think things through.\n")
            print_pause("Wrong choice this time!\n")
            print_pause("The huge boulder clobbers on top of you\n")
            print_pause("flattening you into the grounnd\n")
            print_pause("like pizza dough.\n")
            print_pause("Everything turns black around you.\n")
            game_over(level)
        else:
            print_pause("Please make a valid selection")
    return jump


def play_game():
    level = []
    intro(level)
    level_1(level)
    level_2(level)
    level_3(level)
    level_4(level)
    level_5(level)
    game_over(level)


play_game()
