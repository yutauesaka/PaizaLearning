K = int(input())
A = list(map(int, input().split()))

right = 0
count = 0
interval_sum = 0

for left in range(len(A)):
    # 合計がK以下なら右に伸ばす
    while right < len(A) and interval_sum+A[right] <= K:
        interval_sum += A[right]
        right += 1
    # 区間の数
    count += right-left
    # left=rightならスキップ
    if left == right:
        right += 1
    else:
        interval_sum -= A[left]

print(count)
