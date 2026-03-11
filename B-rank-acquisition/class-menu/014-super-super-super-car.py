import sys
input = sys.stdin.readline


class Supercar:
    def __init__(self, l, f):
        self.l = l
        self.f = f
        self.distance = 0

    def run(self):
        if self.l > 0:
            self.l -= 1
            self.distance += self.f

    def print_distance(self):
        print(self.distance)


class Supersupercar(Supercar):
    def __init__(self, l, f):
        super().__init__(l, f)

    def fly(self):
        if self.l >= 5:
            self.l -= 5
            self.distance += self.f**2
        else:
            self.run()


class Supersupersupercar(Supersupercar):
    def __init__(self, l, f):
        super().__init__(l, f)

    def fly(self):
        if self.l >= 5:
            self.l -= 5
            self.distance += 2*self.f**2
        else:
            self.run()

    def teleport(self):
        if self.l >= self.f**2:
            self.l -= self.f**2
            self.distance += self.f**4
        else:
            self.fly()


N, K = map(int, input().split())
cars = [None]*N

for i in range(N):
    k, l, f = input().split()
    if k == "supercar":
        cars[i] = Supercar(int(l), int(f))
    elif k == "supersupercar":
        cars[i] = Supersupercar(int(l), int(f))
    elif k == "supersupersupercar":
        cars[i] = Supersupersupercar(int(l), int(f))

for _ in range(K):
    query = input().split()
    # 0-indexedに変換
    index = int(query[0])-1
    func = query[1]
    if func == "run":
        cars[index].run()
    elif func == "fly":
        cars[index].fly()
    elif func == "teleport":
        cars[index].teleport()

for car in cars:
    car.print_distance()
