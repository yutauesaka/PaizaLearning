n, k = map(int, input().split())
a = list(map(int, input().split()))

# 0-indexedに変換
k -= 1

print(sorted(a, reverse=True)[k])
