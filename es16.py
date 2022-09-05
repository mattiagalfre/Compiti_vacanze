#Color resistor duo

def value(colors):
    value = ""
    color_code = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", 
                  "grey", "white"]
    index_one = str(color_code.index(colors[0]))
    index_two = str(color_code.index(colors[1]))
    value = index_one + index_two
    return int(value)