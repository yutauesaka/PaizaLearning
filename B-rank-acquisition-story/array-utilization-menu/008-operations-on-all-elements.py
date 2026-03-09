# 定数格納とリスト作成
N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

# すべての要素にKを足して出力
for number in A:
    print(number+K)
