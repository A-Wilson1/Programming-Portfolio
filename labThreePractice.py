print(10 < 100)  # true
print(100 != 100)  # false
print(50 >= 50)  # true

age = 19
print(age < 18)
print(age < 21)
print(age < 31)

print("a" < "b")  # true
print("b" < "a")  # false
print("John" < "Terry")  # true

print("john" < "Terry")  # false because this time john isn't capitalized

print(5 < 10.2)  # true
# print(5<"Monty")  error
# print(5<"5")      error

age = 30
print(age >= 18 and age <= 65)  # true
print(age < 18 or age > 65)  # false
print(not age > 18)  # false

print((age >= 18 and age <= 65) and (not age == 30))  # false

weight = 130
height = 161
print(100 < weight < 200)
print(131 < height < 160)

names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
print("Terry" in names)  # true
print("z" in names)  # false

if 18 <= age <= 30:
    print("you are still young!")

if age > 100:
    print("you are very old,")
    print("well done!")
elif age > 80:
    print("you are fairly old")
    print("pretty good!")
elif age > 40:
    print("you are middle aged")
    print("never mind")
elif age > 30:
    print("you are still fairly young")
else:
    print("you are not very old - yet")

name = input("Enter your name: ")
if name != 0:
    print("Your name is", name)
else:
    print("Name not entered")

print("you are an adult" if age>=18 else "you are not an adult, yet!")

for n in ["tom", "james", "jerry", "joe"]:
    print(n)

for n in range(2,12,2):
    print(n," to the power of ",n," = ",n**n)

numbers = [10, 20 , 30, 90, 200, 30, 22, 11]

total=0
for n in numbers:
    if n>100:
        break
    total=total+n
    print(total)
else:
    print("all number processed")
