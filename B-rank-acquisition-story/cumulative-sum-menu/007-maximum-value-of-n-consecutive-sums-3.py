N = int(input())
A = list(map(int, input().split()))
S = [0]*(N+1)

for i in range(N):
    S[i+1] = S[i]+A[i]

max_sum = -10**18
for j in range(N+1-3):
    if S[j+3]-S[j] > max_sum:
        max_sum = S[j+3]-S[j]

print(max_sum)
