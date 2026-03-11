class Player:
    def __init__(self, hp, F1, A1, F2, A2, F3, A3):
        self.hp = hp
        self.F1 = F1
        self.A1 = A1
        self.F2 = F2
        self.A2 = A2
        self.F3 = F3
        self.A3 = A3

    def get_status(self, technique):
        if technique == 1:
            return (self.hp, self.F1, self.A1)
        elif technique == 2:
            return (self.hp, self.F2, self.A2)
        elif technique == 3:
            return (self.hp, self.F3, self.A3)

    def enhance(self):
        if not (self.F1 == 0 and self.A1 == 0):
            self.F1 = max(1, self.F1-3)
            self.A1 += 5
        if not (self.F2 == 0 and self.A2 == 0):
            self.F2 = max(1, self.F2-3)
            self.A2 += 5
        if not (self.F3 == 0 and self.A3 == 0):
            self.F3 = max(1, self.F3-3)
            self.A3 += 5

    def calc_damage(self, damage):
        self.hp -= damage


N, K = map(int, input().split())
players = [None]*N

for i in range(N):
    hp, F1, A1, F2, A2, F3, A3 = map(int, input().split())
    players[i] = Player(hp, F1, A1, F2, A2, F3, A3)

for _ in range(K):
    P1, T1, P2, T2 = map(int, input().split())
    # 0-indexedに変換
    P1 -= 1
    P2 -= 1
    # どちらか一方が退場してたらスキップ
    if players[P1] == None or players[P2] == None:
        continue
    # どちらも攻撃技を使ったとき
    if players[P1].get_status(T1)[1] != 0 and players[P2].get_status(T2)[1] != 0:
        # P1の方が技の発生が遅いとき
        if players[P1].get_status(T1)[1] > players[P2].get_status(T2)[1]:
            players[P1].calc_damage(players[P2].get_status(T2)[2])
        # P2の方が技の発生が遅いとき
        elif players[P1].get_status(T1)[1] < players[P2].get_status(T2)[1]:
            players[P2].calc_damage(players[P1].get_status(T1)[2])
    # P1だけが強化技を使ったとき
    elif players[P1].get_status(T1)[1] == 0 and players[P2].get_status(T2)[1] != 0:
        players[P1].enhance()
        players[P1].calc_damage(players[P2].get_status(T2)[2])
    # P2だけが強化技を使ったとき
    elif players[P1].get_status(T1)[1] != 0 and players[P2].get_status(T2)[1] == 0:
        players[P2].enhance()
        players[P2].calc_damage(players[P1].get_status(T1)[2])
    # 両方とも強化技を使ったとき
    else:
        players[P1].enhance()
        players[P2].enhance()
    # hpが0以下なら退場
    if players[P1].get_status(T1)[0] <= 0:
        players[P1] = None
    if players[P2].get_status(T2)[0] <= 0:
        players[P2] = None

# 生き残ってるプレイヤーの数を求める
alive_count = 0
for player in players:
    if player:
        alive_count += 1

print(alive_count)
