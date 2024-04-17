n = input()
b = []
for i in range(1, int(n)):
    c = 0  # Reset c for each number
    if len(str(i)) <= 1:
        b.append(i)
    elif len(str(i)) > 1:
        for j in str(i):
            k = int(j) * int(j) * int(j)
            c += k
        if c == i:
            b.append(i)
for k in b:
    print(k, end=" ")
