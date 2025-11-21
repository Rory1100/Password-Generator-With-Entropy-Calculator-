import random
from string import ascii_lowercase, ascii_uppercase
import math

def generate_strong_password(length: str, num: bool, special: bool):
    number = length // 3
    speci = length // 2
    asci = ascii_lowercase + ascii_uppercase
    password = []

    
    while len(password) < length:
        if num and number != 0:
            y = random.randint(1, 9)
            password.append(str(y))
            number -= 1 

        if special and speci != 0:
            spechar = ['!', '?', '=', '+', '-', '(', ')', '#']
            random.shuffle(spechar)
            password.append(spechar[0])
            speci -= 1

        if len(password) >= length:
            break
        else:
            x = random.choice(asci)
            password.append(x)

    random.shuffle(password) #added for more entropy 
    return "".join(password), length

def entropy(password, L): #Shannon Entropy Formula for passwords
    helper = []
    for char in password:
        if char in helper:
            continue
        else:
            helper.append(char)

    entrop = math.log2(len(helper) ** L)
    return f"{entrop:.2f}"

password_length = int(input("Input Password Length (Postive int): "))
number_bool = input("Add numbers Y/N: ")
if number_bool == "y" or number_bool == "Y":
    number_bool = True
elif number_bool == "n" or number_bool == "N":
    number_bool = False

special_char = input("Special Characters Y/N: ")
if special_char == "Y" or special_char == "y":
    special_char = True
else:
    special_char = False

password, length = generate_strong_password(password_length, number_bool, special_char) # Just use these methods if you do not want to go through the questions ex. 24, True, True 
entrop = entropy(password, length)

print(password)
print(f"Entropy: {entrop}\n")

want_loop = input("Do you want to loop passwords Y/N: ")
if want_loop == "Y" or want_loop == "y":
    print("Press Enter: any input will quit loop")
    while True:
        keep_loop = input("")
        if keep_loop == "":
            password, length = generate_strong_password(password_length, number_bool, special_char)
            entrop = entropy(password, length)

            print(password)
            print(f"Entropy: {entrop}\n")
        else:
            break
else:
    print("Thanks!")