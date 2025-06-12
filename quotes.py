# quotes.py
import random

quotes = [
    "The only way out is through. – Robert Frost",
    "You must do the thing you think you cannot do. – Eleanor Roosevelt",
    "It always seems impossible until it’s done. – Nelson Mandela",
    "Do what you can, with what you have, where you are. – Theodore Roosevelt"
]

def get_quote():
    return random.choice(quotes)

