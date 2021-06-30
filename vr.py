#!/usr/bin/python3
import speech_recognition as sr
import os
import time
import pyttsx3

listener = sr.Recognizer()

while True:

    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            if 'capture' in command :
                print('capturing')
                engine = pyttsx3.init()
                engine.say("capturing")
                engine.runAndWait()
            if 'record' in command :
                print('recording')
                engine = pyttsx3.init()
                engine.say("recording")
                engine.runAndWait()                
    except:
        pass
