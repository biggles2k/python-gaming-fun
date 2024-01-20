import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you you see two caves. In one cave the dragon is friendly and will share its treasure with you. The other dragon is greedy and hungry, and will eat you on sight.''')
    print()
    
def chooseCave():
    cave = '0'
    while cave != '1' and cave != '2':
        print('Which cave will you go into (1 or 2)?')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! It opens its jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)
    if chosenCave == str(friendlyCave):
        print('Gives you its treasure!')
    else:
        print('Gobbles you up in one bite!')

playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    
    print()
    print('Would you like to play again?')
    playAgain = input()