N, K = map(int, input().split())
A = list(map(int, input().split()))
S = [0]*(N+1)

# 累積和を求める
for i in range(N):
    S[i+1] = S[i]+A[i]

interval_sum = 0

# K個の範囲を一つずつ右にずらす
for right in range(K, N):
    left = right-K
    if S[right]-S[left] > interval_sum:
        interval_sum = S[right]-S[left]

print(interval_sum)
