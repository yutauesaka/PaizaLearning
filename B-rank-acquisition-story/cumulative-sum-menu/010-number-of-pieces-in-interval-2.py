A = list(map(int, input().split()))
B = [None]*len(A)
S = [0]*(len(B)+1)

# 偶奇判定をBにいれる
for i in range(len(A)):
    if A[i] % 2 == 0:
        B[i] = 1
    else:
        B[i] = 0

# Bの累積和S
for j in range(len(B)):
    S[j+1] = S[j]+B[j]

# A[2]からA[7]までの偶数の数
print(S[7+1]-S[2])
