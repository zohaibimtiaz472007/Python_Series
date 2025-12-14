# Text to Speech Converter
import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 160)

text = input("Enter text you want to convert into speech: ")

engine.say(text)
engine.runAndWait()
