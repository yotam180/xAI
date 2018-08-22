import speech_recognition as sr

#Gets recognizer general object
r = sr.Recognizer()

def recognize():
    try:
        with sr.Microphone() as mic:
            #listens and finds relevant audio for recognition
            audio = r.listen(mic)
            return r.recognize_google(audio)
    except:
        return ""