import sys
input = sys.stdin.readline


class Brave:
    def __init__(self, l, h, a, d, s, c, f):
        self.l = l
        self.h = h
        self.a = a
        self.d = d
        self.s = s
        self.c = c
        self.f = f

    def level_up(self, h, a, d, s, c, f):
        self.l += 1
        self.h += h
        self.a += a
        self.d += d
        self.s += s
        self.c += c
        self.f += f

    def muscle_training(self, h, a):
        self.h += h
        self.a += a

    def running(self, d, s):
        self.d += d
        self.s += s

    def study(self, c):
        self.c += c

    def pray(self, f):
        self.f += f

    def print_status(self):
        print(
            self.l,
            self.h,
            self.a,
            self.d,
            self.s,
            self.c,
            self.f
        )


N, K = map(int, input().split())
braves = [None]*N

for i in range(N):
    l, h, a, d, s, c, f = map(int, input().split())
    braves[i] = Brave(l, h, a, d, s, c, f)

for _ in range(K):
    query = input().split()
    # 0-indexedに変換
    index = int(query[0])-1
    event = query[1]
    if event == "levelup":
        h, a, d, s, c, f = int(query[2]), int(query[3]), int(
            query[4]), int(query[5]), int(query[6]), int(query[7])
        braves[index].level_up(h, a, d, s, c, f)
    elif event == "muscle_training":
        h, a = int(query[2]), int(query[3])
        braves[index].muscle_training(h, a)
    elif event == "running":
        d, s = int(query[2]), int(query[3])
        braves[index].running(d, s)
    elif event == "study":
        c = int(query[2])
        braves[index].study(c)
    elif event == "pray":
        f = int(query[2])
        braves[index].pray(f)

for brave in braves:
    brave.print_status()
