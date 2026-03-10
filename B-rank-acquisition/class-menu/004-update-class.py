# クラス定義


class User:
    def __init__(self, nickname, old, birth, state):
        self.nickname = nickname
        self.old = old
        self.birth = birth
        self.state = state

    def change_nickname(self, new_nickname):
        self.nickname = new_nickname


# 定数格納とリスト作成
N, K = map(int, input().split())
users = [None]*N

# オブジェクト生成
for i in range(N):
    nickname, old, birth, state = input().split()
    users[i] = User(nickname, old, birth, state)

# 名前変更
for _ in range(K):
    values = input().split()
    # 0-indexedに変換
    number = int(values[0])-1
    new_nickname = values[1]
    users[number].change_nickname(new_nickname)

# 出力
for i in range(N):
    print(
        users[i].nickname,
        users[i].old,
        users[i].birth,
        users[i].state
    )
