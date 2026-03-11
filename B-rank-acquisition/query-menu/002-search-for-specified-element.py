import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = set(int(input()) for _ in range(N))

if K in A:
    print("YES")
else:
    print("NO")
