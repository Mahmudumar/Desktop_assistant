# brain.py

import mouth
from datetime import datetime
import sys
import state
def think_loop(command_queue):
    while state.running:
        command = command_queue.get()

        if not command:
            continue

        if command.startswith("[error"):
            mouth.speak("I'm having trouble reaching the speech service.")
            continue
        

        # teach

        if "time" in command:
            now = datetime.now().strftime("%I:%M %p")
            mouth.speak(f"The time is {now}")
        
        elif "exit" in command or "stop" in command:
            mouth.speak("Okay, shutting down.")
            state.running = False

        else:
            mouth.speak(f"I heard: {command}, but I don't know how to do that yet.")
