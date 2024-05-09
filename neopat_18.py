a = [6,4,3,2,5]
b = sorted(a)
print("The unsorted list is :")
print(" ".join(map(str,a)))
for i in range(len(a)):
    for j in range(len(a) - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
    c = i+1
    d = str(c)
    print("After Pass "+d+" elements are:"+' '.join(map(str, a)))
    if a == b:
        break
print("The sorted list is :")
print(' '.join(map(str, a)))

# len(a) returns the length of the list a.
# len(a) - 1 gives the index of the last element in the list.
# len(a) - 1 - i  iterates up to one element less than the last element of the list minus the current value of i.
# This is done because after each pass through the list, the largest element will "bubble up"
