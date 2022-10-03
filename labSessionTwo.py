# task 1

name = input("Hello, what is your name? ")
print(f"Hello, {name}. Good to meet you!")

# task 2

celsius = float(input("Enter a temperature in celsius: "))
fahrenheit = celsius * (9 / 5) + 32
print(f"{str(celsius)}C is equivalent to {str(fahrenheit)}F.")

# task 3

students = int(input("How many students? "))
groupSize = int(input("Required group size? "))
if (students % groupSize) == 1:
    print(f"There will be {str((students // groupSize))} groups with 1 student left over.")
else:
    print(f"There will be {str((students // groupSize))} groups with {str(students % groupSize)} student left over.")

# task 4

students2 = int(input("How many students? "))
sweets = int(input("How many sweets? "))
if (sweets % students2) == 1:
    print(f"There will be {str((sweets // students2))} sweets for each child with 1 sweet left over.")
else:
    print(f"There will be {str((sweets // students2))} sweets for each child with {str(sweets % students2)} sweets left over.")