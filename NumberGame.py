# this is a number guessing game there are 3 levels of difficulty easy, medium, and hard
import random
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    print("You have 10 attempts to guess the number.")
    attempts = 10
elif difficulty == "hard":
    print("You have 5 attempts to guess the number.")
    attempts = 5
else:
    print("Invalid difficulty. Please try again.")
    exit()

number = random.randint(1, 100)
while attempts > 0:
    guess = int(input("Guess a number: "))
    if guess == number:
        print("You guessed the number correctly!")
        break
    elif guess < number:
        print("Too low.")
        attempts -= 1
        print(f"You have {attempts} attempts left.")
    elif guess > number:
        print("Too high.")
        attempts -= 1
        print(f"You have {attempts} attempts left.")
    if attempts == 0:
        print("You have run out of attempts. You lose.")
        break
    print("Guess again.")
if attempts == 0:
    print("You have run out of attempts. You lose.")
else:
    print("You guessed the number correctly!")
    print(f"You have {attempts} attempts left.")
    print(f"You have {attempts} attempts left.")