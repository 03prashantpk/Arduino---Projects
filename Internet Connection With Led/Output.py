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

workingTime = int(input("How many seconds you want to work? "))

count = 0
while True:
    count +=1

    if count == workingTime +1:
        break
    else:
        if connected.ifConnected() == True:
            value = 1
            print("Online Since: "+ str(count) + " Seconds",end="\r")
            toggleOutputOne(LED_PIN,value)
            time.sleep(0.5)
            value = 0
            toggleOutputOne(LED_PIN,value)
            time.sleep(0.5)

        else:
            value = 1
            print("Offline Since: "+ str(count) + " Seconds",end="\r")
            toggleOutputTWO(BUZZER_PIN,value)
            time.sleep(0.5)
            value = 0
            toggleOutputTWO(BUZZER_PIN,value)
            time.sleep(0.5)
