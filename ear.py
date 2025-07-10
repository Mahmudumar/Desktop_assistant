# ear.py

import speech_recognition as sr
import time
import state
def listen_loop(command_queue):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    while state.running:
        with mic as source:
            print("🎧 Listening...")
            try:
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
            except sr.WaitTimeoutError:
                print("❌ Nothing said in time.")
                continue  # Don't send anything to brain

            try:
                command = recognizer.recognize_google(audio) # type: ignore
                if command.strip():  # If it's not just silence
                    print(f"🗣️ Heard: {command}")
                    command_queue.put(command.lower())
                else:
                    print("🔇 Detected silence or empty speech.")
            except sr.UnknownValueError:
                print("❌ Couldn’t understand.")
                # Do NOT send anything
            except sr.RequestError:
                print("🌐 Speech service error.")
                command_queue.put("[error: speech service failure]")

        time.sleep(0.5)
