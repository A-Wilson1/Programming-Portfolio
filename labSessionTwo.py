total = 100
print("the total is ", total)

total = total + 99
print("the total is now ", total)

total -= 1
print("the total is ", total)
total *= 4
print("the total is ", total)
total /= 2
print("the total is ", total)

total = 98.2
count = 5
average = total / count

print(type(False))
print(type(1000))
print(type("hello"))
print(type(True))
print(type(100 / 5))
print(type(100 // 5))

print("abc" * 10)

print("Ashley")
print(len("ashley"))

# age = input("Enter your age ")
# print("in one year your will be", age + 1)
# doesn't work because the input is taken as a string

numberOne = int(input("Enter the first number: "))
numberTwo = int(input("Enter the second number: "))
print("the product of the numbers is ", numberOne * numberTwo)

# comment = "I would have "thought" you knew better!"        when you use double quotes it thinks you've ended the string
print()
print(
    "This text includes characters such as '\\' '\"' and \"'\",\n\tThis is a new line that starts with a tab\n\t\tThis new line starts with two tabs")
print()
print(
    "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\nHello There!\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
print()
print("""This text spans three lines,
and includes both single ('),
and double quotes (").
""")

surname = "Palin"
initial = surname[2]
print(initial)

# surname = "Palin"
# initial = surname[9]
# print(initial)
# index out of range error because there isn't ten letters in the surname

surname = "Palin"
last = surname[-2]
print(last)

surname = "Palin"
middle = surname[1:]
print(middle)

firstHalf = surname[:-1]
print(firstHalf)

names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
primes = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

print(primes[:4])

names[-1:-1] = ["Tim", "Bill"]
print(names)

nums = [1,2,3] * 5
print(nums)