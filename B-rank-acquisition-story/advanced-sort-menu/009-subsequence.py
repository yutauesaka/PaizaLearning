N, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)


def add_to_X(A, X):
    total = 0
    for i in range(len(A)):
        total += A[i]
        if total >= X:
            return i+1
    return -1


print(add_to_X(A, X))
