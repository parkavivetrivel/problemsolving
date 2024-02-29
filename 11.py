def solve(s):
    empty = []
    words = s.split()
    for i in words:
        if i[0].isalpha():
            case = i.title()
            empty.append(case)
        elif i[0].isnumeric():
            empty.append(i)
    return ' '.join(empty)
print(solve("132 456 Wq  m e"))