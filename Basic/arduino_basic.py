from pyfirmata import Arduino, SERVO, OUTPUT, util
import time

port = "COM6"
led = 12
board = Arduino(port)
board.digital[led].mode = OUTPUT
buzzer = 10
buzzer = board.get_pin(f'd:{buzzer}:o')

def finalOutput(pin,value):
    board.digital[led].write(value)


def blink(led):
    count = 0
    while True:
        count +=1

        for i in range(1,101):
            if i % 2 != 0:
                value = 1
                finalOutput(led,value)
                buzzer.write(0)
                time.sleep(0.001)
            else:
                value = 0
                finalOutput(led,value)
                buzzer.write(1)
                time.sleep(0.002)
# blink(led)

def blink2():
    count = 0
    while True:
        count +=1
        print(count,end="")

        if count == 101:
            buzzer.write(1)
            break

        for i in range(1,101):
            if i % 3 == 0:
                buzzer.write(1)
                time.sleep(1)
            elif i % 5 == 0:
                buzzer.write(0)
                time.sleep(0.4)
            else:
                buzzer.write(0)
                time.sleep(0.01)

# blink2()
            

for i in range(1,51):
    if i % 2 == 0:
        blink(led)
        time.sleep(5)
    else:
        blink2()
        time.sleep(9)
