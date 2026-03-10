# クラス定義


class Employee:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def get_number(self):
        return self.number

    def get_name(self):
        return self.name

    def change_number(self, new_number):
        self.number = new_number

    def change_name(self, new_name):
        self.name = new_name


# 定数格納とリスト作成
N = int(input())
employees = []

# クエリ
for _ in range(N):
    query = input().split()
    if query[0] == "make":
        _, number, name = query
        employees.append(Employee(number, name))
    elif query[0] == "getnum":
        _, index = query
        # 0-indexedに変換
        index = int(index)-1
        print(employees[index].get_number())
    elif query[0] == "getname":
        _, index = query
        # 0-indexedに変換
        index = int(index)-1
        print(employees[index].get_name())
    elif query[0] == "change_num":
        _, index, new_number = query
        # 0-indexedに変換
        index = int(index)-1
        employees[index].change_number(new_number)
    else:  # query[0] == "change_name"
        _, index, new_name = query
        # 0-indexedに変換
        index = int(index)-1
        employees[index].change_name(new_name)
