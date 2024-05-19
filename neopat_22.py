a = 3
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c = []
#d = 0 why wrong when it is declared globaly
saddle = False
for i in range(0, len(b)):
    least_row_value = min(b[i])
    tempIndex = b[i].index(min(b[i]))
    d = 0
    for j in range(0, len(b)):
        if least_row_value >= b[j][tempIndex]:
            d += 1
    if d == len(b):
        print(i, tempIndex,least_row_value)
        saddle = True
        break
if not saddle:
    print("no saddle point")
