# navigator.py
import datetime

def navigate_path(choice):
    with open("thought_log.txt", "a") as log:
        log.write(f"[{datetime.datetime.now()}] User chose: {choice}\n")

