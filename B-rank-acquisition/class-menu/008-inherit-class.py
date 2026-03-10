# クラス定義


class Customer:
    def __init__(self):
        self.total = 0

    def order_food(self, price):
        self.total += price

    def order_softdrink(self, price):
        self.total += price

    def order_alcohol(self, price):
        pass


class Adult(Customer):
    def __init__(self):
        super().__init__()
        self.alcohol = False

    def order_food(self, price):
        if self.alcohol:
            self.total += price-200
        else:
            self.total += price

    def order_alcohol(self, price):
        if self.alcohol:
            self.total += price
        else:
            self.total += price
            self.alcohol = True


# 定数格納とリスト作成
N, K = map(int, input().split())
customers = [None]*N

# オブジェクト生成
for i in range(N):
    age = int(input())
    if age >= 20:
        customers[i] = Adult()
    else:
        customers[i] = Customer()

# クエリ
for _ in range(K):
    index, order, price = input().split()
    # 0-indexedに変換
    index = int(index)-1
    # priceを数値に変換
    price = int(price)
    if order == "food":
        customers[index].order_food(price)
    elif order == "softdrink":
        customers[index].order_softdrink(price)
    else:  # order == "alcohol"
        customers[index].order_alcohol(price)

# 出力
for customer in customers:
    print(customer.total)
