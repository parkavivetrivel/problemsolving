#print("%-20s%-20s%-20s" % ("Name", "Deposit", "Cost Per Day"))
n = int(input())
b = set()
for i in range(n):
    a = input().split(" ")
    c = "=".join(a)
    b.add(c)
b = sorted(b)
print("{"+", ".join(b)+"}")
