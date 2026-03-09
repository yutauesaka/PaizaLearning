import sys
input = sys.stdin.readline


def hash(s):
    p = 31
    mod = 10**9+7

    h = 0
    power = 1

    for c in s:
        h = (h+ord(c)*power) % mod
        power = power*p % mod
    return h % 100


N = int(input())

for _ in range(N):
    s = input().strip()
    print(hash(s))
