N, K = map(int, input().split())
A = list(map(int, input().split()))

right = 0
count = 0
interval_sum = 0

for left in range(N):
    while right < N and interval_sum+A[right] <= K:
        interval_sum += A[right]
        right += 1

    count += right-left

    if left == right:
        right += 1
    else:
        interval_sum -= A[left]

print(count)
