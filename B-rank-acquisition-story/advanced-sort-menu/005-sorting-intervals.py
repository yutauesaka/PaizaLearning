n, l, r = map(int, input().split())
a = list(map(int, input().split()))

# 0-indexedに変換
l -= 1
r -= 1

# 区間[l,r)だけソート
a = a[:l]+sorted(a[l:r])+a[r:]

print(*a)
