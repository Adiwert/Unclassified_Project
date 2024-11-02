secret_word = "while"
word_list = ["hello", "memes", "until", "yield", "whine", "while"]

guess = input("Enter your guess: ").lower()

while guess != secret_word:
    if len(guess) != 5:
        print("Please enter a 5-letter word!")
    elif guess not in word_list:
        print("The word is not in word list!")
    else:
        correct_letters = 0
        i = 0
        while i < len(secret_word):
            if guess[i] == secret_word[i]:
                correct_letters += 1
            i += 1
        print(f"The number of correct letters is {correct_letters}")
    
    guess = input("Enter your guess: ").lower()

print("Well done!")