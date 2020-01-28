import random

print("Welcome to Yahtzee!")
print()
print("RULES:\n""- To save a die use 1-5 in the order they apper on the screen\n"\
      "- When it is time to score type out the catigory you would like\n")
print("-" * 65)
print()
def main():
    scoreSheet = {"one": None, "two": None, "three": None, "four": None, "five": None, "six": None, "threeOfKind": None,\
                  "fourOfKind": None, "small": None, "large": None, "fullHouse": None, "yahtzee": None, "chance": None}
    count = 0
    while count < 13:
        diceValues = diceRoll()
        placePoints(diceValues,scoreSheet)
        count += 1
    score(scoreSheet)
    
def diceRoll():
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0
    count = 0
    savedDie = []
    diceValues = []
##    ### ADD REMOVE OPTION AFTER SECOND ROLL
    while count < 3:
        if "1" not in savedDie:
            d1 = random.randint(1,6)
        if "2" not in savedDie:
            d2 = random.randint(1,6)
        if "3" not in savedDie:
            d3 = random.randint(1,6)
        if "4" not in savedDie:
            d4 = random.randint(1,6)
        if "5" not in savedDie:
            d5 = random.randint(1,6)
        savedDie = []
        print(d1,d2,d3,d4,d5)
##        print("Dice 1: '{}'  Dice 2: '{}'  Dice 3: '{}' "\
##              "Dice 4: '{}' Dice 5: '{}'".format(d1,d2,d3,d4,d5))
        print()

        if count != 2:
##            repeat = False
            while True:
                try:
                    keep = int(input("How many die would you like to keep? "))
                    print()
                except ValueError:
                    print("Please pick a number")
                    continue
                else:
                    break
            while keep > 0:
                if keep == 5:
                    savedDie.append("1")
                    savedDie.append("2")
                    savedDie.append("3")
                    savedDie.append("4")
                    savedDie.append("5")
                    keep -= 5
                else:
                    save = input("Enter a die you would like to save: ")
                    savedDie.append(save)
                    keep -= 1
        print()
        count += 1
    diceValues.append(d1)
    diceValues.append(d2)
    diceValues.append(d3)
    diceValues.append(d4)
    diceValues.append(d5)
    
    print("-" * 50)
    return diceValues


def placePoints(diceValues,sheet):
##    while True:
    print("Upper Half:")
    if sheet.get("one") == None:
        print("one")
    if sheet.get("two") == None:
        print("two")
    if sheet.get("three") == None:
        print("three")
    if sheet.get("four") == None:
        print("four")
    if sheet.get("five") == None:
        print("five")
    if sheet.get("six") == None:
        print("six")
    print()
    print("Lower Half:")
    if sheet.get("threeOfKind") == None:
        print("Three of a Kind")
    if sheet.get("fourOfKind") == None:
        print("Four of a Kind")
    if sheet.get("small") == None:
        print("Small Straight")
    if sheet.get("large") == None:
        print("Large Straingt")
    if sheet.get("fullHouse") == None:
        print("Full House")
    if sheet.get("yahtzee") == None:
        print("Yahtzee")
    if sheet.get("chance") == None:
        print("Chance")
    print()
    choice = input("Pick which catagory you would like to score: ")
    calculatePoints(choice,diceValues,sheet)
        
    
def calculatePoints(choice,dice,sheet):
    diceValues = [1,2,3,4,5,6]
    pick = False
    while pick != True:
        #Upper Half
        if choice == "one":
            oneTotal = 0
            for roll in dice:
                if roll == 1:
                    oneTotal += 1
            sheet["one"] = oneTotal
            pick = True
            
        elif choice == "two":
            twoTotal = 0
            for roll in dice:
                if roll == 2:
                    twoTotal += 2
            sheet["two"] = twoTotal
            pick = True

        elif choice == "three":
            threeTotal = 0
            for roll in dice:
                if roll == 3:
                    threeTotal += 3
            sheet["three"] = threeTotal
            pick = True

        elif choice == "four":
            fourTotal = 0
            for roll in dice:
                if roll == 4:
                    fourTotal += 4
            sheet["four"] = fourTotal
            pick = True

        elif choice == "five":
            fiveTotal = 0
            for roll in dice:
                if roll == 5:
                    fiveTotal += 5
            sheet["five"] = fiveTotal
            pick = True

        elif choice == "six":
            sixTotal = 0
            for roll in dice:
                if roll == 6:
                    sixTotal += 6
            sheet["six"] = sixTotal
            pick = True
            
        #Lower half
        elif choice == "three of a kind":
            threeOfKindTotal = 0
            count = 0
            for face in diceValues:
                for roll in dice:
                    if face == roll:
                        count += 1
                if count >= 3:
                    threeOfKindTotal = sum(dice)
                    break
                else:
                    count = 0
            sheet["threeOfKind"] = threeOfKindTotal
            pick = True

        elif choice == "four of a kind":
            fourOfKindTotal = 0
            count = 0
            for face in diceValues:
                for roll in dice:
                    if face == roll:
                        count += 1
                if count >= 4:
                    fourOfKindTotal = sum(dice)
                    break
                else:
                    count = 0
            sheet["fourOfKind"] = fourOfKindTotal
            pick = True
            
        elif choice == "small straight":
            smallStraightTotal = 0
            dice.sort()
            count = 0
            newValue = dice[0] 

            for face in diceValues:
                for roll in dice:
                    if roll == face:
                        if face == roll and roll == newValue:
                            newValue = face + 1
                            count += 1
                            break
            if count >= 4:
                smallStraightTotal = 30
            else:
                smallStraightTotal = 0
            sheet["small"] = smallStraightTotal
            pick = True

        elif choice == "large straight":
            largeStraightTotal = 0
            dice.sort()
            count = 0
            newValue = dice[0] 

            for face in diceValues:
                for roll in dice:
                    if roll == face:
                        if face == roll and roll == newValue:
                            newValue = face + 1
                            count += 1
                            break
            if count == 5:
                largeStraightTotal = 40
            else:
                largeStraightTotal = 0
            sheet["large"] = largeStraightTotal
            pick = True

        elif choice == "full house":
            fullHouseTotal = 0
            dice.sort()
            highCount = 0
            lowCount = 0

            for roll in dice:
                if roll == dice[0]:
                    highCount += 1
                if roll == dice[-1]:
                    lowCount += 1
            if highCount == 3 and lowCount == 2 or lowCount == 3 and highCount == 2:
                fullHouseTotal = 25
            sheet["fullHouse"] = fullHouseTotal
            pick = True

        elif choice == "yahtzee":
            yahtzeeTotal = 0
            if dice[0] and dice[1] == dice[0] and dice[2] == dice[0] and dice[3] == dice[0] and dice[4] == dice[0]:
                yahtzeeTotal = 50
            sheet["yahtzee"] = yahtzeeTotal
            pick = True
        
        elif choice == "chance":
            chance = dice[0] + dice[1] +dice[2] + dice[3] + dice[4]
            sheet["chance"] = chance
            pick = True
            
        else:
            choice = input("Pick whice catagory you would like to score: ")
        
    print()

def score(diceValues):
    ## place all values in dictionary into list, sum list
    totalList = []
    upperList = []
    for key, value in diceValues.items():
        if value != None:
            if key == "one" or key == "two" or key == "three" \
               or key == "four" or key == "five" or key == "six":
                upperList.append(value)
            else:
                totalList.append(value)
    upper = sum(upperList)
    if upper >= 63:
        upper += 35
    totalList.append(upper)
    gameTotal = sum(totalList)
    print(gameTotal)

main()
