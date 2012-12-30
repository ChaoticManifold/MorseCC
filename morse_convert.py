# A program to convert strings to their morse code equivilent 
# and create and play a .wav file of that morse code message.

import os
import wave

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

        if letter in morse_table:
            conv_string += morse_table[letter]  

        else:
            print "\nWARNING: '%s' has no morse code equivilent." % letter
            print "\t A pause will be added to the .wav at this character's position."
            print "\t Use only the 26 letters (a -> z) and 10 numbers (0 -> 9)\n"
            conv_string += morse_table[' ']

    print "Morse Code> " + conv_string

    sound(conv_string)


def sound(morse_string):   # Creates and plays .wav of your message in morse code.

    long_sound = wave.open("morse_long.wav", 'r')
    short_sound = wave.open("morse_short.wav", 'r')
    silent = wave.open("morse_pause.wav", 'r')
    full_sound = wave.open("full_morse.wav", 'w')

    full_sound.setparams(long_sound.getparams())

    for char in morse_string:

        if '_' == char:
            full_sound.writeframes(long_sound.readframes(long_sound.getnframes()))
            long_sound.rewind()

        elif '.' == char:
            full_sound.writeframes(short_sound.readframes(short_sound.getnframes()))
            short_sound.rewind()

        else:
            full_sound.writeframes(silent.readframes(silent.getnframes()))
            silent.rewind()

    long_sound.close()
    short_sound.close()
    silent.close()
    full_sound.close()

    os.system("aplay full_morse.wav")


main()
