import random
secret_number = random.randint(1, 100)

max_guesses = 5

for i in range(max_guesses):

  user_guess = int(input("Enter your guess: "))

  if user_guess == secret_number:
    print("Congratulations! You guessed the number in", i + 1, "guesses!")
    break
  elif user_guess < secret_number:
    print("Your guess is low. Guess again!")
  else:
    print("Your guess is high. Guess again!")

if i == max_guesses - 1:
  print("Sorry, you ran out of guesses! The secret number was", secret_number)

