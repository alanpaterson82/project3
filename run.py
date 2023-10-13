import random
name = input("Type your name: ")
print("Good luck", name)
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
word = random.choice(words)
print("\nChoose a letter")
guesses = ""
tries = 10
while tries > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end = "")
        else:
            print("_", end = "")
            failed += 1
    if failed == 0:
        print("\n\nCongratulations!")
        print("\nThe word was:", word)
        break
    guess = input("\n\nChoose a letter: ")
    guesses += guess
    if guess not in word:
        tries -= 1
        print("\nThat's Not Right")
        print("\nYou have", +tries, "remaining")
        if tries == 0:
            print("\n\nBetter Luck Next Time!")