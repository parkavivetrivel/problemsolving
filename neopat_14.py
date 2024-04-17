def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    total = sum(int(digit)**num_digits for digit in num_str)
    return total == num

def armstrong_numbers_in_range(n):
    armstrong_numbers = []
    for i in range(1, n + 1):
        if is_armstrong(i):
            armstrong_numbers.append(i)
    return armstrong_numbers

# Input
n = int(input())

# Output
armstrong_nums = armstrong_numbers_in_range(n)
print(" ".join(map(str, armstrong_nums)))
