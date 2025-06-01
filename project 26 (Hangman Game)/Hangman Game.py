import random

def hangman():
    word_list = ["python", "hangman", "minecraft", "coding", "developer", "banana", "keyboard"]
    word = random.choice(word_list)
    guessed = "_" * len(word)
    attempts = 6
    guessed_letters = []

    print("🎮 Welcome to Hangman!")
    print("Word to guess: " + " ".join(guessed))

    while attempts > 0 and "_" in guessed:
        guess = input("\nEnter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("🔁 You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            guessed = "".join([letter if letter == guess or letter in guessed_letters else "_" for letter in word])
            print("✅ Correct!")
        else:
            attempts -= 1
            print(f"❌ Wrong! {attempts} attempts left.")

        print("Word: " + " ".join(guessed))
        print("Guessed letters:", " ".join(guessed_letters))

    if "_" not in guessed:
        print("\n🎉 You win! The word was:", word)
    else:
        print("\n💀 Game over! The word was:", word)

if __name__ == "__main__":
    hangman()
