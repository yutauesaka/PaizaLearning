import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

stack = []

for a in A:
    stack.append(a)
    while len(stack) >= 2 and stack[-1] == stack[-2]:
        v = stack.pop()
        stack.pop()
        stack.append(v*2)

for ball in reversed(stack):
    print(ball)
