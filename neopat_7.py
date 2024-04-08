a = "abc%sld*"
b =[]
s =[]
for i in range(len(a)-1,-1,-1):
    if a[i].isalpha():
        b.append(a[i])
    else:
        s.append(a[i])
for i in s:
    d = a.index(i)
    b.insert(d,i)
result = "".join(b)
print(result)



