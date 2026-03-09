import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

q = deque()

for a in A:

    while q and q[0] <= a - K:
        q.popleft()

    q.append(a)

    print(len(q))
