# this is rock paper scissor game
import random

choice = int(input("what do you choose? type 0 for rock, 1 for paper, 2 for scissor\n"))


computer_choice = random.randint(0, 2)
print(f"computer chose {computer_choice}")

if choice == computer_choice:
    print("it's a tie")
elif choice == 0 and computer_choice == 1:
    print("you lose")
elif choice == 0 and computer_choice == 2:
    print("you win")
elif choice == 1 and computer_choice == 0:
    print("you win")
elif choice == 1 and computer_choice == 2:
    print("you lose")
elif choice == 2 and computer_choice == 0:
    print("you lose")
elif choice == 2 and computer_choice == 1:
    print("you win")






