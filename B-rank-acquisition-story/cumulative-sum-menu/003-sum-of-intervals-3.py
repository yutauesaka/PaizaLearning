X, Y = map(int, input().split())
A = list(map(int, input().split()))
S = [0]*(len(A)+1)

for i in range(len(A)):
    S[i+1] = S[i]+A[i]

# A[X]からA[Y]までの和
print(S[Y+1]-S[X])
