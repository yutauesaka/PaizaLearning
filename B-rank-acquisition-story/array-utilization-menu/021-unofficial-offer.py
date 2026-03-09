# 定数格納とリスト作成
N, K, M = map(int, input().split())
A = [int(input()) for _ in range(N)]

# 合格者だけのリスト
passed = [score for score in A if score >= K]

# M人に辞退された後
hired = max(len(passed)-M, 0)

# 雇える人数
print(hired)
