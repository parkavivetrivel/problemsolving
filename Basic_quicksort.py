data = [7,113,245,67,89,10]


def quicksort(data):
    if len(data) <= 1:
        return data
    length = len(data)
    pivot = data[-1]
    j = 0
    for i in range(0, len(data)):
        if data[i] < pivot:
            data[i], data[j] = data[j], data[i]
            j += 1
    left_partition = quicksort(data[:j])
    right_partition = quicksort(data[j:-1])

    return left_partition + [pivot] + right_partition

a = quicksort(data)
print(a)
