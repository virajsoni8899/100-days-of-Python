" this program will generate a random password for you"
import random 

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

my_letters = int(input("how many letters would you like in your password?"))
my_symbols = int(input("how many symbols would you like in your password?"))
my_numbers = int(input("how many numbers would you like in your password?"))

generated_password = ""

for i in range(my_letters):
    generated_password += random.choice(letters)

for i in range(my_symbols):
    generated_password += random.choice(symbols)

for i in range(my_numbers):
    generated_password += random.choice(numbers)

password_list = list(generated_password)
random.shuffle(password_list)
generated_password = "".join(password_list)

print(generated_password)