s_list = [1,4,77,77,77,88,88,2,2]
s_dict = {}
s_list1 = []
d =[]
for i in s_list:
    s_dict[i] = s_list.count(i)
#print(s_dict)
sorted_dict = dict(sorted(s_dict.items(), key=lambda item: item[1],reverse=True))
#print(sorted_dict)
for k,y in sorted_dict.items():
    for i in range(0,y):
        d.append(k)
print(d)
