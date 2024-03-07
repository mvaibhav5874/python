import random


def choose_word():
    words = (
        "apple", "banana", "orange", "grape", "kiwi",
        "dog", "cat", "bird", "fish", "rabbit",
        "computer", "programming", "code", "algorithm", "software",
        "mountain", "ocean", "forest", "desert", "canyon",
        "book", "novel", "author", "library", "page",
        "music", "song", "instrument", "melody", "concert",
        "sun", "moon", "star", "planet", "galaxy",
        "friend", "family", "love", "happiness", "laughter",
        "travel", "adventure", "explore", "journey", "destination",
        "coffee", "tea", "cup", "mug", "caffeine",
        "color", "painting", "palette", "canvas", "art",
        "movie", "film", "actor", "director", "cinema",
        "guitar", "piano", "drums", "violin", "musician",
        "football", "soccer", "basketball", "tennis", "athlete",
        "pizza", "burger", "pasta", "sushi", "dessert",
        "flower", "tree", "garden", "blossom", "petal",
        "rain", "snow", "storm", "cloud", "weather",
        "school", "teacher", "student", "classroom", "education",
        "phone", "tablet", "laptop", "smartwatch", "technology",
        "fire", "water", "earth", "air", "element",
        "time", "clock", "hour", "minute", "second",
        "dream", "imagination", "fantasy", "wonder", "inspiration")

    print(type(words))
    return random.choice(words)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def word_guessing_game():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 10

    print("Welcome to the Word Guessing Game!")
    print(display_word(word_to_guess, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word_to_guess:
                guessed_letters.append(guess)
                print("Good guess!")
            else:
                attempts -= 1
                print(f"Incorrect! You have {attempts} attempts remaining.")
        else:
            print("Please enter a valid single letter.")

        print(display_word(word_to_guess, guessed_letters))

        if set(guessed_letters) == set(word_to_guess):
            print("Congratulations! You guessed the word.")
            break

    if attempts == 0:
        print(f"Sorry, you're out of attempts. The word was '{word_to_guess}'.")


# Run the game
word_guessing_game()
