N, A, B = map(int, input().split())
array = list(map(int, input().split()))
S = [0]*(N+1)

# 累積和を求める
for i in range(N):
    S[i+1] = S[i]+array[i]

# array[A]からarray[B]までの和
print(S[B+1]-S[A])
