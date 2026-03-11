import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = set(int(input()) for _ in range(N))

for _ in range(Q):
    K = int(input())
    if K in A:
        print("YES")
    else:
        print("NO")
