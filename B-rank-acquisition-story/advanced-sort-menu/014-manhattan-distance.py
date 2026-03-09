N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

points.sort(key=lambda x: abs(x[0])+abs(x[1]))

for point in points:
    print(*point)
