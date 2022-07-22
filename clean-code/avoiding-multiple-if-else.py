# Connect us on Twitter @myrzadev
# Page 1/2

def blue_function():
    # Execute some code and print color name.
    return "Blue"


def red_function():
    # Execute some code and print color name.
    return "Red"


def green_function():
    # Execute some code and print color name.
    return "Green"
  
# Page 2/2

colors_funcs = {
    "red": red_function(),
    "blue": blue_function(),
    "green": green_function(),
}

colors_funcs.get("red")
