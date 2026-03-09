A = [1, 5, 9, 7, 5, 3, 2, 5, 8, 4]
B = [None]*len(A)
S = [0]*(len(B)+1)

# Bに1(偶数)または0(奇数)をいれる
for i in range(len(A)):
    if A[i] % 2 == 0:
        B[i] = 1
    else:
        B[i] = 0

# Bの累積和Sを取る
for j in range(len(B)):
    S[j+1] = S[j]+B[j]

# A[2]からA[7]までの偶数の数を求める
print(S[7+1]-S[2])
