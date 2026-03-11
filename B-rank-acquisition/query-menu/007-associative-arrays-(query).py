import sys
from collections import defaultdict
input = sys.stdin.readline

N, K = map(int, input().split())
numbers_and_IDs = defaultdict(lambda: "")

for _ in range(N):
    number, ID = input().split()
    numbers_and_IDs[number] = ID

for _ in range(K):
    query = input().split()
    event = query[0]
    if event == "join":
        numbers_and_IDs[query[1]] = query[2]
    elif event == "leave":
        del numbers_and_IDs[query[1]]
    elif event == "call":
        print(numbers_and_IDs[query[1]])
