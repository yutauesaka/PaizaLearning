N, Q = map(int, input().split())
numbers = [0]*N
intervals = [list(map(int, input().split())) for _ in range(Q)]
S = [0]*(N+1)

# 前処理
for i in range(Q):
    # 0-indexedに変換
    intervals[i][0] -= 1
    intervals[i][1] -= 1
    # 区間の始まりと終わり+1にそれぞれ1、-1を足す
    numbers[intervals[i][0]] += 1
    numbers[intervals[i][1]+1] -= 1

# 累積和S
for j in range(N):
    S[j+1] = S[j]+numbers[j]

print(max(S))
