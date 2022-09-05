#Yacht

# Score categories.
# Change the values as you see fit.
YACHT = None
ONES = None
TWOS = None
THREES = None
FOURS = None
FIVES = None
SIXES = None
FULL_HOUSE = None
FOUR_OF_A_KIND = None
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None


def score(dice, category):
    score = 0
    counter = 0
    
    if(category == YACHT):
        if(dice[0] == dice[1] and dice[0] == dice[2] and dice[0] == dice[3] and dice[0] == dice[4]):
            score = 50
            #YACHT = score
        return score
    elif(category == ONES):
        for k in range(5):
            if(dice[k] == 1):
                score = score + 1
        #ONES = score
        return score
    elif(category == TWOS):
        for k in range(5):
            if(dice[k] == 2):
                counter = counter + 1
        score = 2 * counter
        #TWOS = score
        return score
    elif(category == THREES):
        for k in range(5):
            if(dice[k] == 3):
                counter = counter + 1
        score = 3 * counter
        #THREES = score
        return score
    elif(category == FOURS):
        for k in range(5):
            if(dice[k] == 4):
                counter = counter + 1
        score = 4 * counter
        #FOURS = score
        return score
    elif(category == FIVES):
        for k in range(5):
            if(dice[k] == 5):
                counter = counter + 1
        score = 5 * counter
        #FIVES = score
        return score
    elif(category == SIXES):
        for k in range(5):
            if(dice[k] == 6):
                counter = counter + 1
        score = 6 * counter
        #SIXS = score
        return score
    elif(category == LITTLE_STRAIGHT):
        ok = False
        if(dice[0] == 1):
            ok = True
            for k in range(4):
                if(ok == True and dice[k+1] == (k+2)):
                    ok = True
                else:
                    ok = False
            if(ok == True):
                score = 30
        #LITTLE_STRAIGHT = score
        return score
    elif(category == BIG_STRAIGHT):
        ok = False
        if(dice[0] == 2):
            ok = True
            for k in range(4):
                if(ok == True and dice[k+1] == (k+3)):
                    ok = True
                else:
                    ok = False
            if(ok == True):
                score = 30
        #BIG_STRAIGHT = score
        return score
    elif(category == CHOICE):
        for k in range(5):
            score = score + dice[k]
        #CHOICE = score
        return score
    elif(category == FOUR_OF_A_KIND):
        counter = [0, 0, 0, 0, 0, 0]
        for k in range(5):
            if(dice[k] == 1):
                counter[0] = counter[0] + 1
            elif(dice[k] == 2):
                counter[1] = counter[0] + 1
            elif(dice[k] == 3):
                counter[2] = counter[0] + 1
            elif(dice[k] == 4):
                counter[3] = counter[0] + 1
            elif(dice[k] == 5):
                counter[4] = counter[0] + 1
            elif(dice[k] == 6):
                counter[5] = counter[0] + 1

        for k in range(5):
            if(counter[k] == 4):
                score = (k+1) * 4
        #FOUR_OF_A_KIND = score
        return score
    elif(category == FULL_HOUSE):
        counter = [0, 0, 0, 0, 0, 0]
        for k in range(5):
            if(dice[k] == 1):
                counter[0] = counter[0] + 1
            elif(dice[k] == 2):
                counter[1] = counter[0] + 1
            elif(dice[k] == 3):
                counter[2] = counter[0] + 1
            elif(dice[k] == 4):
                counter[3] = counter[0] + 1
            elif(dice[k] == 5):
                counter[4] = counter[0] + 1
            elif(dice[k] == 6):
                counter[5] = counter[0] + 1

        for k in range(5):
            if(counter[k] == 3):
                for k in range(5):
                    if(counter[k] == 2): 
                        for k in range(5):
                            score = score + dice[k]
        #FULL_HOUSE = score
        return score
            
            
    
