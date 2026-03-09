string = "bwwbwbbwbwbb"
B = [None]*len(string)
S = [0]*(len(B)+1)

# "b"なら1をBに入れる
for i in range(len(string)):
    if string[i] == "b":
        B[i] = 1
    else:
        B[i] = 0

# Bの中の1の累積和S
for j in range(len(B)):
    S[j+1] = S[j]+B[j]

# 3文字目から8文字目=string[2]からstring[7]までの"b"の個数
print(S[8-1+1]-S[3-1])
