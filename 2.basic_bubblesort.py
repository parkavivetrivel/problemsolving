array = [9, 8, 7, 6, 5, 4]
for i in range(0, len(array)-1):
    for j in range(0, len(array)-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            print(array)





