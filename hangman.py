print("Welcome to the hangman game!")

import random

# Step 2: Generate a random word
word_list = [
    "python", "hangman", "computer", "programming", "challenge",
    "developer", "keyboard", "mouse", "algorithm", "function"
]

chosen_word = random.choice(word_list)

# Step 3: Generate blanks
display = ["_"] * len(chosen_word)
lives = 6

# Show initial state
print(f"\nThe word has {len(chosen_word)} letters:")
print(" ".join(display))
print(f"You have {lives} lives remaining.\n")

# Main game loop (Steps 4-5)
while "_" in display and lives > 0:
    # Step 4: Ask user to guess a letter
    user_guess = input("Guess a letter: ").lower()
    
    # Step 5: Is the guessed letter in the word?
    if user_guess in chosen_word:
        # Path A: Yes - Replace blanks with the letter
        for position in range(len(chosen_word)):
            if chosen_word[position] == user_guess:
                display[position] = user_guess
        
        print("\nCorrect guess!")
        print(" ".join(display))
        
        # Check: Are all blanks filled?
        if "_" not in display:
            # Game won - will exit loop
            break
    else:
        # Path B: No - Lose a life
        lives -= 1
        print(f"\nWrong guess! The letter '{user_guess}' is not in the word.")
        print(f"You have {lives} lives remaining.")
        print(" ".join(display))
        
        # Check: Have they run out of lives?
        if lives == 0:
            # Game lost - will exit loop
            break
    
    print()  # Empty line for spacing

# Step 6: GAME OVER
if "_" not in display:
    print("\n🎉 Congratulations! You won!")
else:
    print(f"\n💀 Game Over! The word was: {chosen_word}")