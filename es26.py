#Darts

from math import sqrt

def score(x, y):
    radius = sqrt(x**2 + y**2)
    score = 0
    
    if(radius <= 1):
        score = 10
    elif(radius <= 5):
        score = 5
    elif(radius <= 10):
        score = 1
    else:
        score = 0
    return score
