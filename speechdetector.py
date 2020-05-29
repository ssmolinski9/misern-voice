import speech_recognition as sr


def detect_from_file(filename):
    r = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        audio = r.record(source)

    try:
        print("Recognised text: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
