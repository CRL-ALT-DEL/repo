import time

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(0)


def game_over(level):
    print_pause("Game Over\n")
    print_pause("Try Again?")
    restart = input("Enter Y or N\n").lower()
    if restart == "y" or restart == "yes":
        print_pause("Good choice!\n")
        print_pause(level)
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
    elif restart =="n" or restart == "no":
        print_pause("Thanks for playing, goodbye!\n")
    else:
        print_pause("Please make a valid selection")
        game_over()
        

def intro(level):
    print_pause("Welcome to Legends of the Forbidden Temple!\n")
    print_pause("You have just landed after jumping out of an airplane into the thick Cambodian jungle.\n")
    print_pause("Your mission, should you choose to accept it...\n")
    print_pause("is to retrieve an ancient relic deep in the forbidden tomb.\n")
    level_1(level)
    

def level_1(level):
    level=("1")
    print_pause("Level "+(level))
    print_pause("The sun has now set, you need to act quick!\n")
    print_pause("What do you do?")
    option = input("1. Look for shelter to rest\n"
                "2. Press onwards\n")
    if option == '1':
        print_pause("\nYou quickly fall asleep.\n")
        print_pause("You are so glad you got a good nights rest.\n")
        print_pause("Now you have the energy to press on.\n")
        level=2
        level_2(level)
    elif option =="2":
        print_pause("\nAfter a few hours of hiking by a creek you draw weary.\n")
        print_pause("You start seeing things that are not really there.\n")
        print_pause("You came to the end of the creek and are at the edge of the mountain\n")
        print_pause("You try to climb down the mountain but as you scale downwards you slip and fall into the abyss.\n")
        game_over(level)
    else:
        print_pause("Please make a valid selection")


def level_2(level):
    level=("2")
    print_pause("Level "+(level))
    print_pause("Up ahead you spot a creek and follow it downstream.\n")
    print_pause("After several more minutes of walking you come to a fork in the road.\n")
    print_pause("What do you do?")
    turn = input("1. Take the Left Path\n"
                "2. Take the Right Path \n")
    if turn == '1':
        print_pause("\nYou walk on and on....\n")
        print_pause("Hours pass by...\n")
        print_pause("There is no end in sight...\n")
        print_pause("You can't find your way back and are lost forever!\n")
        game_over(level)
    elif turn == '2':
        print_pause("\nCongratulations!! You found the entrance to the tomb!\n") 
        level_3(level)
    else:
        print_pause("Please make a valid selection")


def level_3(level):
    level=("3")
    print_pause("Level "+(level))
    print_pause("However... right in front of you is a deep dark pit...\n")
    print_pause("It's so deep you can't even see the bottom.\n")
    print_pause("What do you do?")
    deep_pit = input("1. You take your chances and try to jump over the pit.\n"
            "2. You take a second to think of other options.\n")
    if deep_pit == "1":
        print_pause("\nYou back up a few good feet to get a running start...\n")
        print_pause("You take a deep breath and hold it before exhaling...\n")
        print_pause("This is it, you dash down the dirt pathway...\n")
        print_pause("...mis-calculate your footing...\n")
        print_pause("...trip and fall head first into the deep dark pit...\n")
        game_over(level)
    elif deep_pit == '2':
        print_pause("\nYou take a second to think things through.\n") 
        print_pause("You noticed that right above in the middle of the pit is an overhand branch from a nearby tree.\n")
        print_pause("You also just remembered that you still have your parachute rip cord.\n")
        print_pause("You roll up the cord and in a lasso'ing motion you toss one end onto the branch!\n")
        print_pause("You tug on the rope and it appears tightly bound to the branch\n")
        print_pause("You jump, swing over the deep dark pit and stick the landing on the other side. Great job!\n")
        level_4(level)
    else:
        print_pause("Please make a valid selection")

def level_4(level):
    level=("4")
    print_pause("Level "+(level))
    print_pause("You press onward and enter the tomb.\n")
    print_pause("After several hours of walking you finally stumble upon the ancient relic you came looking for.\n")
    print_pause("It's a golden monkey statue!\n")
    print_pause("What do you do?")
    golden_monkey = input("1. You grab the monkey and make a run for it!\n"
            "2. You take a second to think of other options.\n")
    if golden_monkey == '1':
        print_pause("\nYou stand there holding the golden monkey in your hands...\n")
        print_pause("It's heavy...\n")
        print_pause("and cold...\n")
        print_pause("all of a sudden you have chills running down your back and realized you have made a grave mistake...\n")
        print_pause("the earth beneath you begins to shake...\n")
        print_pause("the walls around you begin to fall...\n")
        print_pause("you look up and see a huge rock that comes straight for your head...\n")
        game_over(level)
    if golden_monkey == '2':
        print_pause("\nYou take a second to think things through.\n") 
        print_pause("You remember seeing something like this in a movie before.\n")
        print_pause("You rip off a piece of parachute cloth, load it with a handfull of sand and tie off the top to make a sandbag.\n")
        print_pause("You step up towards the golden monkey...\n")
        print_pause("You grab the monkey and immediately replace it with the sand bag you just made...\n")
        print_pause("You stand there, in the quiet for a few seconds...\n")
        level_5(level)
 

def level_5(level):
    level=("5")
    print_pause("Level "+(level))
    print_pause("A few seconds later you see a huge bolder the size of an SUV come rolling down from a second story level, and you are right in it's pathway...\n")
    print_pause("You make a run for it towards this opening where light is peeking through the end of a tunnel.\n")
    print_pause("The boulder chases you...\n")
    print_pause("You come out of the tunnel, just out running the bolder by a few feet, and appear on a cliff just out side of a mountain with a running river beneath you...\n")
    print_pause("What do you do?")
    jump = input("1. You jump into the river\n"
            "2. You take a second to think of other options.\n")
    if jump == '1':
        print_pause("\nYou jump!\n")
        print_pause("...\n")
        print_pause("...\n")
        print_pause("...\n")
        print_pause("...\n")
        print_pause("You crash in to the river, just barely holding onto the golden monkey...\n")
        print_pause("The boulder flys out of the tunnel above and you hear it crash into the river right beind you...\n")
        print_pause("You have survived!\n")
        print_pause("You swim to shore and radio in your plane to take you home...\n")
        print_pause("The plane arrives and you get in.\n")
        print_pause("Did you accidentally drop the golden monkey and pick up this log right before boarding this plane instead?\n")
        print_pause("Before you can decide on what to do next, you are awaken by your alarm clock going off...\n")
        print_pause("Ring!!!\n")
        print_pause("Ring!!!\n")
        print_pause("Ring!!!\n")
        print_pause("This was all a dream.\n")
        print_pause("Thanks for playing!\n")
    if jump == '2':
        print_pause("\nYou take a second to think things through.\n") 
        print_pause("Wrong choice this time!\n")
        print_pause("The huge boulder crashes ontop of you, and flattens you into the grounnd like pizza dough...\n")
        print_pause("All turns black around you.\n")
        game_over(level)

      

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
