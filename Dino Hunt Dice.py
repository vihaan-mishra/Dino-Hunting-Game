#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Ask for however many user names and rounds
Set player scores to 0

- 6 green dice: these have dinosaurs on 3 sides, leaves on 2 sides, and a foot on 1 side
- 4 yellow dice: these have dinosaurs on 2 sides, leaves on 2 sides and feet on 2 sides
- 3 red dice: these have dinosaurs on 1 side, leaves on 2 sides, and feet on 3 sides
State remaining dice

On each turn:
- at the start of the turn, all 13 dice are placed into a pile
- the player randomly selects 3 dice and rolls them (if fewer than 3 dice are remaining, the player rolls all the remaining dice)
- any dice showing dinosaurs and feet are set aside; any dice showing leaves are put back into the pile of unrolled dice
- if the player has rolled 3 or more feet during the turn, the player has been stomped: they lose all the dinosaurs captured during the turn and their turn ends.
- the player can stop and score 1 point for each dinosaur captured, or can continue rolling.

die class



'''

import random

class Die:
    '''Die class'''
    def __init__(self, sides=6):
        '''Die(sides)
        creates a new Die object
        int sides is the number of sides
        (default is 6)
        -or- sides is a list/tuple of sides'''
        if isinstance(sides, int):
            self.numSides = sides
            self.sides = list(range(1, sides + 1))
        else:
            self.numSides = len(sides)
            self.sides = list(sides)
        self.roll()

    def __str__(self):
        '''str(Die) -> str
        string representation of Die'''
        return ('A ' + str(self.numSides) + '-sided die with ' + str(self.get_top()) + ' on top')

    def roll(self):
        '''Die.roll()
        rolls the die'''
        self.top = self.sides[random.randrange(self.numSides)]

    def get_top(self):
        '''Die.get_top() -> object
        returns top of Die'''
        return self.top

    def set_top(self, value):
        '''Die.set_top(value)
        sets the top of the Die to value
        Does nothing if value is illegal'''
        if value in self.sides:
            self.top = value

### end Die class ###

class DinoDie(Die):
    def __init__(self, color):
        self.color = color
        if color == 'green':
            sides = ['dino', 'dino', 'dino', 'leaf', 'leaf', 'foot']
        elif color == 'yellow':
            sides = ['dino', 'dino', 'leaf', 'leaf', 'foot', 'foot']
        elif color == 'red':
            sides = ['dino', 'leaf', 'leaf', 'foot', 'foot', 'foot']
        else: 
            raise ValueError("Invalid color choice")
        super().__init__(sides)
        
    def __str__(self):
        return 'A ' + str(self.color) + ' Dino die with a ' + str(self.top) + ' on top.'

    def roll(self):
        self.top = random.choice(self.sides)
        
    def get_top(self):
        return self.top
    
class DinoPlayer:
    '''implements a player of Dino Hunt'''
    def __init__(self, name):
        self.name = name
        self.score = 0
        
    def __str__(self):
        return self.name
                
def play_dino_hunt(numPlayers,numRounds):
    '''play_dino_hunt(numPlayer,numRounds)
    plays a game of Dino Hunt
      numPlayers is the number of players
      numRounds is the number of turns per player'''
    ### you need to add the code ###
    players = []
    for i in range(numPlayers):
        name = input("Player " + str(i + 1)+ ", enter your name: ")
        players.append(DinoPlayer(name))
    for roundNum in range(numRounds):
        for player in players:
            numofDinos = 0
            numofFeet = 0
            print('ROUND ' + str(roundNum + 1))
            print(str(player.name) + ' has ' + str(player.score) + ' points')
            print(str(player.name) + ", it's your turn!")
            numofDie = []
            for i in range(6):
                numofDie.append(DinoDie('green'))
            for i in range(4):
                numofDie.append(DinoDie('yellow'))
            for i in range(3):
                numofDie.append(DinoDie('red'))
            while True:
                input('Press enter to select dice and roll.')

                randomDice = (random.sample(numofDie,3)) #### DRAW
                # looks at every single die out of the 3 die that are chosen 
                for p in randomDice:
                    print(p)
                    # check if it's a dino --> add to score, remove it from the total list 
                    # check if it's a foot --> add to number of feet, remove it from the total list
                    ## check if num of feet is greater than or equal to 3 
                    # check if it's a leaf --> return the dice to the total list 
                    # ask if they want to reroll 
                    if p.get_top() == 'dino':
                        numofDie.remove(p)
                        numofDinos += 1
                        # player.score = numofDinos
                        #print("score: ", score)
                    elif p.get_top() == 'foot':
                        numofDie.remove(p)
                        numofFeet += 1
                        #print("num feet: ", numofFeet)
                    elif p.get_top() == 'leaf':
                        pass
                if numofFeet >= 3:
                    print('Too bad -- you got stomped!')
                    numofDinos = 0
                    break
                print('This turn so far: ' + str(numofDinos) + ' dinos and ' + str(numofFeet) + ' feet')
                print('You have ' + str(len(numofDie)) + ' dice remaining.')
                reroll = input('Do you want to roll again? (y/n)')
                if reroll == 'n':
                    player.score = player.score + numofDinos
                    break
            for p in range(numPlayers):
                print(str(players[p]) + ' has ' + str(players[p].score) + ' points')
    highscore = 0
    winningPlayer = ''
    for i in range(numPlayers):
        if players[i].score > highscore:
            winningPlayer = players[i]
            highscore = players[i].score
    print('We have a winner!')
    print(str(winningPlayer) + ' has ' + str(players[i].score) +  ' points.')

numofPlayers = int(input('How many people are playing: '))
numofRounds = int(input('How many rounds are there: '))
play_dino_hunt(numofPlayers, numofRounds)


# In[ ]:





# In[ ]:




