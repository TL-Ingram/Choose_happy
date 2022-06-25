# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 13:54:51 2022

@author: ingram_t
"""

"""
Author: Adam Ricks

Description:
  Runs a Choose Your Own Adventure game, forcing you to choose a weapon, and
  then running you through a series of other choices.
"""

import time

# Variable that decides whether the game will run again or not.
goOn = True

# Variables that store how many end_ones and end_twos you get.
end_ones = 0
end_twos = 0

# Here's some space so that you don't ruin the surprise...
































# Displays a message when you end_one!
def end_one():
    print('{:*^80}'.format(''))
    print('*{:^78}*'.format(''))
    print('*{:^78}*'.format('You survived'))
    print('*{:^78}*'.format(''))
    print('{:*^80}'.format(''))

# Displays a message when you end_two...
def end_two():
    print('{:*^80}'.format(''))
    print('*{:^78}*'.format(''))
    print('*{:^78}*'.format('You did not survive'))
    print('*{:^78}*'.format(''))
    print('{:*^80}'.format(''))

# Displays all the lyrics of "All Star" by Smash Mouth.
def allStar():
    print('{:^120}'.format("Somebody once told me the world is gonna roll me"))
    time.sleep(2)
    print('{:^120}'.format("I ain't the sharpest tool in the shed"))
    time.sleep(2)


# Return T or F for Y or N (to be used to reassign goOn var).
def cont(yn):
    if yn == 'y':
        return True
    elif yn == 'n':
        return False


# Main program. runs the Choose Your Own Adventure game.

while goOn == True:
    print("You stumble on a loose rock")
    time.sleep(3)
    print("The noise echos off the cave wall")
    time.sleep(6)
    print("You hear indistinct voices from deeper in the cavern...")
    time.sleep(5)
    print("{:^120}".format("...they're getting louder"))
    time.sleep(3)
    print("You look down at your waistbelt")
    time.sleep(2.5)
    # Decide between sword and wand
    #while choice == (not ('sword' or 'wand')):
    choice = input('Unsheath sword or look back up? ').lower()
    if choice == 'sword' or 'unsheath sword':
        weapon = 'sword'
        # Decide between sword or unarmed.
        print("The weight of the sword in your hand feels natural")
        time.sleep(2)
        print("You can make out ")
        choice = input('Ogre or Beast? ').lower()
        if choice == 'ogre':
            print("You've reached the swamp!")
            time.sleep(1)
            choice = input('Left or Right? ').lower()
            
            if choice == 'left':
                print('{}'.format("You come up on a little hut in the middle of the swamp."))
                time.sleep(3)
                print('{}'.format("Suddenly, you hear footsteps behind you."))
                time.sleep(3)
                print('{}'.format("Startled, you turn around, and then hear:"))
                time.sleep(3)
                allStar()
                time.sleep(3)
                end_one()
                end_ones += 1
            elif choice == 'right':
                print('Oh no! An Ogre!')
                time.sleep(1)
                if weapon == 'sword':
                    print('You slice the Ogre.')
                    time.sleep(1)
                    end_one()
                    end_ones += 1
                elif weapon != 'sword':
                    print('The Ogre breaks your wand, and then you.')
                    time.sleep(1)
                    end_two()
                    end_twos += 1
                else:
                    print('Pick a valid input!')
        # Decide between dunes or canyon.
        elif choice == 'beast':
            print("You've reached the desert!")
            time.sleep(1)
            choice = input('Dunes or canyon? ').lower()
            
            if choice == 'dunes':
                print("You stumble upon the Beast!")
                time.sleep(1)
                if weapon == 'sword':
                    print('The Beast eats your sword, and then you.')
                    time.sleep(1)
                    end_two()
                    end_twos += 1
                elif weapon == 'wand':
                    print('You cast a mighty fireball at the Beast!')
                    time.sleep(1)
                    end_one()
                    end_ones += 1
                else:
                    print('Pick a valid input!')
                    
            elif choice == 'canyon':
                print('You find a witch\'s hut. She invites you in.')
                time.sleep(1)
                choice = input('Go in or leave? ').lower()
                
                if choice == 'go in':
                    print('She casts a dark spell, puts you in a coma, and then cooks you and eats you.')
                    time.sleep(1)
                    end_two()
                    end_twos += 1
                elif choice == 'leave':
                    print('You leave her hut and stumble around a bit in the desert, eventually dying of starvation.')
                    time.sleep(1)
                    end_two()
                    end_twos += 1
                else:
                    print('Pick a valid input!')
            else:
                    print('Pick a valid input!')
        else:
                    print('Pick a valid input!')
                
    elif choice == 'wand':
        weapon = 'wand'
        print("Good choice! What place do you want to go now?")
        time.sleep(1)
        choice = input('Swamp or Desert? ').lower()
        
        if choice == 'swamp':
            print("You've reached the swamp!")
            time.sleep(1)
            choice = input('Left or Right? ').lower()
            
            if choice == 'left':
                print('{}'.format("You come up on a little hut in the middle of the swamp."))
                time.sleep(3)
                print('{}'.format("Suddenly, you hear footsteps behind you."))
                time.sleep(3)
                print('{}'.format("Startled, you turn around, and then hear:"))
                time.sleep(3)
                allStar()
                time.sleep(3)
                end_one()
                end_ones += 1
            elif choice == 'right':
                print('Oh no! An Ogre!')
                time.sleep(1)
                if weapon == 'sword':
                    print('You slice the Ogre.')
                    time.sleep(1)
                    end_one()
                    end_ones += 1
                elif weapon != 'sword':
                    print('The Ogre breaks your wand, and then you.')
                    time.sleep(1)
                    end_two()
                    end_twos += 1
                else:
                    print('Pick a valid input!')
            else:
                    print('Pick a valid input!')
                
        elif choice == 'desert':
            print("You've reached the desert!")
            time.sleep(1)
            choice = input('Dunes or canyon? ').lower()
            
            if choice == 'dunes':
                print("You stumble upon the Beast!")
                time.sleep(1)
                if weapon == 'sword':
                    print('The Beast eats your sword, and then you.')
                    time.sleep(1)
                    end_two()
                    end_twos += 1
                elif weapon == 'wand':
                    print('You cast a mighty fireball at the Beast!')
                    time.sleep(1)
                    end_one()
                    end_ones += 1
                else:
                    print('Pick a valid input!')
                    
            elif choice == 'canyon':
                print('You find a witch\'s hut. She invites you in.')
                time.sleep(1)
                
                choice = input('Go in or leave? ').lower()
                if choice == 'go in':
                    print('She casts a dark spell, puts you in a coma, and then cooks you and eats you.')
                    time.sleep(1)
                    end_two()
                    end_twos += 1
                elif choice == 'leave':
                    print('You leave her hut and stumble around a bit in the desert,eventually dying of starvation.')
                    time.sleep(1)
                    end_two()
                    end_twos += 1
                else:
                    print('Pick a valid input!')
            else:
                    print('Pick a valid input!')
        else:
                    print('Pick a valid input!')
    
    else:
        print('Pick sword or wand next time!')
    time.sleep(3)
    decision = input('Do you want to play again? y/n \n')
    goOn = cont(decision)