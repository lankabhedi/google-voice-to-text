# Text/Voice to Morse Signals in Python 3

Making an Python Based API to convert human speech through Google Assistant into Morse Code using Bolt IoT Wi-Fi module and an API

You need to put your API requests in the following format.

```html
http://<website url>/api?api_key=5bbf44a6&device_id=BOLT135&message=<your message>
```

When the code is successfully executed, you will get the following response.

```json
{
    "device_status": "online",
    "message_passed": "yes",
    "morse_code": "<your message> "
}
```

## Hardware Requirements
1. Bolt Wi-Fi Module
2. 330 ohm Resistor
3. Wires
4. Buzzer
5. LED

PS. Software requirements are metioned in the requirements.txt file

## Circuit Diagram

![image](https://user-images.githubusercontent.com/50140975/121958729-963d3100-cd81-11eb-88c0-64bd8aff6146.png)


