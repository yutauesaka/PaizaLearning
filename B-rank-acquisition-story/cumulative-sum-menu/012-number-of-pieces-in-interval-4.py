N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = [None]*N
S = [0]*(N+1)

for i in range(N):
    if A[i] % 2 == 0:
        B[i] = 1
    else:
        B[i] = 0

for j in range(N):
    S[j+1] = S[j]+B[j]

print(S[Y+1]-S[X])
