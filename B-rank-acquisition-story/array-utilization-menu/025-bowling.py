# リスト作成
temp = [list(map(int, input().split())) for _ in range(4)]
pins = []

# 扱いやすいように並べ替える
for i in range(3, -1, -1):
    for j in range(3-i, -1, -1):
        pins.append(temp[i][j])

# ピンの数と次に狙うピンを決める
pin_to_aim = -1
count = 0
for i in range(len(pins)):
    if pins[i] == 1:
        if pin_to_aim == -1:
            pin_to_aim = i+1
        count += 1

# 出力
print(pin_to_aim)
print(count)
