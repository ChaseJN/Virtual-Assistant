#from date import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

engine = pyttsx3.init()
voices = engine.getProperty('voices')
