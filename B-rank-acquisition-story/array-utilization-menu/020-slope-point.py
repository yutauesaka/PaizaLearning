# 定数格納とリスト作成
N = int(input())
M = list(map(int, input().split()))
A = [0]*N

# 点数計算
for i in range(N):
    scores = list(map(int, input().split()))
    for j in range(5):
        A[i] += M[j]*scores[j]

# 最も高得点の人を出力
print(max(A))
