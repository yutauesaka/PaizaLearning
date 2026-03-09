def hash(num):
    return num % 10


N = int(input())
hash_table = [[] for _ in range(10)]

for _ in range(N):
    x = int(input())
    hash_table[hash(x)].append(x)

for element in hash_table:
    print(*element)
