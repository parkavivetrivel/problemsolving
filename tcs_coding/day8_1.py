a = int(input())
c = 0
list_a = list(map(int, input().split()))
b = int(input())
for i in list_a:
    if list_a.count(i) == b:
        print(i)
        break
    else:
        print("-1")
        break
