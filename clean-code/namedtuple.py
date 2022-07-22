# Connect us on Twitter @myrzadev
# Page 1/3

from collections import namedtuple

color = {'red': 55, 'green': 155, 'blue': 255}

print(color['red'])

# Page 2/3

Color = namedtuple('Color', ['red', 'green', 'blue'])

colors = Color(blue=55, green=155, red=255)

print(colors.blue)

# Page 3/3

white_color = Color(255, 255, 255)

print(white_color)
print(white_color.red)
