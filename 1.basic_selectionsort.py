array = [7, 6, 3, 4, 43 ]
for i in range(0, len(array)):
    first_number = i
    for j in range(first_number+1,len(array)):
        if array[first_number]>array[j]:
            array[first_number],array[j]=array[j],array[first_number]
print(array)