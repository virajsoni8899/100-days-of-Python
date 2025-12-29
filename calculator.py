def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    should_accumilate = True
    num1 = float(input("what's the first number?"))

    while should_accumilate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("pick an operation from the line above: ")
        num2 = float(input("what's the second number?"))
        answer = operations[operation_symbol](num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {answer}')

        choice = input("type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if choice == "y":
            num1 = answer
        else:
            should_accumilate = False
            print("Thank you for using the calculator!")

calculator()



