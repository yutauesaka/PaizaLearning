A = list(map(int, input().split()))
S = [0]*(len(A)+1)

for i in range(len(A)):
    S[i+1] = S[i]+A[i]

# A[2]からA[7]までの和
print(S[7+1]-S[2])
