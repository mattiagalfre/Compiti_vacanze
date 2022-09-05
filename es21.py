#Grains

def square(number):
    if(number > 0 and number < 65):
        esponent = number - 1
        grains = 2**esponent
        return grains
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    total_grains = (2**64) - 1
    return total_grains