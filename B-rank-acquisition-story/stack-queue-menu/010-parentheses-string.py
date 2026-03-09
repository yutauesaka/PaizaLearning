import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()

count = 0

for c in S:
    if c == "(":
        count += 1
    else:
        count -= 1

    if count < 0:
        print("No")
        exit()

if count == 0:
    print("Yes")
else:
    print("No")
