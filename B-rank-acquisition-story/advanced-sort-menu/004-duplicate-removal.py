n = int(input())
a = list(map(int, input().split()))

new_a = []

# 重複削除
for number in a:
    if number not in new_a:
        new_a.append(number)

new_a.sort()

print(*new_a)
