# this is pizza delivery program

print("welcome to python pizza deliveries!")

size = input("what size pizza do you want? S, M, or L\n")
pepperoni = input("do you want pepperoni? Y or N\n")
extra_cheese = input("do you want extra cheese? Y or N\n")
bill = 0

if size == "S":
    bill += 15
    print("Small pizza is $15.")
elif size == "M":
    bill += 20
    print("Medium pizza is $20.")
elif size == "L":
    bill += 25
    print("Large pizza is $25.")

if pepperoni == "Y":
    bill += 2
    print("Pepperoni is $2.")

if extra_cheese == "Y":
    bill += 1
    print("Extra cheese is $1.")

print(f"Your final bill is ${bill}.")