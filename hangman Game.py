import random

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    ========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    ========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    ========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    ========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    ========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    ========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========"""
]

WORDS = ["python", "hangman", "challenge", "simple", "program", "developer"]

def hangman():
    word = random.choice(WORDS)
    guessed = ["_"] * len(word)
    guessed_letters = []
    wrong_guesses = 0
    max_attempts = len(HANGMAN_PICS) - 1

    print("Welcome to Hangman!")

    while wrong_guesses < max_attempts and "_" in guessed:
        print(HANGMAN_PICS[wrong_guesses])
        print("Word: " + " ".join(guessed))
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print("Correct!")
        else:
            wrong_guesses += 1
            print("Incorrect!")

    if "_" not in guessed:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print(HANGMAN_PICS[wrong_guesses])
        print("\nGame over. The word was:", word)

# Run the game
hangman()
