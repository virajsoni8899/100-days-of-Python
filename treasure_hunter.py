print("welcome to the treasure hunter island\n you mission is to find the treasure")
direaction = input("you are at a crossroad. where do you want to go? left or right")


if direaction == "left":
    decision = input("you come to a lake. there is an island in the middle of the lake. type 'wait' to wait for a boat. type 'swim' to swim across.")
    if decision == "swim":
        print("you swam across and were eaten by an alligator.\nGame Over.")
    elif decision == "wait":
        print("you waited for a boat. now you are at the island")
        doors = input("you see three doors. red, blue, and yellow, which one do you choose?")
        if doors == "red":
            print("you chose the red door. it was on fire.\nGame Over.")
        elif doors == "blue":
            print("you chose the blue door. it was a room full of snakes.\nGame Over.")
        elif doors == "yellow":
            print("you chose the yellow door. you found the treasure!\nYou Win!")
        else:
            print("you chose a door that doesn't exist.\nGame Over.")
    else:
        print("you chose a wrong direction.\nGame Over.")
elif direaction == "right":
    print("you chose the right direction. you are now at the edge of a cliff.\nGame Over.")
else:
    print("you chose a wrong direction.\nGame Over.")
        