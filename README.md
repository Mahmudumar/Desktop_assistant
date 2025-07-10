
# 🗣️ Upchups Desktop Assistant

**Upchups Desktop Assistant** is a minimal, offline-capable voice assistant built in Python. It listens to spoken input, converts it to text, and responds based on simple rule-based logic.

The assistant is designed with clean separation between its core components: listening, thinking, and speaking.

---

## ✅ Features

- 🎤 Voice input (Google Speech or offline via Vosk)
- 🧠 Basic command processing (e.g., tell time, exit)
- 🗣️ Text-to-speech output using `pyttsx3`
- 🚦 Voice-controlled shutdown ("exit" / "stop")

---

## 📦 Folder Structure

```plaintext

project\_root/
├── main.py         # Entry point
├── ear.py          # Online voice input (Google)
├── ear2.py         # Offline voice input (Vosk)
├── brain.py        # Handles voice commands
├── mouth.py        # Text-to-speech output
├── state.py        # Shared flag for stopping threads
├── vosk-model/     # (Optional) Offline model directory
└── README.md

````

---

## 🛠 Requirements

Install dependencies:

```bash
pip install speechrecognition pyttsx3 keyboard vosk
````

For offline mode (`ear2.py`), download a Vosk model:
🔗 [https://alphacephei.com/vosk/models](https://alphacephei.com/vosk/models)

Extract it into a folder named `vosk-model`, for example:

```
vosk-model-small-en-us-0.15/
```

---

## 💬 Sample Voice Commands

| You Say            | Assistant Responds                                       |
| ------------------ | -------------------------------------------------------- |
| `what is the time` | 🗣️ "The time is 09:48 AM"                               |
| `exit` or `stop`   | 🗣️ "Okay, shutting down."                               |
| anything else      | 🗣️ "I heard: ..., but I don't know how to do that yet." |

---

## ⚙️ How It Works

* **`ear.py` / `ear2.py`**: Captures voice, converts to text
* **`brain.py`**: Interprets the command and decides on a response
* **`mouth.py`**: Speaks back the assistant’s reply
* **`state.py`**: Used to stop all background threads gracefully

Thread-safe queues handle communication between modules.

---

## 🎯 Design Principles

* 🧩 **Modular** — Each file does one thing well.
* 📡 **Offline-First** — Works without internet using Vosk.
* 🧘 **Minimal** — Only the core logic is included.
* 🧼 **Voice-Based Exit** — No keyboard needed to stop the assistant.

---

## 🧠 For Learners

This project demonstrates:

* Real-world Python threading with queues
* Voice I/O architecture (mic in → logic → speaker out)
* Clean separation of components (MVC-style thinking)
* Introduction to offline-first design in assistant tools

---

## ⚠️ Developer Reminder

> ✋ If the project is working, **stop here**. Add new features only when there's a clear reason.

Protect working code. Build intentionally.


Made with intention by the **TNR Software Team**
Teaching real software design from day one.
