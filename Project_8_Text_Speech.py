import pyttsx3

data= input("Enter text which you want to speech: ")
engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()