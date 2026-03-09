# 定数格納とリスト作成
N = int(input())
A = [int(input()) for _ in range(N)]
n = int(input())

# 0-indexedに変換
n -= 1

# Aのn番目を削除
A.pop(n)

# 出力
for number in A:
    print(number)
