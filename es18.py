#Isogram

def is_isogram(string):
    string_only_letters = [k for k in string.lower() if k.isalpha()]
    right_string = set(string_only_letters)
    if(len(right_string) == len(string_only_letters)):
        return True
    else:
        return False