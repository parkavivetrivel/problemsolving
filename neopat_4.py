a = "AODN".lower()
b = ["a", "e", "i", "o", "u"]
d = []
for i in a:
    if i not in b:
        if a.index(i) == len(a)-1:
            d.append(i)
        else:
            d.append("."+i+".")

result = "".join(d)
print(result)