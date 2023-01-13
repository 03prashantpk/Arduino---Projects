import speech_recognition as sr
from pyfirmata import Arduino, SERVO, OUTPUT, util
from time import sleep
import time
from gtts import gTTS
from playsound import playsound
import urllib.request

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

port = "COM6"
led = 12
buzzer = 10
analoginput = 0
board = Arduino(port)

board.digital[led].mode =OUTPUT
analog_input = board.get_pin(f'a:{analoginput}:i')
buzzer = board.get_pin(f'd:{buzzer}:o')

it = util.Iterator(board)
it.start()  

def voiceOutput(text_value):
    language='en'
    obj=gTTS(text=text_value,lang=language,slow=False,tld='com')
    obj.save("exam.mp3")
    time.sleep(2)
    playsound("exam.mp3")
                    
def finalOutput(led,value):
    board.digital[led].write(value)

def temperature():
    count = 0
    while True:
        count +=1
        if count == 50:
            voiceControl()
        time.sleep(0.9)

        analog_value = analog_input.read()
        if analog_value is not None:
            temp = float(5.0*100)*float(analog_value)
            temp = round(temp,3)
            str(temp)
            formatedTemp = str(temp)+"°C"

            if temp >= 15.00 and temp < 25:
                buzzer.write(0)
                print(f"\n{formatedTemp} Low Temperature")
              
                for i in range(1,51):
                    if i % 4 == 0:
                        buzzer.write(1)
                        finalOutput(led,1)
                        time.sleep(0.005)
                    else:
                        buzzer.write(0)
                        finalOutput(led,0)
            
            elif temp >= 25:
                buzzer.write(0)
                print(f"\n{formatedTemp} Very Temperature")
                for i in range(1,60):
                    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
                        buzzer.write(1)
                        finalOutput(led,1)
                        time.sleep(0.025)
                    else:
                        buzzer.write(0)
                        finalOutput(led,0)

        else:
            print(f"\nNormal {formatedTemp}")
            buzzer.write(0)
            finalOutput(led,0)


def blink(led):
    count = 0
    while True:
        count +=1
        if count == 50:
            voiceControl()
        time.sleep(0.15)

        for i in range(1,101):
            if i % 2 != 0:
                value = 1
                finalOutput(led,value)
                time.sleep(0.001)
            else:
                value = 0
                finalOutput(led,value)

def open_links(link):
    webUrl = urllib.request.urlopen(link)
    print("opening...")
    time.sleep(2)

def voiceControl():
    print("\nVoice Control Active\n")
    with mic as source:
        r.adjust_for_ambient_noise(source)
        while True:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language = 'en-US')
                print(text)
                if text == "switch on" or text == "turn on" or text == "led" or text == "LED":
                    value = 1
                    text_value = "Turning on LED"
                    voiceOutput(text_value)
                    time.sleep(2)
                    finalOutput(led,value)
                
                elif text == "switch Off" or text == "turn off" or text == "turn of" :
                    value = 0
                    text_value = "Turning OFF LED"
                    voiceOutput(text_value)
                    finalOutput(led,value)
                
                elif text == "read temperature" or text == "readtemperature" or text == "temperature":
                    text_value = "Reading Temperature"
                    voiceOutput(text_value)
                    temperature()
                    buzzer.write(0)
                
                elif text == "three" or text == "3" or text == "buzzer":
                    buzzer.write(1)
                
                elif text == "off" or text == "4" or text == "four" or text == "stop" or text == "top":
                    buzzer.write(0)

                elif text == "linkedin" or text == "profile" or text == "open linkedin" or text == "browse linkedin":
                    link = "https://www.linkedin.com/in/03prashantpk/"
                    open_links(link)
                    time.sleep(2)
                
                elif text == "blink":
                    text_value = "LED is Blinking"
                    blink(led)
                    time.sleep(2)

                else:
                    print("Say Again Please!")
            
            except:
                print("Listening...")

voiceControl()