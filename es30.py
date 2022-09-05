#Flatten array

def flatten(iterable):
    result = []
    
    for k in iterable:
        if type(k) is list or type(k) is tuple:
            result.extend(flatten(k))
        elif k is not None:
            result.append(k)
    return result