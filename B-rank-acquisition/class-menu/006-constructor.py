# クラス定義


class Employee:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def get_number(self):
        return self.number

    def get_name(self):
        return self.name


# 定数格納とリスト作成
N = int(input())
employees = []

# クエリ
for i in range(N):
    query = list(input().split())
    if query[0] == "make":
        _, number, name = query
        employees.append(Employee(number, name))
    elif query[0] == "getnum":
        _, index = query
        # 0-indexedに変換
        index = int(index)-1
        print(employees[index].get_number())
    else:  # query[0]が"getname"のとき
        _, index = query
        # 0-indexedに変換
        index = int(index)-1
        print(employees[index].get_name())
