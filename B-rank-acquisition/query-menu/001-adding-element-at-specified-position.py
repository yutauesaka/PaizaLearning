N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(N)]

# 0-indexedに変換
K -= 1

A.insert(K+1, Q)

for a in A:
    print(a)
