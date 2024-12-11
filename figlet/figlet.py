from pyfiglet import Figlet
import sys
import random

font_is_random = False

if len(sys.argv) == 1:
    font_is_random = True
elif len(sys.argv) == 3:
    font_is_random = False
    if (sys.argv[1] != "-f" and sys.argv[1] != "--font"):
        sys.exit("Second command-line argument is incorrect")
else:
    sys.exit("No right use of command-line arguments")



figlet = Figlet()

available_fonts = figlet.getFonts()

if font_is_random == True:
    figlet.setFont(font = random.choice(available_fonts))
    text = input("Give me a text: ")
    print(figlet.renderText(text))

elif font_is_random == False and sys.argv[2] not in available_fonts:
    sys.exit("Font is not available")

else:
    figlet.setFont(font=(sys.argv[2]))
    text = input("Give me a text: ")
    print(figlet.renderText(text))
