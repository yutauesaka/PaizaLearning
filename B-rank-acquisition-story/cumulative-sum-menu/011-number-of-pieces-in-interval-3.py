X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = [None]*len(A)
S = [0]*(len(B)+1)

for i in range(len(A)):
    if A[i] % 2 == 0:
        B[i] = 1
    else:
        B[i] = 0

for j in range(len(B)):
    S[j+1] = S[j]+B[j]

print(S[Y+1]-S[X])
