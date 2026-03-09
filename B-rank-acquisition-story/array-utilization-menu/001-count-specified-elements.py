from collections import Counter

# 定数格納とリスト生成
N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

# カウンターを作成
counter = Counter(A)

# Kの数を出力
print(counter[K])
