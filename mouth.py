# mouth.py

import multiprocessing
import pyttsx3

def speak(text):
    print(f"[🗣️ Speaking]: {text}")
    p = multiprocessing.Process(target=_speak_internal, args=(text,))
    p.start()
    p.join()  # Wait until done

def _speak_internal(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 180)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id) # type: ignore
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"[⚠️ Mouth error]: {e}")
