# クラス定義


class User:
    def __init__(self, nickname, old, birth, state):
        self.nickname = nickname
        self.old = old
        self.birth = birth
        self.state = state


# 定数格納とリスト生成
N = int(input())
users = [None]*N

# オブジェクト生成
for i in range(N):
    nickname, old, birth, state = input().split()
    users[i] = User(nickname, old, birth, state)

# 出力
for i in range(N):
    print("User{")
    print(f"nickname : {users[i].nickname}")
    print(f"old : {users[i].old}")
    print(f"birth : {users[i].birth}")
    print(f"state : {users[i].state}")
    print("}")
