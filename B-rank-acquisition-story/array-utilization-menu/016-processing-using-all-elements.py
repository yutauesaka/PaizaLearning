# 定数格納とリスト作成
N = int(input())
A = [int(input()) for _ in range(N)]

# 出力
for i in range(N):
    for j in range(i):
        print(A[i] * A[j])
