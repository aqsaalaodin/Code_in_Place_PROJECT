# journal.py
def write_journal_entry():
    print("\n✍️ Let's journal your thoughts.")
    entry = input("What would you like to reflect on or release today?\n> ")
    with open("thought_log.txt", "a") as f:
        f.write(f"Journal Entry: {entry}\n")
    print("✅ Your journal entry has been saved.")
