# task 1

def in_Range(num):
    if 0 <= num <= 100:
        return True
    else:
        return False


print(in_Range(54))
print(in_Range(104))


# task 2

def string_Calc(sentance):
    upper = 0
    lower = 0
    for i in sentance:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    return upper, lower


print(string_Calc("Hello AAA"))


# task 3

def make_proper(name):
    name = name.lower()
    name = name.capitalize()
    return name


# name = input("enter your name: ")
# name = make_proper(name)
# print("Hello ", name)

# task 4

def remove_last(a):
    if len(a) > 1:
        a = a.rstrip(a[-1])
    return a


print(remove_last("abcd"))


# task 5

def cels_tofahr(a):
    return (a * (9 / 5)) + 32


def fahr_tocels(a):
    return (a - 32) * (5 / 9)


print("12C is ", cels_tofahr(12), "F")
print("12F is ", fahr_tocels(12), "C")

# task 6

cels = input("enter a temperature : ")
cels = int(cels.rstrip(cels[-1]))
farh = cels_tofahr(cels)
print(cels, "C is ", farh, "F")

# task 7

temps = []
total = 0
for n in range(6):
    cels = input("enter a temperature : ")
    cels = int(cels.rstrip(cels[-1]))
    total += cels
    temps.append(cels)
print(max(temps), "C is the max ", min(temps), "C is the min and ", total / len(temps), "C is the mean")

# task 8

temps = []
total = 0
while 1:
    cels = input("enter a temperature : ")
    if cels:
        cels = int(cels.rstrip(cels[-1]))
        total += cels
        temps.append(cels)
    else:
        break
print(max(temps), "C is the max ", min(temps), "C is the min and ", total / len(temps), "C is the mean")
