N = int(input())
S = [input() for _ in range(N)]

S.sort(key=lambda x: (len(x), x))

for string in S:
    print(string)
