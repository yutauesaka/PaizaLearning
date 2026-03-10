class Customer:
    checked_count = 0

    def __init__(self):
        self.total = 0

    def order_food(self, price):
        self.total += price

    def order_softdrink(self, price):
        self.total += price

    def order_alcohol(self, price):
        pass

    def order_beer(self, price=500):
        pass

    def check(self):
        Customer.checked_count += 1
        return self.total


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
            self.alcohol = True
            self.total += price

    def order_beer(self, price=500):
        if self.alcohol:
            self.total += price
        else:
            self.alcohol = True
            self.total += price


N, K = map(int, input().split())
customers = [None]*N

for i in range(N):
    age = int(input())
    if age >= 20:
        customers[i] = Adult()
    else:
        customers[i] = Customer()

for _ in range(K):
    query = input().split()
    # 0-indexedに変換
    index = int(query[0])-1
    order = query[1]
    if order == "food":
        price = int(query[2])
        customers[index].order_food(price)
    elif order == "softdrink":
        price = int(query[2])
        customers[index].order_softdrink(price)
    elif order == "alcohol":
        price = int(query[2])
        customers[index].order_alcohol(price)
    elif order == "0":
        customers[index].order_beer()
    else:
        print(customers[index].check())

# 帰った人数
print(Customer.checked_count)
