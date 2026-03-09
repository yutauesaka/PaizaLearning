# 定数格納とリスト作成
N, n = map(int, input().split())
A = [int(input()) for _ in range(N)]
new_A = []

# new_Aを作成
if n <= N:
    new_A = A[:n]
else:
    new_A = A[:n]+[0]*(n-N)

# 出力
for number in new_A:
    print(number)
