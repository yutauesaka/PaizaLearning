Q = int(input())
divisible_nums = [0]*1000
S = [0]*1001

for i in range(1, 1001):
    if i % 3 == 0 and i % 5 == 0:
        divisible_nums[i-1] = 1

for j in range(1000):
    S[j+1] = S[j]+divisible_nums[j]

for _ in range(Q):
    l, r = map(int, input().split())
    # 0-indexedに変換
    l -= 1
    r -= 1
    print(S[r+1]-S[l])
