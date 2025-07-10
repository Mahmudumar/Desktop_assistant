# main.py

import threading
from queue import Queue
import ear
import brain
import state
import sys
# Shared queues
command_queue = Queue()
# Note: speech goes directly through `mouth.speak()` now, not via speech_queue.


def run_ear():
    ear.listen_loop(command_queue)


def run_brain():
    brain.think_loop(command_queue)


if __name__ == "__main__":
    print("🤖 Assistant started.")

    # Optional greet once at startup
    import mouth
    import time
    mouth.speak("Hello. I'm ready. You can speak anytime.")

    # Start ear and brain in separate threads
    threading.Thread(target=run_ear, daemon=True).start()
    threading.Thread(target=run_brain, daemon=True).start()

    # Keep the main thread alive
    while state.running:
        try:
            time.sleep(0.5)
        except KeyboardInterrupt:
            print("🛑 Exiting assistant.")
            state.running = False
            break
    print("Exiting now.")
    sys.exit()
