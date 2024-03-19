def creatingStack():
    stack = []
    return stack


def push(stack, item):
    stack.append(item)
    return stack


def pop(stack):
    return stack.pop()


def length(stack):
    return len(stack)


creatingStack()
a = creatingStack()
print(push(a, 12))
print(push(a, 14))
print(pop(a))

