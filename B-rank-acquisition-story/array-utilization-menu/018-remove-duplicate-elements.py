# 定数格納とリスト作成
N = int(input())
A = [int(input()) for _ in range(N)]
B = []

# Aの要素を重複なくもつBを作る
for number in A:
    if number not in B:
        B.append(number)

# 出力
for number in B:
    print(number)
