class Point:
    def __init__(self, character, path1, path2):
        self.character = character
        self.path1 = path1
        self.path2 = path2

    def go_to_path1(self):
        return self.path1

    def go_to_path2(self):
        return self.path2

    def get_character(self):
        return self.character


N, K, S = map(int, input().split())
points = [None]*N
spell = []

# 0-indexedに変換
now = S-1

for i in range(N):
    character, path1, path2 = input().split()
    # 0-indexedに変換してから代入
    points[i] = Point(character, int(path1)-1, int(path2)-1)

# スタート地点の文字を追加
spell.append(points[now].get_character())

for _ in range(K):
    path_to_choose = int(input())
    if path_to_choose == 1:
        now = points[now].go_to_path1()
    elif path_to_choose == 2:
        now = points[now].go_to_path2()
    spell.append(points[now].get_character())

# 呪文を言う
print("".join(spell))
