N, M, K = map(int, input().split())
imos = [[0]*(M+1) for _ in range(N+1)]
y1 = []
x1 = []
y2 = []
x2 = []

for _ in range(K):
    a, b, c, d = map(int, input().split())
    # 0-indexedに変換
    y1.append(b-1)
    x1.append(a-1)
    y2.append(d-1)
    x2.append(c-1)

# 前処理
for i in range(K):
    # 左上に+1
    imos[y1[i]][x1[i]] += 1
    # 右上+右1に-1
    imos[y1[i]][x2[i]+1] -= 1
    # 左下+下1に-1
    imos[y2[i]+1][x1[i]] -= 1
    # 右下+右1下1に+1
    imos[y2[i]+1][x2[i]+1] += 1

# 累積和(横)
for y_h in range(N):
    for x_h in range(M):
        imos[y_h][x_h+1] += imos[y_h][x_h]

# 累積和(縦)
for x_v in range(M):
    for y_v in range(N):
        imos[y_v+1][x_v] += imos[y_v][x_v]

# 最大値
print(max(max(row) for row in imos))
