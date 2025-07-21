import time
import random
from difflib import SequenceMatcher
from colorama import Fore, Style

def get_sentence(level):
    """Return a random sentence based on the chosen difficulty level."""
    levels = {
        "beginner": [
            "The sun rises in the east.",
            "Python is easy to learn.",
            "Practice makes perfect.",
            "Keep calm and type on.",
            "Typing is a fun skill."
        ],
        "intermediate": [
            "Computers are an integral part of our daily lives.",
            "Typing tests are a great way to improve accuracy and speed.",
            "Learning new skills can be challenging but rewarding.",
            "Programming languages like Python are versatile and powerful.",
            "Technology continues to shape the modern world."
        ],
        "advanced": [
            "Artificial intelligence is revolutionizing industries across the globe.",
            "A journey of a thousand miles begins with a single step, as they say.",
            "Understanding complex algorithms requires patience and practice.",
            "Theoretical physics and quantum mechanics are fascinating fields of study.",
            "Effective communication is the cornerstone of success in any endeavor."
        ]
    }
    return random.choice(levels[level])

def calculate_results(start_time, typed_text, sentence):
    """Calculate typing speed, accuracy, and elapsed time."""
    end_time = time.time()
    elapsed_time = end_time - start_time
    words_per_minute = len(typed_text.split()) / (elapsed_time / 60)
    accuracy = SequenceMatcher(None, typed_text, sentence).ratio() * 100
    return elapsed_time, words_per_minute, accuracy

def display_results(player, elapsed_time, wpm, accuracy):
    """Display the results for a player."""
    print(f"\n{Fore.YELLOW}Player {player}'s Results:{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Time Taken: {elapsed_time:.2f} seconds{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Words Per Minute (WPM): {wpm:.2f}{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}Accuracy: {accuracy:.2f}%{Style.RESET_ALL}")

def typing_speed_test():
    """Main function to conduct the multiplayer or single-player typing speed test."""
    print(f"{Fore.CYAN}Welcome to the Typing Speed Test!{Style.RESET_ALL}")

    # Choose Mode: Single-player or Multiplayer
    print(f"{Fore.YELLOW}Select mode:{Style.RESET_ALL}")
    print("1. Single-player")
    print("2. Multiplayer")
    mode_choice = input(f"{Fore.GREEN}Enter your choice (1 or 2): {Style.RESET_ALL}").strip()

    # Ask players to choose a level
    print("\nChoose a difficulty level: beginner, intermediate, or advanced.")
    level = input(f"{Fore.GREEN}Enter your choice: {Style.RESET_ALL}").strip().lower()
    if level not in ["beginner", "intermediate", "advanced"]:
        print(f"{Fore.RED}Invalid choice. Defaulting to beginner level.{Style.RESET_ALL}")
        level = "beginner"

    sentence = get_sentence(level)
    print(f"\nYou will type the following sentence ({level.capitalize()} Level):")
    print(f"\n{Fore.YELLOW}\"{sentence}\"{Style.RESET_ALL}")

    results = {}

    if mode_choice == "1":  # Single Player Mode
        print(f"\n{Fore.CYAN}Single-player mode: You will now take the test.{Style.RESET_ALL}")
        input(f"{Fore.GREEN}Press Enter when you are ready...{Style.RESET_ALL}")
        print("\n3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)

        print(f"\n{Fore.YELLOW}Start typing:{Style.RESET_ALL}")
        start_time = time.time()
        typed_text = input("> ").strip()

        elapsed_time, wpm, accuracy = calculate_results(start_time, typed_text, sentence)
        results[1] = {"time": elapsed_time, "wpm": wpm, "accuracy": accuracy}
        display_results(1, elapsed_time, wpm, accuracy)

    elif mode_choice == "2":  # Multiplayer Mode
        print(f"\n{Fore.CYAN}Multiplayer mode: Two players will take the test.{Style.RESET_ALL}")
        for player in [1, 2, 3,4]:
            print(f"\n{Fore.YELLOW}Player {player}, get ready!{Style.RESET_ALL}")
            input(f"{Fore.GREEN}Press Enter when you are ready...{Style.RESET_ALL}")
            print("\n3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            time.sleep(1)

            print(f"\n{Fore.YELLOW}Start typing:{Style.RESET_ALL}")
            start_time = time.time()
            typed_text = input("> ").strip()

            elapsed_time, wpm, accuracy = calculate_results(start_time, typed_text, sentence)
            results[player] = {"time": elapsed_time, "wpm": wpm, "accuracy": accuracy}
            display_results(player, elapsed_time, wpm, accuracy)

    else:
        print(f"{Fore.RED}Invalid choice. Please restart and select a valid mode.{Style.RESET_ALL}")

    # Final Results: Declare Winner in Multiplayer or display Single Player results
    print("\n--- Final Results ---")
    for player, result in results.items():
        print(f"Player {player}: Time = {result['time']:.2f}s, WPM = {result['wpm']:.2f}, Accuracy = {result['accuracy']:.2f}%")

    if mode_choice == "2":  # Multiplayer Mode Results
        if results[1]["wpm"] > results[2]["wpm"]:
            print(f"\n{Fore.GREEN}Player 1 wins by typing faster!{Style.RESET_ALL}")
        elif results[1]["wpm"] < results[2]["wpm"]:
            print(f"\n{Fore.GREEN}Player 2 wins by typing faster!{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.YELLOW}It's a tie in typing speed!{Style.RESET_ALL}")

        if results[1]["accuracy"] > results[2]["accuracy"]:
            print(f"{Fore.GREEN}Player 1 wins with higher accuracy!{Style.RESET_ALL}")
        elif results[1]["accuracy"] < results[2]["accuracy"]:
            print(f"{Fore.GREEN}Player 2 wins with higher accuracy!{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}It's a tie in accuracy!{Style.RESET_ALL}")

if __name__ == "__main__":
    typing_speed_test()