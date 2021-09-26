#!/usr/bin/python3
# v0.0.1 25.09.2021
# Kerszi (Szikers)
# git - https://github.com/kerszl/demorse
import argparse
import sys
import re

MORSE_CODE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    ".-.-.-": ".",
    "---...": ":",
    "--..--": ",",
    "-.-.-.": ";",
    "..--..": "?",
    "-...-": "=",
    ".----.": "'",
    "-..-.": "/",
    "-.-.--": "!",
    "-....-": "-",
    "..--.-": "_",
    ".-..-.": "\"",
    "-.--.": "(",
    "-.--.-": ")",
    "...-..-": "$",
    ".-...": "&",
    ".--.-.": "@"
}


def get_param():
    # exception for "--" in head of string
    if len(sys.argv) == 3:
        if sys.argv[2] == '--':
            return '--'

    description = """The program converts the morse code to plain text. 
You can throw in some text like this "\\..../.\\.-.. .-..|---".
The program will cut unnecessary characters and convert 
it into plain text like: ".... . .-.. .-.. ---" and
convert it to "hello".

Example: demorse -t ".... . .-.. .-.. ---"
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-t', '--text', type=str, help="Text to decode", default=None, nargs=argparse.REMAINDER)

    args = parser.parse_args()

    if args.text:
        return str(args.text)
    else:
        parser.print_help()
        return None


def decode_morse_code(pure_morse_code_2_decode):
    decode_string = ""
    morse_string = " ".join(pure_morse_code_2_decode)
    for i in pure_morse_code_2_decode:
        decode_string += MORSE_CODE.get(i, '')
    if len(decode_string) > 0:
        return morse_string, decode_string
    else:
        return None


def leave_plain_text(morse_string_code):
    # Clean from unnecessary signs
    chars = re.findall('[.]|-| ', morse_string_code, re.DOTALL)
    decode_morse_string = ''.join(chars)

    # return string2list
    if len(decode_morse_string) > 0:
        return decode_morse_string.split(' ')
    else:
        return None


# ----


def just_decode(text_to_decode):
    if text_to_decode:
        pure_text = leave_plain_text(text_to_decode)
        if pure_text:
            morse_string, decode_morse_string = decode_morse_code(pure_text)
            if decode_morse_string:
                print("Morse   :", morse_string)
                print("Demorse :", decode_morse_string)
            else:
                print("No real morse code")
        else:
            print("Nothing to decode")


if __name__ == '__main__':
    text2decode = get_param()
    just_decode(text2decode)
