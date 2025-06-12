from navigator import navigate_path
from journal import write_journal_entry
from quotes import get_quote
from tasks import suggest_task
from reflection import reflect
from distraction import distract

def main():
    print("\n🧭 Welcome to Thought Navigator – Let's gently guide your mind.")
    print("--------------------------------------------------------------")

    while True:
        print("\nWhat are you looking for right now?")
        print("1. Reflection 🌌")
        print("2. Distraction 🎈")
        print("3. Random Quote 💬")
        print("4. Guided Task 🧠")
        print("5. Journal ✍️")
        print("6. Exit 🚪")

        choice = input("Enter your choice (1–6): ").strip()

        if choice == "1":
            navigate_path("reflection")
            reflect()
        elif choice == "2":
            navigate_path("distraction")
            distract()
        elif choice == "3":
            print("💬 Quote of the moment:")
            print(get_quote())
        elif choice == "4":
            suggest_task()
        elif choice == "5":
            write_journal_entry()
        elif choice == "6":
            print("\n🌿 Take care. See you next time on Thought Navigator!")
            break
        else:
            print("❗ Invalid choice. Please select a number from 1 to 6.")

if __name__ == "__main__":
    main()
