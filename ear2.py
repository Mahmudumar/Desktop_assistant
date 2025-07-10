from vosk import Model, KaldiRecognizer
import pyaudio
import json
import time
import state
import os

def listen_loop(command_queue):
    model_path = os.path.join(os.path.dirname(__file__), "vosk_model")
    model = Model(model_path)
    recognizer = KaldiRecognizer(model, 16000)

    # Mic setup
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    input=True,
                    frames_per_buffer=8000)
    stream.start_stream()

    print("🎧 Vosk Listening (offline)...")

    try:
        while state.running:
            data = stream.read(4000, exception_on_overflow=False)
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "").strip()
                if text:
                    print(f"🗣️ Heard: {text}")
                    command_queue.put(text.lower())
                else:
                    print("🔇 Silence or unrecognized speech.")
            time.sleep(0.3)

    except KeyboardInterrupt:
        print("🛑 Interrupted.")

    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
        print("🎤 Mic closed.")
