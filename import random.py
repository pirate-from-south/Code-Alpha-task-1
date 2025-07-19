import random

def hangman():
    words = ["python", "programming", "computer", "challenge", "developer"]
    secret_word = random.choice(words).lower()
    guessed_letters = []
    attempts = 7  

    print("Welcome to Hangman!")
    print(f"The word has {len(secret_word)} letters.")

    while attempts > 0:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print(f"\nWord: {display_word}")

        if "_" not in display_word:
            print("Congratulations! You guessed the word!")
            break

        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1

    if attempts == 0:
        print("\nGame Over! You ran out of attempts.")
        print(f"The word was: {secret_word}")

if __name__ == "__main__":
    hangman()
