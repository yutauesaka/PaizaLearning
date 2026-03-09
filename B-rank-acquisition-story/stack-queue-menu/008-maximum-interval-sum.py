import sys
from collections import deque

input = sys.stdin.readline

N, X = map(int, input().split())
A = list(map(int, input().split()))

intervals = deque(A[:X])
left_num = intervals[0]
interval_sum = sum(A[:X])
max_sum = interval_sum

for i in range(X, len(A)):
    intervals.append(A[i])
    interval_sum += A[i]-intervals.popleft()
    if interval_sum > max_sum:
        max_sum = interval_sum
        left_num = A[i-X+1]

print(max_sum, left_num)
