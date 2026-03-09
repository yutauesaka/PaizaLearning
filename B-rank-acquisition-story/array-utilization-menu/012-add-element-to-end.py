# 定数格納とリスト作成
N = int(input())
A = [int(input()) for _ in range(N)]
B = int(input())

# Aの末尾にBを加える
A.append(B)

# 出力
for number in A:
    print(number)
