import math

result = math.sqrt(2401)
print(result)

from math import log2

result = log2(1024)
print(result)


def displayTwice(msg):
    """
    Displays the users input twice.
    """
    print(msg)
    print(msg)


displayTwice("hello")
displayTwice(12)
displayTwice(True)

help(displayTwice)


def findMax(a, b):
    """Finds the maximum of two values."""
    if (a > b):
        max = a
    else:
        max = b
    return max


print(findMax(1, 2))
print(findMax(20, 76))
print(findMax("abc", "xyz"))


def multiply(a, b=0):
    if b:
        return a * b
    else:
        return a * a


print(multiply(12))
print(multiply(6, 5))


def someFunc(x, y, z):
    print("x is", x, "\ny is", y, "\nz is", z)


print(someFunc(z=9, y=19, x=56))
print(someFunc(y=10, x=9, z=8))

print("file", "loading", sep="--")
print(1, 2, 3, sep="AA")


def calcAve(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


print(calcAve(1, 2, 3))
print(calcAve(1, 2, 3, 4, 5, 6, 7))

hypot = lambda a, b: math.sqrt(a * a + b * b)
print(type(hypot))

to_seconds = lambda hours, minutes: hours * 3600 + minutes * 60
print(to_seconds(2, 50))
print(to_seconds(0, 2))
print(to_seconds(1, 30))

to_seconds = lambda hours, minutes=0: hours * 3600 + minutes * 60
print(to_seconds(2))
