# 定数格納とリスト作成
N = int(input())
A = [int(input()) for _ in range(N)]
X, Y = map(int, input().split())

# 0-indexedに変換
X -= 1
Y -= 1

# 入れ替え
A[X], A[Y] = A[Y], A[X]

# 出力
for number in A:
    print(number)
