N, A, B = map(int, input().split())
string = input()
Ps = [0]*N
S = [0]*(N+1)

# 0-indexedに変換
A -= 1
B -= 1

# 1文字後が"i"で2文字後が"z"な"p"の数を数える
for i in range(N):
    if i+2 < N:
        if string[i] == "p" and string[i+1] == "i" and string[i+2] == "z":
            Ps[i] = 1

# 累積和
for j in range(N):
    S[j+1] = S[j]+Ps[j]

if B+1-2 < A:
    print(0)
else:
    print(S[B+1-2]-S[A])
