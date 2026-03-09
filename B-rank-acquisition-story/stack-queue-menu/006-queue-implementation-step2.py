from collections import deque

Q = int(input())
A = deque()

for _ in range(Q):
    query = list(input().split())
    if query[0] == "1":
        A.append(query[1])
    else:
        print(A.popleft())
    print(*A)
