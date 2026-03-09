# 定数格納とリスト作成
N, K, F = map(int, input().split())
A = [int(input()) for _ in range(K)]

# 残ったブルーシート(0~F-1を取った後)
sheets = A[F:]

# 残っている人
people = []
for person in sheets:
    if person not in people:
        people.append(person)

# 出力
for person in people:
    print(person)
