# 定数格納とリスト作成
N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

# Kが何番目か探す
kth = -1
for i in range(len(A)):
    if A[i] == K:
        # 1-indexedに変換
        kth = i+1
        break

# 出力
print(kth)
