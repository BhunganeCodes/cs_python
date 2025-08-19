from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    
    if len(sys.argv) == 1:
        font = random.choice(fonts)
        
    elif len(sys.argv) == 3:
        flag, font = sys.argv[1], sys.argv[2]

        if flag not in ["-f", "--font"]:
            sys.exit("Invalid usage")
        if font not in fonts:
            sys.exit("Font does not exist")
        
    else:
        sys.exit("Invalid usage")
    
    user_input = input("Input: ").strip()
    figlet.setFont(font=font)
    print(f"Output: \n{figlet.renderText(user_input)}")

if __name__ == "__main__":
    main()