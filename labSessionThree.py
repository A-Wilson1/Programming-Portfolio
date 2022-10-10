# Task 1
name = input("enter your name: ")
if name:
    print("hello ", name)
else:
    print("Hello, stranger")

# Task 2
passwordOne = input("please enter your password: ")
passwordTwo = input("please retype your password: ")
if passwordOne == passwordTwo:
    print("password is set")
else:
    print("passwords are not the same.")

# task 3
passwordOne = input("please enter your password: ")
if 8 <= len(passwordOne) <= 12:
    passwordTwo = input("please retype your password: ")
    if passwordOne == passwordTwo:
        print("password is set")
    else:
        print("passwords are not the same.")
else:
    print("password must be between 8 and 12 characters")

# task 4
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
passwordOne = input("please enter your password: ")
if len(passwordOne) < 8 or len(passwordOne) > 12:
    print("password must be between 8 and 12 characters")
elif passwordOne in BAD_PASSWORDS:
    print("pick a better password.")
else:
    passwordTwo = input("please retype your password: ")
    if passwordOne == passwordTwo:
        print("password is set")
    else:
        print("passwords are not the same.")

# task 5

while 1:
    passwordOne = input("please enter your password: ")
    if len(passwordOne) < 8 or len(passwordOne) > 12:
        print("password must be between 8 and 12 characters")
    elif passwordOne in BAD_PASSWORDS:
        print("pick a better password.")
    else:
        passwordTwo = input("please retype your password: ")
        if passwordOne == passwordTwo:
            print("password is set")
            break
        else:
            print("passwords are not the same.")

# task 6

for n in range(13):
    print(n, " x 7 = ", n * 7)

# task 7

while 1:
    number = int(input("enter a number between 0 and 12: "))
    if 0 <= number <= 12:
        break
for n in range(12):
    print(n, " x ", number, " = ", n * number)

# task 8
while 1:
    number = int(input("enter a number between 0 and 12: "))
    if -12 <= number <= 12:
        break
if number < 0:
    for n in range(12, 0, -1):
        print(n, " x ", abs(number), " = ", n * abs(number))
else:
    for n in range(12):
        print(n, " x ", number, " = ", n * number)
