import speech_recognition as sr 

r = sr.Recognizer()
print('How can I help you?')
def my_first_sr():
    while True:
        try:
            with sr.Microphone() as mic:
                r.adjust_for_ambient_noise(mic)
                audio = r.listen(mic)
                text = r.recognize_google(audio, language = 'en-US')

            print(text)

            output = open('Speech Recognition.txt', 'w')
            output.write(text) #Write the text to the file
            output.close()

        except sr.UnknownValueError:
            print('I didn`t understand!')

        except sr.RequestError:
            print('Sorry my service is down')


my_first_sr()