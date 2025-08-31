import random

class Player:
    def __init__(self, name, playerID):
        self.name = name
        self.playerID = playerID
        self.currentRoll = [0,0,0,0,0]
        self.rollsRemaining = 3
        self.upperScore = 0
        self.lowerScore = 0
        self.totalScore = 0
        self.rounts = 0
        self.scoreCard = {
            'One' : None,
            'Two' : None,
            'Three' : None,
            'Four' : None,
            'Five' : None,
            'Sixe' : None,
            'Three of a Kind' : None,
            'Four of a Kind' : None,
            'Full House' : None,
            'Small Straight' : None,
            'Large Straight' : None,
            'Yahtzee!' : None,
            'Chance' : None,
        }

class Roll:
    def __init__(self, player):
        self.player = player
    
    def roll_dice(self, keptDice=[]):
        for i in range(5):
            if i + 1 not in keptDice:
                self.player.currentRoll[i] = random.randint(1,6)
        self.player.rollsRemaining -= 1
        print(f"{self.player.name} rolled: {self.player.currentRoll}")
    
    def playersTurn(self):
        count = 1
        while self.player.rollsRemaining != 0:
            print("--- Roll " + str(count) + " ---")
            if self.player.rollsRemaining == 3:
                self.roll_dice()
            else:
                keptDice = list(map(int, input("Enter the dice you would like to keep seperated by space: ").split()))
                self.roll_dice(keptDice)
            count += 1
        self.player.rollsRemaining = 3
        count = 1

        print("Which category would you like to score on?")
        for scoreSlot in self.player.scoreCard:
            if self.player.scoreCard[scoreSlot] == None:
                print(scoreSlot)
        
        while True:
            scorePlace = input("Select which category you want to score on: ")
            if scorePlace in self.player.scoreCard and self.player.scoreCard[scorePlace] == None:
                break
            else:
                print("Not a valild scoring position. Please enter a valid option from the list above.")
    
    def 

 
class Scoring:

    def __init__(self, player):
        self.player = player

    def upperBonus(self):
        pass

    def upperSectionTotal(self):
        pass

    def lowerSectionTotal(self):
        pass

    def upperSectionScoring(self, number, scoreCardValue):
        dice = self.player.currentRoll
        scoreCard = self.player.scoreCard
        points = 0
        for die in dice:
            if die == number:
                points += die
        scoreCard[scoreCardValue] = points



    def threeOfAKind(self):
        pass

    def fourOfAKind(self):
        pass

    def fullHouse(self):
        pass

    def straight(self):
        pass

    def yahtzee(self):
        pass

    
players = []
print('Welcome to Yatzee! How many players will there be?')
playerCount = int(input("Enter number of players: "))

# Gets the total number of players and randomizes the order of play
for p in range(1, playerCount + 1):
    player_name = input("Enter player " + str(p) + "'s name: ")
    players.append(Player(player_name, p))

if len(players) > 1:
    print("Here is the order of play.")
    random.shuffle(players)
    for i in players:
        print(i.name)
    print('\n')

# Loop that will run through each players turn and the actions they will take
for i in range(len(players)):
    roll = Roll(players[i])
    scoring = Scoring(players[i])
    roll.playersTurn()
