from pyfirmata import Arduino, SERVO, OUTPUT, util
import keyboard

port = "COM6"
LED_PIN = 12
BUZZER_PIN = 10
board = Arduino(port)
board.digital[LED_PIN].mode = OUTPUT
board.digital[BUZZER_PIN].mode = OUTPUT


def toggleOutputOne(LED_PIN,value):
    board.digital[LED_PIN].write(value)

def toggleOutputTWO(BUZZER_PIN,value):
    board.digital[BUZZER_PIN].write(value)

record = 0
while True:
    record += 1
    print(keyboard.read_key()[0].replace(keyboard.read_key()[0], " "),end="\r", flush=True)
    
    if keyboard.read_key() == "insert":
        if record % 2 == 0:
            value = 0
            toggleOutputOne(LED_PIN,value)
            # toggleOutputTWO(BUZZER_PIN,value)
        else:
            value = 1
            toggleOutputOne(LED_PIN,value)
            # toggleOutputTWO(BUZZER_PIN,value)



#### Instructions  ####
# Press (Insert Key) 2 time/Once to Turn ON LED
# Press (Insert Key) 1 time/Twice to Turn OFF LED
