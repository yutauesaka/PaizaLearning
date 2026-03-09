from collections import deque
# 定数格納とリスト作成
N = int(input())
A = deque()

# クエリ
for _ in range(N):
    query = input().split()
    order = query[0]
    if order == "in":
        n = int(query[1])
        A.append(n)
    elif order == "out" and len(A) > 0:
        A.popleft()

# 出力
for number in A:
    print(number)
