import random

def decimalToBin(number):
    res = ""
    while number > 0:
        res = str(number % 2) + res
        number //= 2
    return res

for i in range(3):
    number = random.randint(5, 20)
    binary = decimalToBin(number=number)
    binary_true = bin(number)[2:]
    check = binary_true == binary
    print(f"imput: {number}, output: {binary}, check:{check}\n")