N = int(input())
A = list(map(int, input().split()))
S = [0]*(N+1)

# 累積和
for i in range(N):
    S[i+1] = S[i]+A[i]

# 黒板に書かれた数字の最大値を求める
max_num = -10**18
num_on_board = 0
for j in range(1, N+1):
    num_on_board += S[j]
    if num_on_board > max_num:
        max_num = num_on_board

print(max_num)
