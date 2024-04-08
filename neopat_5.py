st = input()
intialize = 0
empty_list = []
sts = sorted(st)
for i in sts:
    if i.isnumeric():
        i = int(i)
        intialize += i
for j in sts:
    if j.isalpha():
        empty_list.append(j)
empty_list.append(str(intialize))
print(''.join(empty_list))