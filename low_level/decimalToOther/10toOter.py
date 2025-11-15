import random

def decimalToOther(number, system_cal):
    res = ""
    while number > 0:
        res = str(number % system_cal) + res
        number //= system_cal
    return res

for i in range(5):
    system_cal = random.randint(2, 16)
    number = random.randint(20, 60)
    res = decimalToOther(number=number, system_cal=system_cal)
    print(f"system_cal: {system_cal}, number: {number}, res: {res}")