N, Q = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(Q):
    query = list(input().split())
    direction = query[0]
    # 0-indexedに変換
    k = int(query[1])-1
    if direction == "update":
        x = int(query[2])
        A[k] = x
    elif direction == "get":
        print(sorted(A, reverse=True)[k])
