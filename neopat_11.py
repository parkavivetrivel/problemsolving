n = int(input())
b = []
k = 2*n
for i in range(k):
    a = input()
    #b[a] = input()
    b.append(a)
alpha = set()
for i in b:
    if i.isalpha():
        alpha.add(i)
sorted_alpha = sorted(alpha)
print("Distinct Symbols are:")
print(" ".join(sorted_alpha))
for i in sorted_alpha:
    if i in b:
        count = b.count(i)
        print(f"Cards in {i} symbol:")
        c = b.index(i)+1
        bh = 0
        for j in range(count):
            print(i, b[c])
            bh += int(b[c])
            b[b.index(i)] = "@"
            b[c] = "@"
        print("Number of Cards:", b.count(i))
        print("Sum of Numbers:",bh)
print(b,"b")

