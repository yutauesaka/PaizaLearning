N, A, B, MOD = map(int, input().split())

for _ in range(N):
    x = int(input())
    print((A*x+B) % MOD)
