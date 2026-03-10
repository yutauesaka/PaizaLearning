imos = [[0]*(5+1) for _ in range(5+1)]
N = int(input())
y1 = []
x1 = []
y2 = []
x2 = []

for _ in range(N):
    a, b, c, d = map(int, input().split())
    y1.append(b)
    x1.append(a)
    y2.append(d)
    x2.append(c)

# 前処理
for i in range(N):
    # 0-indexedに変換
    y1[i] -= 1
    x1[i] -= 1
    y2[i] -= 1
    x2[i] -= 1
    # 左上に+1
    imos[y1[i]][x1[i]] += 1
    # 右上+右1に-1
    imos[y1[i]][x2[i]+1] -= 1
    # 左下+下1に+1
    imos[y2[i]+1][x1[i]] -= 1
    # 右下+右1下1に+1
    imos[y2[i]+1][x2[i]+1] += 1

# 累積和(横)
for y_h in range(5):
    for x_h in range(5):
        imos[y_h][x_h+1] += imos[y_h][x_h]

# 累積和(縦)
for x_v in range(5):
    for y_v in range(5):
        imos[y_v+1][x_v] += imos[y_v][x_v]

# 最大値
print(max(max(row) for row in imos))
