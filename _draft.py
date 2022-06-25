print("You are stuck in a sand ditch.")
print("Crawl out LEFT or RIGHT.")

do = input(":: ")
if do == "LEFT":
    print("You see a STARFISH and a CRAB on the sand.")
    print("And you're hungry! Which do you eat?")

    do = input(":: ")
    if do == "STARFISH":
        print("Oh no! You immediately don't feel well.")
        print("You do not survive :(")

    elif do == "CRAB":
        print("Raw crab should be fine, right? YES or NO.")

        do = input(":: ")
        if do == "YES":
            print("Ok, You eat it raw. Fingers crossed.")
            print("Food in your belly helps you see a TREE.")

            do = input(":: ")
            if do == "TREE":
                print("It's a coconut tree! And you're thirsty!")
                print("Do you drink the coconut water? YES OR NO.")

                do = input(":: ")
                if do == "YES":
                    print("Oh boy. Coconut water and raw crab don't mix.")
                    print("You do not survive :(")

                elif do == "NO":
                    print("Good choice.")
                    print("Look! It's a rescue plane! You made it! \o/")

        elif do == "NO":
            print("Well, there's nothing else left to eat.")
            print("You do not survive :(")

elif do == "RIGHT":
    print("No can do. That side is very slippery.")
    print("You fall very far into some weird cavern.")
    print("You do not survive :(")

pip install pyinstaller
import pyinstaller as pyi
