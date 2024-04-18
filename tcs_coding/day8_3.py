a = list(input())
n = int(input())
b = []
for i in range(0,len(a), n):
    print(i,"i")
    b.append(a[i])
for j in range(1,len(a),n):
    print(j,"j")
    b.append(a[j])
print("".join(b))