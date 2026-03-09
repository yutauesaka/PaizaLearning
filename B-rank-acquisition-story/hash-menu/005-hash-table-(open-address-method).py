def hash(num):
    return num % 10


N = int(input())
hash_table = [-1]*10

for _ in range(N):
    x = int(input())
    i = x
    while hash_table[hash(i)] != -1:
        i += 1
    hash_table[hash(i)] = x

for number in hash_table:
    print(number)
