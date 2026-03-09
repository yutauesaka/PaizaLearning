n = int(input())
a = list(map(int, input().split()))

sorted_a = sorted(a)

if sorted_a == a:
    print("Yes")
else:
    print("No")
