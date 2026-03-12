N = int(input())
A = list(map(int, input().split()))

# 左累積最大
left = [-10**18]*(N+1)
for i in range(N):
    left[i+1] = max(left[i], A[i])

# 右累積最大
right = [-10**18]*(N+1)
for i in range(N-1, -1, -1):
    right[i] = max(right[i+1], A[i])

for K in range(1, N-1):
    max1 = left[K]
    max2 = right[K+1]
    print(min(max1, max2))
