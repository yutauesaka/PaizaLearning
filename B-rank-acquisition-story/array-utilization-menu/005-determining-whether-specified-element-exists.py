# 定数格納とリスト作成
N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

# Kが含まれているか判定
if K in A:
    print("Yes")
else:
    print("No")
