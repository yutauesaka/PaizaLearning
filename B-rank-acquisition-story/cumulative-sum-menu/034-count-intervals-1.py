A = list(map(int, input().split()))

left = 0
right = 0
count = 0
interval_sum = 0

while left < len(A):

    while right < len(A) and interval_sum + A[right] <= 15:
        interval_sum += A[right]
        right += 1

    count += right - left

    if left == right:
        right += 1
    else:
        interval_sum -= A[left]

    left += 1

print(count)
