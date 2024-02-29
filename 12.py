list_sp =[]
no_of_shoes = input()
shoe_size = input().split()
no_of_customer = int(input())

for i in range(0, no_of_customer):
        size_and_price = input().split()
        list_sp.append(size_and_price)
for j in shoe_size:
    print(j)
for k in size_and_price:
    print(k)



