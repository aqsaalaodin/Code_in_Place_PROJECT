# reflection.py
import random

deep_questions = [
    "What are you grateful for today?",
    "What's one lesson you've learned recently?",
    "If today had a theme, what would it be?",
    "What are you holding onto that you should let go?"
]

def reflect():
    question = random.choice(deep_questions)
    print("\n🌌 Reflection Time:")
    print(f"🧠 {question}")
    input("Take a moment and write your thoughts (press Enter when done)...")
    with open("thought_log.txt", "a") as f:
        f.write(f"Reflection: {question}\n")

