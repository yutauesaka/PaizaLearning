N = int(input())
A = list(map(int, input().split()))
S = [0]*(N+1)

# 累積和
for i in range(N):
    S[i+1] = S[i]+A[i]

# sum1とsum2の差の絶対値の最小値を求める
min_abs_dif = 10**18
for K in range(N):
    if K == 0 and N > 2:
        sum1 = 0
        sum2 = S[N-1+1]-S[K+1]
    elif K == N-1 and N > 2:
        sum1 = S[K+1]-S[0]
        sum2 = 0
    elif N == 2:
        sum1 = A[0]
        sum2 = A[1]
    else:
        sum1 = S[K+1]-S[0]
        sum2 = S[N-1+1]-S[K+1]
    if abs(sum1-sum2) < min_abs_dif:
        min_abs_dif = abs(sum1-sum2)

print(min_abs_dif)
