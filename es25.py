#Armstrong numbers

def is_armstrong_number(number):
    numbers = list(str(number))
    esponent = len(numbers)
    sum = 0
    
    for element in numbers:
        sum = sum + int(element)**esponent
    if(sum == number):
        return True
    else:
        return False
