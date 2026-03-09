N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

A.sort(key=lambda x: (x[0], x[1]))

for a in A:
    print(*a)
