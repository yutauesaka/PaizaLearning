from collections import deque

Q = int(input())
A = deque()
B = deque()

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        if query[1] == 1:
            A.append(query[2])
        else:
            B.append(query[2])
    elif query[0] == 2:
        if query[1] == 1:
            print(A.popleft())
        else:
            print(B.popleft())
    else:
        print(len(A), len(B))
