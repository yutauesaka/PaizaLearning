from collections import deque

N = int(input())
A = list(input().split())

stack = deque()

for a in A:
    if a == "+":
        addend_right = int(stack.pop())
        addend_left = int(stack.pop())
        stack.append(addend_left+addend_right)
    elif a == "-":
        subtrahend = int(stack.pop())
        minuend = int(stack.pop())
        stack.append(minuend-subtrahend)
    else:
        stack.append(int(a))

print(*stack)
