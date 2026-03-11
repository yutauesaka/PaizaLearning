import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = deque(int(input()) for _ in range(N))

A.popleft()

for a in A:
    print(a)
