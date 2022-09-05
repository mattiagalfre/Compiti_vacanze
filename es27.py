#Raindrops

def convert(number):
    str = ""
    if(number % 3 == 0):
        str = str + "Pling"
    if(number % 5 == 0):
        str = str + "Plang"
    if(number % 7 == 0):
        str = str + "Plong"
    if(str == ""):
        str = f"{number}"
    return str
