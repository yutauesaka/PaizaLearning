N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
S = [0]*(N+1)

for i in range(N):
    S[i+1] = S[i]+A[i]

# A[X]からA[Y]までの和
print(S[Y+1]-S[X])
