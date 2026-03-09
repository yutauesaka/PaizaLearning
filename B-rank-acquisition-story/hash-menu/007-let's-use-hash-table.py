A, B = map(int, input().split())
Q = int(input())
hash_table = [[] for _ in range(100)]

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        hash_table[(A*query[1]+B) % 100].append(query[1])
    else:
        if query[1] in hash_table[(A*query[1]+B) % 100]:
            print("Yes")
        else:
            print("No")

for element in hash_table:
    print(*element)
