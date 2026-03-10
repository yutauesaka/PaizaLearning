numbers = [0]*10
N = int(input())
intervals = [list(map(int, input().split())) for _ in range(N)]
S = [0]*(10+1)

# 前処理
for i in range(N):
    # 0-indexedに変換
    intervals[i][0] -= 1
    intervals[i][1] -= 1
    # numbersの区間の始まりに1、終わり+1に-1を足す
    numbers[intervals[i][0]] += 1
    numbers[intervals[i][1]+1] -= 1

# 累積和
for j in range(len(numbers)):
    S[j+1] = S[j]+numbers[j]

print(max(S))
