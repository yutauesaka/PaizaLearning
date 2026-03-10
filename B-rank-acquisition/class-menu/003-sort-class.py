# クラス定義


class User:
    def __init__(self, nickname, old, birth, state):
        self.nickname = nickname
        self.old = old
        self.birth = birth
        self.state = state


# 定数格納とリスト作成
N = int(input())
users = [None]*N

# オブジェクト生成
for i in range(N):
    nickname, old, birth, state = input().split()
    users[i] = User(nickname, int(old), birth, state)

# 年齢順にソート
users.sort(key=lambda x: x.old)

# 出力
for i in range(N):
    print(
        users[i].nickname,
        users[i].old,
        users[i].birth,
        users[i].state
    )
