import sys
input = sys.stdin.readline

N, K, P = map(int, input().split())
A = [int(input()) for _ in range(N)]

# Paiza君より低い人たち
count = 0
for a in A:
    if P > a:
        count += 1

for _ in range(K):
    query = input().split()
    event = query[0]
    if event == "join":
        height = int(query[1])
        if P > height:
            count += 1
    elif event == "sorting":
        print(count+1)
