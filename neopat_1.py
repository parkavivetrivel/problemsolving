def min_steps_to_almost_same_strings(A, B, K):
    steps = 0
    for i in range(len(A)):
        diff = abs(ord(A[i]) - ord(B[i]))
        print(ord(A[i]),ord(B[i]),"a","b")
        print("d",diff)
        if diff > K:
            steps += 1
    return steps


# Input
A = input().strip()
B = input().strip()
K = int(input().strip())

# Output
print(min_steps_to_almost_same_strings(A, B, K))
