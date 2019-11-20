
import speech_recognition as sr
from textblob import TextBlob as blob
import pyttsx3
'''
speech_recognition: For Realtime Speech Recognizer
textblob : Sentimental analysis
pyttsx3  : Text-to-speech conversion library

if you got any error Please check Readme.md File To solve it.
'''

__AUTHOR__='Ravishankar Chavare'
__GITHUB__='https://github.com/chavarera'


def takeSound():
    '''
    It Takes Microphone input From user and
    return string output
    '''
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening....")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold=0.6
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
    except:
        return None
    return query

def getsentiment(text):
    '''
    Take input as text and Return Sentimental
    '''
    tb=blob(text)
    result=tb.sentiment
    polarity=result.polarity
    print({'polarity':polarity,'text':text})
    if polarity==0:
        return "Neutral"
    elif polarity>0:
        return "Positive"
    else:
        return "Negative"

def Speak(audio):
    '''
    Accept Text and Speak with Computer voice
    '''
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty("voice",voices[0].id)
    engine.say(audio)
    engine.runAndWait()

while True:
    print()
    text=takeSound()
    if text is not None:
        state=getsentiment(text)
        speak_text='I think You Are speaking {} thought'.format(state)
        print("Computer:",speak_text)
        Speak(speak_text)
