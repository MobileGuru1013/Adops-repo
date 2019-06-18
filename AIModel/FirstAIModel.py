import speech_recognition as sr
from gtts import gTTS
import os
import speak
import webbrowser as wb

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


for x in range(1, 50):
    # get audio from that microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak")
        audio = r.listen(source)

    try:
        if r.recognize_google(audio) == "who are you":
            print("You said: " + r.recognize_google(audio))
            tts = gTTS(text="I am machine", lang='en')
            tts.save("pcvoice.mp3")
            os.system("start pcvoice.mp3")
            print("Miny Said:" + "I am machine")

        if r.recognize_google(audio) == "who made you":
            print("You said: " + r.recognize_google(audio))
            tts = gTTS(text="You made me Sir. By the way, thanks for making me", lang='en')
            tts.save('pcvoice.mp3')
            os.system("start pcvoice.mp3")
            print("Miny Said:" + "You made me Sir. By the way, thanks for making me")

        if r.recognize_google(audio) == "can you hack":
            print("You said: " + r.recognize_google(audio))
            tts = gTTS(text="Sorry Sir, I am not designed for this", lang='en')
            tts.save('pcvoice.mp3')
            os.system("start pcvoice.mp3")
            print ("Miny Said: " + "Sorry Sir, I am not designed for this")

        if r.recognize_google(audio) == "thanks":
            print("You said: " + r.recognize_google(audio))
            tts = gTTS(text="You are most welcome sir, by the way thanks for using me", lang='en')
            tts.save('pcvoice.mp3')
            os.system("start pcvoice.mp3")
            print ("Miny Said: " + "You are most welcome sir, by the way thanks for using me")

        else:
            try:
                text = r.recognize_google(audio)
                print('Google thinks you said:\n' + text)
                lang = 'en'
                speak.tts(text, lang)
                f_text = 'https://www.google.co.in/search?q=' + text
                wb.get(chrome_path).open(f_text)

            except Exception as e:
                print (e)
        break

    except sr.UnknownValueError:
        print ('Could not understand the audio')
    except sr.RequestError as e:
        print("Could not request result: {0}".format(e))


