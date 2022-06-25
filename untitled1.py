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

# Variables that store how many wins and loses you get.
wins = 0
loses = 0

# Here's some space so that you don't ruin the surprise...
































# Displays a message when you win!
def win():
    print('{:*^80}'.format(''))
    print('*{:^78}*'.format(''))
    print('*{:^78}*'.format('You won, you beautiful human.'))
    print('*{:^78}*'.format(''))
    print('{:*^80}'.format(''))

# Displays a message when you lose...
def lose():
    print('{:*^80}'.format(''))
    print('*{:^78}*'.format(''))
    print('*{:^78}*'.format('Dang. You lost.'))
    print('*{:^78}*'.format(''))
    print('{:*^80}'.format(''))

# Displays all the lyrics of "All Star" by Smash Mouth.
def allStar():
    print('{:^120}'.format("Somebody once told me the world is gonna roll me"))
    time.sleep(2)
    print('{:^120}'.format("I ain't the sharpest tool in the shed"))
    time.sleep(2)
    print('{:^120}'.format("She was looking kind of dumb with her finger and her thumb"))
    time.sleep(2)
    print('{:^120}'.format("In the shape of an 'L' on her forehead"))
    time.sleep(2)
    print('{:^120}'.format("Well the years start coming and they don't stop coming"))
    time.sleep(2)
    print('{:^120}'.format("Fed to the rules and I hit the ground running"))
    time.sleep(2)
    print('{:^120}'.format("Didn't make sense not to live for fun"))
    time.sleep(2)
    print('{:^120}'.format("Your brain gets smart but your head gets dumb"))
    time.sleep(2)
    print('{:^120}'.format("So much to do, so much to see"))
    time.sleep(2)
    print('{:^120}'.format("So what's wrong with taking the back streets?"))
    time.sleep(2)
    print('{:^120}'.format("You'll never know if you don't go"))
    time.sleep(2)
    print('{:^120}'.format("You'll never shine if you don't glow"))
    time.sleep(2)
    print('{:^120}'.format("Hey now, you're an all-star, get your game on, go play"))
    time.sleep(2)
    print('{:^120}'.format("Hey now, you're a rock star, get the show on, get paid"))
    time.sleep(2)
    print('{:^120}'.format("And all that glitters is gold"))
    time.sleep(2)
    print('{:^120}'.format("Only shooting stars break the mold"))
    time.sleep(2)
    print('{:^120}'.format("It's a cool place and they say it gets colder"))
    time.sleep(2)
    print('{:^120}'.format("You're bundled up now, wait till you get older"))
    time.sleep(2)
    print('{:^120}'.format("But the meteor men beg to differ"))
    time.sleep(2)
    print('{:^120}'.format("Judging by the hole in the satellite picture"))
    time.sleep(2)
    print('{:^120}'.format("The ice we skate is getting pretty thin"))
    time.sleep(2)
    print('{:^120}'.format("The water's getting warm so you might as well swim"))
    time.sleep(2)
    print('{:^120}'.format("My world's on fire, how about yours?"))
    time.sleep(2)
    print('{:^120}'.format("That's the way I like it and I never get bored"))
    time.sleep(2)
    print('{:^120}'.format("Hey now, you're an all-star, get your game on, go play"))
    time.sleep(2)
    print('{:^120}'.format("Hey now, you're a rock star, get the show on, get paid"))
    time.sleep(2)
    print('{:^120}'.format("All that glitters is gold"))
    time.sleep(2)
    print('{:^120}'.format("Only shooting stars break the mold"))
    time.sleep(2)
    print('{:^120}'.format("Hey now, you're an all-star, get your game on, go play"))
    time.sleep(2)
    print('{:^120}'.format("Hey now, you're a rock star, get the show, on get paid"))
    time.sleep(2)
    print('{:^120}'.format("And all that glitters is gold"))
    time.sleep(2)
    print('{:^120}'.format("Only shooting stars"))
    time.sleep(2)
    print('{:^120}'.format("Somebody once asked could I spare some change for gas?"))
    time.sleep(2)
    print('{:^120}'.format("I need to get myself away from this place"))
    time.sleep(2)
    print('{:^120}'.format("I said yep what a concept"))
    time.sleep(2)
    print('{:^120}'.format("I could use a little fuel myself"))
    time.sleep(2)
    print('{:^120}'.format("And we could all use a little change"))
    time.sleep(2)
    print('{:^120}'.format("Well, the years start coming and they don't stop coming"))
    time.sleep(2)
    print('{:^120}'.format("Fed to the rules and I hit the ground running"))
    time.sleep(2)
    print('{:^120}'.format("Didn't make sense not to live for fun"))
    time.sleep(2)
    print('{:^120}'.format("Your brain gets smart but your head gets dumb"))
    time.sleep(2)
    print('{:^120}'.format("So much to do, so much to see"))
    time.sleep(2)
    print('{:^120}'.format("So what's wrong with taking the back streets?"))
    time.sleep(2)
    print('{:^120}'.format("You'll never know if you don't go (go!)"))
    time.sleep(2)
    print('{:^120}'.format("You'll never shine if you don't glow"))
    time.sleep(2)
    print('{:^120}'.format("Hey now, you're an all-star, get your game on, go play"))
    time.sleep(2)
    print('{:^120}'.format("Hey now, you're a rock star, get the show on, get paid"))
    time.sleep(2)
    print('{:^120}'.format("And all that glitters is gold"))
    time.sleep(2)
    print('{:^120}'.format("Only shooting stars break the mold"))
    time.sleep(2)
    print('{:^120}'.format("And all that glitters is gold"))
    time.sleep(2)
    print('{:^120}'.format("Only shooting stars break the mold"))
    time.sleep(3)

# Return T or F for Y or N (to be used to reassign goOn var).
def cont(yn):
    if yn == 'y':
        return True
    elif yn == 'n':
        return False


# Main program. runs the Choose Your Own Adventure game.

while goOn == True:
    print("IT'S DANGEROUS TO GO ALONE! TAKE THIS.")
    time.sleep(1)
    # Decide between sword and wand
    #while choice == (not ('sword' or 'wand')):
    choice = input('Sword or wand? ').lower()
    if choice == 'sword':
        weapon = 'sword'
        # Decide between left or right.
        print("Good choice! Now what monster do you want to kill?")
        time.sleep(1)
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
                win()
                wins += 1
            elif choice == 'right':
                print('Oh no! An Ogre!')
                time.sleep(1)
                if weapon == 'sword':
                    print('You slice the Ogre.')
                    time.sleep(1)
                    win()
                    wins += 1
                elif weapon != 'sword':
                    print('The Ogre breaks your wand, and then you.')
                    time.sleep(1)
                    lose()
                    loses += 1
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
                    lose()
                    loses += 1
                elif weapon == 'wand':
                    print('You cast a mighty fireball at the Beast!')
                    time.sleep(1)
                    win()
                    wins += 1
                else:
                    print('Pick a valid input!')
                    
            elif choice == 'canyon':
                print('You find a witch\'s hut. She invites you in.')
                time.sleep(1)
                choice = input('Go in or leave? ').lower()
                
                if choice == 'go in':
                    print('She casts a dark spell, puts you in a coma, and then cooks you and eats you.')
                    time.sleep(1)
                    lose()
                    loses += 1
                elif choice == 'leave':
                    print('You leave her hut and stumble around a bit in the desert, eventually dying of starvation.')
                    time.sleep(1)
                    lose()
                    loses += 1
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
                win()
                wins += 1
            elif choice == 'right':
                print('Oh no! An Ogre!')
                time.sleep(1)
                if weapon == 'sword':
                    print('You slice the Ogre.')
                    time.sleep(1)
                    win()
                    wins += 1
                elif weapon != 'sword':
                    print('The Ogre breaks your wand, and then you.')
                    time.sleep(1)
                    lose()
                    loses += 1
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
                    lose()
                    loses += 1
                elif weapon == 'wand':
                    print('You cast a mighty fireball at the Beast!')
                    time.sleep(1)
                    win()
                    wins += 1
                else:
                    print('Pick a valid input!')
                    
            elif choice == 'canyon':
                print('You find a witch\'s hut. She invites you in.')
                time.sleep(1)
                
                choice = input('Go in or leave? ').lower()
                if choice == 'go in':
                    print('She casts a dark spell, puts you in a coma, and then cooks you and eats you.')
                    time.sleep(1)
                    lose()
                    loses += 1
                elif choice == 'leave':
                    print('You leave her hut and stumble around a bit in the desert,eventually dying of starvation.')
                    time.sleep(1)
                    lose()
                    loses += 1
                else:
                    print('Pick a valid input!')
            else:
                    print('Pick a valid input!')
        else:
                    print('Pick a valid input!')
    
    else:
        print('Pick sword or wand next time!')
    time.sleep(3)
    print('You have won {} times.'.format(wins))
    print('You have lost {} times.'.format(loses))
    time.sleep(2)
    decision = input('Do you want to play again? y/n \n')
    goOn = cont(decision)