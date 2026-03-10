# クラス定義


class Student:
    def __init__(self, name, old, birth, state):
        self.name = name
        self.old = old
        self.birth = birth
        self.state = state


# 定数格納とリスト作成
N = int(input())
students = [None]*N

# オブジェクト作成
for i in range(N):
    name, old, birth, state = input().split()
    students[i] = Student(name, int(old), birth, state)

# 定数格納
K = int(input())

# 年齢がKである生徒を探す
for i in range(N):
    if students[i].old == K:
        print(students[i].name)
