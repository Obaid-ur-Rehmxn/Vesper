import speech_recognition as sr
from googletrans import Translator

def Listen():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source,0,8)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')

    except:
        return ""

    return query

def translationIntoEnglish(Text):
    line=str(Text)
    translator = Translator()
    result=translator.translate(line)
    data=result.text
    print(f"You: {data}.")
    return data

def micExecution():
    query=Listen().lower()
    data=translationIntoEnglish(query)
    return data      