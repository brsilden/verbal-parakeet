from time import sleep
import pyttsx3

engine = pyttsx3.init()

#engine.setProperty('voice', "com.apple.speech.synthesis.voice.samantha")


while True:
    text = input()
    engine.say(text)
    engine.runAndWait()
