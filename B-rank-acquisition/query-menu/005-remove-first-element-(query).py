import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
A = deque(int(input()) for _ in range(N))

for _ in range(K):
    S = input().strip()
    if S == "pop":
        A.popleft()
    elif S == "show":
        for a in A:
            print(a)
