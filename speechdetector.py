
import speech_recognition as sr
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException


def detect_from_file(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = r.record(source)

    try:
        en = r.recognize_google(audio, language="en-EN")
        isEnglish = detect(en) == "en"

        es = r.recognize_google(audio, language="es-ES")
        isSpanish = detect(es) == "es"

        de = r.recognize_google(audio, language="de-DE")
        isGerman = detect(de) == "de"

        rec = 0

        if isEnglish and rec == 0:
            rec = 1
            print("I think you speak English. " + "Recognised text: " + en)
        if isGerman and rec == 0:
            rec = 1
            print("I think you speak German. " + "Recognised text: " + de)
        if isSpanish and rec == 0:
            rec = 1
            print("I think you speak Spanish. " + "Recognised text: " + es)
        if rec == 0:
            print("I can't recognize your language :(")

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except LangDetectException:
        print("Please say something more than just a numbers if you want your language to be recognized")
