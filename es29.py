#Difference of squares

def square_of_sum(number):
    total = 0
    sum = 0
    for k in range(1, number + 1):
        sum = sum + k
    total = sum**2
    return total


def sum_of_squares(number):
    total = 0
    for k in range(1, number + 1):
        total = total + k**2
    return total


def difference_of_squares(number):
    squareOS = square_of_sum(number)
    sumOS = sum_of_squares(number)
    difference = squareOS - sumOS
    return difference