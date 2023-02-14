import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause("You are in a train...")
    print_pause("The FBI suspects that someone will blow the train up!!!")
    print_pause("Your mission is to find who it is ANONIMISLY!")
    print_pause("Your suspection list are:\n" "asian old man who wears \
    yakuza clothes, \n middle age woman wears sunglasses on the middle of\
    the night and always look at you in a wierd way,\n a teenage boy whom\
    seems to have something to hide and goes to the bathroom every 10 minutes")


def play_again():
    choice = input("wanna play again (y/n)?")
    if choice == 'y':
        play_game()
    elif choice == 'n':
        print_pause("GG!")
    else:
        print_pause("Wrong entry detected")
        play_again()


def first_suspect(leads):
    print_pause("You approach the Asian old man.")
    print_pause("He looks at you waiting for you to ask something")
    print_pause("You ask for the purpes of his travel")
    print_pause("He sayes it is for attending comic con show which\
    is just after the arrival time")
    choice = input("Take him into custedy (y/n)?")
    if choice == 'y':
        print_pause("GAME OVER, no enough leads!")
        play_again()
    elif choice == 'n':
        suspects_interaction(leads)
    else:
        print_pause("Wrong entry detected")
        first_suspect(leads)


def second_suspect(leads):
    print_pause("You approach the Middle age woman.")
    print_pause("She starts looking at you with very\
    open eyes and screams asking for help")
    choice = input("Take her into custedy (y/n)?")
    if choice == 'y':
        if "photo" in leads:
            print_pause("You saved the train!")
            play_again()
        else:
            print_pause("GAME OVER, no enough leads!")
            play_again()
    elif choice == 'n':
        suspects_interaction(leads)
    else:
        print_pause("Wrong entry detected")
        second_suspect(leads)


def third_suspect(leads):
    print_pause("You approach the Teenage boy.")
    print_pause("He goes to the bathroom and you follow him")
    print_pause("He looks at you waiting for you to ask something")
    print_pause("You ask for the purpes of his continuos bathroom sessions")
    print_pause("He screems at you and you close his mouth, and ask him\
    agian slowly with a low tune")
    print_pause("He sayes it is for the Middle age woman, and gives you\
    a picture of her persuit which has a bomb in it")
    leads.append("photo")
    choice = input("Take him into custedy (y/n)?")
    if choice == 'y':
        print_pause("GAME OVER, no enough leads!")
        play_again()
    elif choice == 'n':
        suspects_interaction(leads)
    else:
        print_pause("Wrong entry detected")
        third_suspect(leads)


def suspects_interaction(leads):
    print_pause("Please enter the number for the "
                "suspect you would like to talk to:")
    suspect = input("1. Asian old man\n"
                    "2. Middle age woman\n"
                    "3. Teenage boy\n"
                    "4. Random\n")

    if suspect == '1':
        first_suspect(leads)
    elif suspect == '2':
        second_suspect(leads)
    elif suspect == '3':
        third_suspect(leads)
    elif suspect == '4':
        guys = ['1', '2', '3']
        random_guy = random.choice(guys)
        if random_guy == '1':
            first_suspect(leads)
        elif random_guy == '2':
            second_suspect(leads)
        elif random_guy == '3':
            third_suspect(leads)
    else:
        print_pause("Wrong entry detected")
        suspects_interaction(leads)


def play_game():
    leads = []
    intro()
    suspects_interaction(leads)


play_game()
