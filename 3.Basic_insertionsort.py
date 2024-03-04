array = [98, 76, 54, 33, 32, 41]
for i in range(1, len(array)):
    first = array[i]
    j = i - 1
    while j >= 0 and array[j] > first:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = first
print(array)
