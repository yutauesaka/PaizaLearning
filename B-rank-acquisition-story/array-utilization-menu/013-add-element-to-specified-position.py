# 定数格納とリスト作成
N = int(input())
A = [int(input()) for _ in range(N)]
n, B = map(int, input().split())

# 0-indexedに変換
n -= 1

# BをAのn番目の後ろに挿入
A.insert(n+1, B)

# 出力
for number in A:
    print(number)
