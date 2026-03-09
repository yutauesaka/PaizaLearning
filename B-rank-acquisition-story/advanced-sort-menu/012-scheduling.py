n = int(input())
intervals = []

for _ in range(n):
    l, r = map(int, input().split())
    intervals.append((l, r))

# 終了日でソート
intervals.sort(key=lambda x: x[1])

count = 0
last_end = 0

for l, r in intervals:
    if l > last_end:
        count += 1
        last_end = r

print(count)
