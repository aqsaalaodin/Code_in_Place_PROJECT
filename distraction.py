# distraction.py
import random

affirmations = [
    "You are doing your best, and that's enough! 💪",
    "You deserve peace and joy. 🌈",
    "You're stronger than you think! 🌟",
    "One moment at a time, you are moving forward. 🛤️"
]

jokes = [
    "Why don’t skeletons fight each other? They don’t have the guts. 💀",
    "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾"
]

def distract():
    print("\n🎈 Time for a light moment!")
    if random.choice([True, False]):
        print("💬 Affirmation: " + random.choice(affirmations))
    else:
        print("😂 Joke: " + random.choice(jokes))

