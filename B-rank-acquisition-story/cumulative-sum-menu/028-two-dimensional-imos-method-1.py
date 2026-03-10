imos = [[0]*(5+1) for _ in range(5+1)]
y1 = [1, 2, 3, 3, 1]
x1 = [1, 2, 3, 1, 3]
y2 = [3, 4, 5, 5, 3]
x2 = [3, 4, 5, 3, 5]

# 前処理
for i in range(5):
    # 左上に+1
    imos[y1[i]-1][x1[i]-1] += 1
    # 右上の右隣に-1
    imos[y1[i]-1][x2[i]] -= 1
    # 左下の直下に-1
    imos[y2[i]][x1[i]-1] -= 1
    # 右下の1マス右下に+1
    imos[y2[i]][x2[i]] += 1

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
