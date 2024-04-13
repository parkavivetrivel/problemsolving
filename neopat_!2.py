n = int(input())
b = {}
g = 0
for i in range(n):
    a = input()
    b[a] = int(input())
d = sorted(b.keys())
print("After sorting the employee names:")
for i in d:
    print(i + "-" + str(b[i]))
e = list(b.values())
e.sort()
print("After sorting the salary:")
for k in range(len(e)):
    for key ,value in b.items():
        if str(e[k]) == str(value):
            print(key + "-" + str(value))
