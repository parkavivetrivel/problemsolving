n = int(input())
list1 = list(map(int,input().split()))
m = int(input())
list2 = list(map(int,input().split()))
list3 = list1 + list2
a = sum(list3)
print("Total distance covered:",a,"units")