from itertools import combinations
# 定数格納とリスト作成
N = int(input())
A = [int(input()) for _ in range(N)]

# 二人を選んで身長差を比べる
pair = []
difference = 10**18
for a, b in combinations(A, 2):
    if abs(a-b) < difference:
        difference = abs(a-b)
        pair = [a, b]

# 二人組を昇順に出力する
pair.sort()
for person in pair:
    print(person)
