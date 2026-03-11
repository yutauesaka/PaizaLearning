import sys
input = sys.stdin.readline

N, X, P = map(int, input().split())
A = [int(input()) for _ in range(N)]

# Paiza君より小さい人の数
count = 0
for a in A:
    if P > a:
        count += 1

if P > X:
    count += 1

print(count+1)
