from collections import defaultdict

N, K = map(int, input().split())
numbers_and_IDs = defaultdict(lambda: "")

for _ in range(N):
    number, ID = input().split()
    numbers_and_IDs[number] = ID

for _ in range(K):
    query = input()
    print(numbers_and_IDs[query])
