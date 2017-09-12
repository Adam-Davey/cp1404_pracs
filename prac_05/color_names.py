COLOR_NAMES = {"turquoise": "#40e0d0", "yellowgreen": "#9acd32", "salmon": "#fa8072", "saddlebrown": "#8b4513"}

color_length = [len(color) for color in COLOR_NAMES]

for color in COLOR_NAMES:
    print("{:{}} is {}".format(color, max(color_length), COLOR_NAMES[color]))

color = input("enter a color").lower()
while color != "":
    if color in COLOR_NAMES:
        print(color, "is", COLOR_NAMES[color])
    else:
        print("invalid color name")
    color = input("enter a color").lower()
