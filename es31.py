#Perfect numbers

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if(number < 1):
        raise ValueError("Classification is only possible for positive integers.")

    divisors = []
    for k in range(1, int(number//2) + 1):
        if(number % k == 0):
            divisors.append(k)
    aliquot_sum = sum(divisors)

    type = ""
    if(aliquot_sum == number):
        type = "perfect"
    elif(aliquot_sum > number):
        type = "abundant"
    elif(aliquot_sum < number):
        type = "deficient"
    return type
