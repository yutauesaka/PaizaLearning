a, b = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(5)]
S = [[0]*(5+1) for _ in range(5+1)]

for y in range(5):
    for x in range(5):
        S[y+1][x+1] = A[y][x]+S[y][x+1]+S[y+1][x]-S[y][x]

# A[a][3]からA[b][3]までの和
print(
    S[b+1][3+1]
    - S[a][3+1]
    - S[b+1][3]
    + S[a][3]
)
