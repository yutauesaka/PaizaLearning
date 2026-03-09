n, q = map(int, input().split())
a = list(map(int, input().split()))
k = list(map(int, input().split()))

a.sort(reverse=True)

# k_i番目に大きい数をaから見つける
for k_i in k:
    # 0-indexedに変換
    k_i -= 1
    print(a[k_i])
