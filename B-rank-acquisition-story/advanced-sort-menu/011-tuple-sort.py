N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 0-indexedに変換
K -= 1

A.sort(key=lambda row: (row[K],)+tuple(row))

for a in A:
    print(*a)
