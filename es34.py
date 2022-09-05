#Callatz conjecture

def steps(number):
    tot = 0

    if(number < 1):
        raise ValueError("Only positive integers are allowed")

    while(number > 1):
        if(number % 2 == 0):
            number = number // 2
            tot = tot + 1
        else:
            number = (3 * number) + 1
            tot = tot + 1
    return tot