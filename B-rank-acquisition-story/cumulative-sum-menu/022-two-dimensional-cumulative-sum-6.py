N, M = map(int, input().split())
a, b, c, d = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
S = [[0]*(M+1) for _ in range(N+1)]

for y in range(N):
    for x in range(M):
        S[y+1][x+1] = A[y][x]+S[y][x+1]+S[y+1][x]-S[y][x]

# A[a][b]からA[c][d]までの和
print(
    S[c+1][d+1]
    - S[a][d+1]
    - S[c+1][b]
    + S[a][b]
)
