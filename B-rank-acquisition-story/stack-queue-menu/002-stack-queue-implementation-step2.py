Q = int(input())
A = []

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        A.append(query[1])

print(len(A))
for a in A:
    print(a)
