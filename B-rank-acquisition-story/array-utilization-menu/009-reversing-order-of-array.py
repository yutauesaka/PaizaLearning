# 定数格納とリスト作成
N = int(input())
A = [int(input()) for _ in range(N)]

# 逆向きに出力
for i in range(len(A)-1, -1, -1):
    print(A[i])
