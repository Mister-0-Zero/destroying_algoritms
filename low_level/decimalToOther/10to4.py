import random 

def decimalToFour(number):
    res = ""
    while number > 0:
        res = str(number % 4) + res
        number //= 4

    return res

for i in range(3):
    number = random.randint(5, 40)
    four_ = decimalToFour(number=number)
    print(f"number: {number}, in four: {four_}")