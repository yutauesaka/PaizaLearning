# 九九表を出力
for i in range(1, 10):
    for j in range(1, 10):
        if j < 9:
            print(i*j, end=" ")
        else:
            print(i*j)
