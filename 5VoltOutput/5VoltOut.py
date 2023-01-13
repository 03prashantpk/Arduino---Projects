from pyfirmata import Arduino, SERVO, OUTPUT, util
import time
import connected

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

value =1
toggleOutputOne(LED_PIN,value)
toggleOutputTWO(BUZZER_PIN,value)


input("Press any Key to continue: ")