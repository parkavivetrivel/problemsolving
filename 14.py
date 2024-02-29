import os

def factorial(num):
    if num == 0:
        return 1

    return num * factorial(num - 1)



okey = factorial(5)
print(okey)