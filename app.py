from flask import Flask, jsonify, render_template, request
from boltiot import Bolt
import time as t

app = Flask(__name__, template_folder="templates/")

@app.route('/', methods = ['GET','POST'])
def mainpage():
    return "Hello World!"
    """
    if request.method == 'POST':
        device_id = request.form['device_id']
        api_key = request.form['api_key']
        message = request.form['message']

        morsed = encrypt(message)
        mybolt = Bolt(api_key, device_id)

        if mybolt.isAlive() == '{"value": "alive", "success": 1}':
            morse(message, api_key, device_id)
            return(render_template('success.html',morsed = morsed))
        else:
            return((render_template('deviceoffline.html')))
            """




    else:
        return (render_template('index.html'))


@app.route('/api', methods = ['GET'])
def morserApi():
    if request.method == 'GET':
        api_key = request.args.get('api_key')
        device_id = request.args.get('device_id')
        message = request.args.get('message')

        morsed = encrypt(message)
        mybolt = Bolt(api_key, device_id)

        if mybolt.isAlive() == '{"value": "alive", "success": 1}':
            morse(message, api_key, device_id)
            return jsonify(
                device_status="online",
                message_passed="yes",
                morse_code=morsed
            )
        else:
            return jsonify(
                device_status = "offline",
                message_passed = "no",
                morse_code = ""
            )

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

def morse(message, api_key, device_id):
    mybolt = Bolt(api_key, device_id)
    result = encrypt(message.upper())

    mybolt.digitalWrite("1", "LOW")
    mybolt.digitalWrite("1", "HIGH")
    t.sleep(0.01)
    mybolt.digitalWrite("1", "LOW")
    mybolt.digitalWrite("1", "HIGH")
    t.sleep(0.01)
    mybolt.digitalWrite("1", "LOW")
    mybolt.digitalWrite("1", "HIGH")
    t.sleep(0.01)
    mybolt.digitalWrite("1", "LOW")
    mybolt.digitalWrite("1", "HIGH")
    t.sleep(0.01)
    mybolt.digitalWrite("1","LOW")

    for char in result:

        if(char == "-"):
            mybolt.digitalWrite("0", "LOW")
            mybolt.digitalWrite("0", "HIGH")
            t.sleep(3)
            mybolt.digitalWrite("0", "LOW")

        elif(char == "."):
            mybolt.digitalWrite("0", "LOW")
            mybolt.digitalWrite("0", "HIGH")
            t.sleep(1)
            mybolt.digitalWrite("0", "LOW")

        elif(char == " "):
            mybolt.digitalWrite("1", "LOW")
            mybolt.digitalWrite("1", "HIGH")
            t.sleep(0.2)
            mybolt.digitalWrite("1", "LOW")
            t.sleep(0.1)

        else:
            continue

    return (result, "SUCCESS")




if __name__ == '__main__':
    app.run(debug=True)

