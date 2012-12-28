# A program to convert strings to morse code.

import os

def main():
    
    morse_table = { 'a' : '._', 'b' : '_...', 'c' : '_._.', 'd' : '_..', 'e' : '.', 'f' : '.._.',
                    'g' : '__.', 'h' : '....', 'i' : '..', 'j' : '.___', 'k' : '_._', 'l' : '._..',
                    'm' : '__', 'n' : '_.', 'o' : '___', 'p' : '.__.', 'q' : '__._', 'r' : '._.',
                    's' : '...', 't' : '_', 'u' : '.._', 'v' : '..._', 'w' : '.__', 'x' : '_.._',
                    'y' : '_.__', 'z' : '__..', ' ' : ' ', '1' : '.____', '2' : '..___',
                    '3' : '...__', '4': '...._', '5' : '.....', '6' : '_....', '7' : '__...',
                    '8' : '___..', '9' : '____.', '0' : '_____' }

    string = raw_input("Message> ").lower()
    conv_string = ""

    for letter in string:
        conv_string += morse_table[letter]

    print conv_string

    for l in conv_string:
        if '_' == l:
            os.system("aplay morse_long.wav")
        elif '.' == l:
            os.system("aplay morse_short.wav")
        else:
            pass

main()
