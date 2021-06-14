from boltiot import Bolt
import time as t

api_key = "5bbf44a6-01f5-438c-b9ed-617bbcd2cc00"
device_id  = "BOLT13168625"
mybolt = Bolt(api_key, device_id)

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def encrypt(message):
    cipher = ''
    for letter in message.upper():
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '

    return cipher

def main():
    message = "geeks-for-geeks"
    result = encrypt(message.upper())
    print(message.upper())
    print(result)

    for char in result:

        if(char == "-"):
            mybolt.digitalWrite("0", "HIGH")
            t.sleep(3.1)
            mybolt.digitalWrite("0", "LOW")

        elif(char == "."):
            mybolt.digitalWrite("0", "HIGH")
            t.sleep(1.5)
            mybolt.digitalWrite("0", "LOW")

        else:
            mybolt.digitalWrite("1", "HIGH")
            t.sleep(0.5)
            mybolt.digitalWrite("1", "LOW")


if(__name__ == '__main__'):
    main()
