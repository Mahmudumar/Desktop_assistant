# hands.py

import os
import shutil

def open_app(name):
    try:
        if name == "chrome":
            os.system("start chrome")
        elif name == "notepad":
            os.system("start notepad")
        elif name == "vscode" or name == "code":
            os.system("code")  # VS Code must be in PATH
        else:
            return f"App '{name}' not recognized"
        return True
    except Exception as e:
        return str(e)

def move_file(src, dest_folder):
    try:
        if not os.path.exists(src):
            return f"Source file not found: {src}"
        if not os.path.isdir(dest_folder):
            return f"Destination folder not found: {dest_folder}"
        shutil.move(src, dest_folder)
        return True
    except Exception as e:
        return str(e)

def create_folder(path):
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except Exception as e:
        return str(e)
