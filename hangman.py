import random
STAGES = [
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / \\
       -
    """,
    # head, torso, both arms, and one leg
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     /
       -
    """,
    # head, torso, and both arms
    """
       --------
       |      |
       |      O
       |     \\|
       |      |
       |
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |
       -
    """,
    # head, torso, and one arm
    # head and torso
    """
       --------
       |      |
       |      O
       |      |
       |      |
       |
       -
    """,
    # head
    """
       --------
       |      |
       |      O
       |
       |
       |
       -
    """,
    # initial empty state
    """
       --------
       |      |
       |
       |
       |
       |
       -
    """,
]
WORDS = ['HAYDN', 'SOFTWARE', 'ENGINEER', 'YOUTUBE', 'CHANNEL' 'AMAZING', 'SUBSCRIBE']

if __name__ == '__main__':
    word_to_guess = random.choice(WORDS)
    word_to_display = ['_'] * len(word_to_guess)

    guesses_remaining = len(STAGES)
    guessed_letters = []

    print('Time to play Hangman!')

    while guesses_remaining > 0:
        print(STAGES[guesses_remaining - 1])
        print("".join(word_to_display))
        letter = input('What letter do you guess?: ').upper()

        if letter in guessed_letters:
            print(f"You already guessed {letter}, so try again!")
        elif letter in word_to_guess:
            print(f'Wahoo, you found {letter} in the word!')
            # replace word to display with guessed letter.
            for i, char in enumerate(word_to_guess):
                if char == letter:
                    word_to_display[i] = letter
        else:
            # we didn't guess a letter, so lose a life.
            print(f'Sorry {letter} is not in the word!')
            guesses_remaining -= 1

        guessed_letters.append(letter)

        if '_' not in word_to_display:
            print('You won!')
            break
        if guesses_remaining == 0:
            print('Oh, no it is Hangman! - you are out of guesses')
