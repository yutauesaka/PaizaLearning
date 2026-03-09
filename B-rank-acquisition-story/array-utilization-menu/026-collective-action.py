# 定数格納とリスト作成
N, Q = map(int, input().split())
line = [person for person in range(1, N+1)]

# クエリ
for _ in range(Q):
    query = input().split()
    direction = query[0]
    if direction == "swap":
        # 0-indexedに変換
        a = int(query[1])-1
        b = int(query[2])-1
        line[a], line[b] = line[b], line[a]
    elif direction == "reverse":
        line = line[::-1]
    else:  # direction == "resize"
        c = int(query[1])
        if len(line) > c:
            line = line[:c]

# 出力
for student in line:
    print(student)
