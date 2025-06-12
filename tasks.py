# tasks.py
import random

tasks = [
    "Take 3 deep breaths slowly.",
    "Look out the window and describe what you see.",
    "Stretch your arms over your head and hold for 10 seconds.",
    "Drink a glass of water. Hydration helps!",
    "Write down one thing you're looking forward to."
]

def suggest_task():
    task = random.choice(tasks)
    print("\n🧠 Gentle Task: " + task)
    with open("thought_log.txt", "a") as f:
        f.write(f"Task Suggested: {task}\n")
