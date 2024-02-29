
def factorial(n):
    return n * factorial(n - 1)


do = factorial(10)
print(do)