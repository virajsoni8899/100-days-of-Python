print("welcome to the tip calculator")

total_bill = float(input("what was the total bill? $"))
tip_percentage = int(input("what percentage tip would you like to give? 10, 12, or 15?"))
split = int(input("how many people to split the bill?"))

print(f'Each person should pay: ${((total_bill/split)*(1+tip_percentage/100)):.2f}')
