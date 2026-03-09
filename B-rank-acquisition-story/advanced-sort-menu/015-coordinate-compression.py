import sys
import bisect
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
X = list(map(int, input().split()))

A.sort()

for x in X:
    i = bisect.bisect_left(A, x)
    if i < len(A) and A[i] == x:
        print(i+1)
