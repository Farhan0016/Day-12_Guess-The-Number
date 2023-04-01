import random

#Make function to set difficulty.
def difficulty_level(difficulty):
    if difficulty == 'hard':
        return 5
    else:
        return 10

#Function to check user's guess against actual answer.
def check_the_guess(guess):
    if (guess == selected_number):
        print(f"You got it! The answer was {guess}.")
        return True
    elif guess > selected_number:
        print("Too high.")
    else:
        print("Too low.")


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

#Choosing a random number between 1 and 100.
selected_number = random.randint(1, 100)

print(f"Psst, the correct answer is {selected_number}")

attempts = difficulty_level(input("Choose a difficulty. Type 'easy' or 'hard': "))

print(f"You have {attempts} attempts remaining to guess the number.")

#Repeat the guessing functionality if they get it wrong.
game_over = False
while not game_over:
    # Let the user guess a number.
    guess = int(input("Make a guess: "))

    if check_the_guess(guess):
        game_over = True
    else:
        attempts -= 1

        if attempts == 0:
            print(f"You've run out of guesses. You lose, the number is {selected_number}.")
            game_over = True
        else:
            print("Guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")
