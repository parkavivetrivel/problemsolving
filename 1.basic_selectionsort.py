array = [9,6,4,3,8]
for i in range(0, len(array)-1):
    for j in range(i+1,len(array)):
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]
print(array)