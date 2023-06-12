import speech_recognition as sr
def Listen():

    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source,0,4)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')

    except:
        return ""

    return query

def wakeUp():
    query=Listen().lower()

    if "wake up" in query:
        from Body.speak import Speak
        Speak("Yes Boss")
        from vesper import MainExe
        MainExe()
    else:
        pass