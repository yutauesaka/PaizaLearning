# 定数格納とリスト作成
N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

# Bを作成
B = [number for number in A if number >= K]

# 出力
for number in B:
    print(number)
