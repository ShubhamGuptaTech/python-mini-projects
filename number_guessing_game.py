import random
guessed_num = random.randint(1, 100)
process = True
guess_count = 0
print("WELCOME IN  GAME:'GUESSING A NUMBER'")
while process:
    guess_count += 1
    user_guess = input("Guess a number between 1 to 100 or press 'q' or 'Q' to quit the game: ")
    if (user_guess == "q" or user_guess== "Q"):
        print("thanks for playing")
        break
    user_guess = int(user_guess)
    if user_guess == guessed_num:
        print("YOU WON - you guessed the right number")
        print(f"you won in {guess_count} attempt")
        guessed_num = random.randint(1,100)
        guess_count = 0
    elif user_guess < guessed_num:
        print("Guess a higher number ")
    else:
        print("Guess a lower number ")
