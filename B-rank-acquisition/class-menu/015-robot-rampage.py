class Robot:
    def __init__(self, x, y, level):
        self.x = x
        self.y = y
        self.level = level
        self.distance = [None, 1, 2, 5, 10]

    def go_to_north(self):
        self.y -= self.distance[self.level]

    def go_to_south(self):
        self.y += self.distance[self.level]

    def go_to_west(self):
        self.x -= self.distance[self.level]

    def go_to_east(self):
        self.x += self.distance[self.level]

    def level_up(self):
        self.level = min(4, self.level+1)

    def get_position(self):
        return (self.x, self.y)

    def print_status(self):
        print(self.x, self.y, self.level)


H, W, N, K = map(int, input().split())
robots = []
tools_x = []
tools_y = []

for _ in range(10):
    tx, ty = map(int, input().split())
    tools_x.append(tx)
    tools_y.append(ty)

for _ in range(N):
    rx, ry, rl = map(int, input().split())
    robots.append(Robot(rx, ry, rl))

for _ in range(K):
    query = input().split()
    # 0-indexedに変換
    index = int(query[0])-1
    direction = query[1]
    if direction == "N":
        robots[index].go_to_north()
    elif direction == "S":
        robots[index].go_to_south()
    elif direction == "W":
        robots[index].go_to_west()
    elif direction == "E":
        robots[index].go_to_east()
    # 道具の上か確認
    for i in range(10):
        if robots[index].get_position()[0] == tools_x[i] and robots[index].get_position()[1] == tools_y[i]:
            robots[index].level_up()

for robot in robots:
    robot.print_status()
