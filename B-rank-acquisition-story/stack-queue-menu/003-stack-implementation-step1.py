from collections import deque

Q = int(input())
A = deque()

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        A.append(query[1])
    else:
        A.pop()
    print(*A)
