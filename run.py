import random

words = [
    "tiger",
    "lion",
    "elephant",
    "giraffe",
    "hippopotamus",
    "antelope",
    "zebra",
    "hyena",
    "rhinoceros",
    "bear",
    "leopard",
]


def play_round():
    name = input("Type your name:\n")
    print("Good luck", name)

    word = random.choice(words)
    print("\nChoose a letter or type a word")
    guesses = ""
    tries = 10
    while tries > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end="")
            else:
                print("_", end="")
                failed += 1
        if failed == 0:
            print("\n\nCongratulations!")
            print("\nThe word was:", word)
            break
        guess = input("\n\nChoose a letter or type a word:\n")
        guesses += guess
        if guess not in word:
            tries -= 1
            print("\nThat's Not Right")
            print("\nYou have", +tries, "tries remaining")
            if tries == 0:
                print("\n\nBetter Luck Next Time! The word was", word)


def main():
    play_again = True
    while play_again:
        play_round()
        play_again_response = input("\n\nPress y then 'Enter' to play again, or any other key then 'Enter' to exit: ").strip().lower()

        if play_again_response != 'y':
            print("Thank you for playing. Good Bye!")
            play_again = False

main()

