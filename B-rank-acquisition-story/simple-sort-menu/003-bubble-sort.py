n = int(input())
A = list(map(int, input().split()))

for i in range(n-1):
    for j in range(n-1, i, -1):
        if A[j-1] > A[j]:
            A[j-1], A[j] = A[j], A[j-1]
    print(*A)
