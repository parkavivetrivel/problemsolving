a = "aebaecedabbee"
b = []
c = 0
for i in a:
    if i not in b:
        b.append(i)
    elif i in b:
        c += 1
print(c)