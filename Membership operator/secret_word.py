word = "APPLE"

letter = input("Guess a letter in the secret words: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")