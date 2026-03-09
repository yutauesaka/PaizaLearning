N, K = map(int, input().split())
A = list(map(int, input().split()))
S = [0]*(N+1)

for i in range(N):
    S[i+1] = S[i]+A[i]

max_sum = -10**18
for j in range(N+1-K):
    if S[j+K]-S[j] > max_sum:
        max_sum = S[j+K]-S[j]

print(max_sum)
