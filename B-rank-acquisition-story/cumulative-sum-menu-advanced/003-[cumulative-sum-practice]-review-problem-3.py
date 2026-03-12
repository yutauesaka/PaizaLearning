N, X, Y, C = input().split()
string = input()

# 整数に直す+0-indexedに変換
N = int(N)
X = int(X)-1
Y = int(Y)-1

Cs = [None]*N
S = [0]*(N+1)

# string[i]がCなら1,そうでなければ0
for i in range(N):
    if string[i] == C:
        Cs[i] = 1
    else:
        Cs[i] = 0

# 累積和
for j in range(N):
    S[j+1] = S[j]+Cs[j]

# string[X]からstring[Y]までのCの数
print(S[Y+1]-S[X])
