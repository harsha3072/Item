class Item:
    def __init__(self, name, price, category):
        if price <= 0:
            raise ValueError("Invalid value for price, got {}".format(price))
        self.name = name
        self.price = price
        self.category = category

    def get_detail(self):
        return "{}@{}-{}".format(self.name, self.price, self.category)


def default_test():
    item = Item(name="Oreo Biscuits", price=30, category="Food")
    print(item.name)  # prints "Oreo Biscuits"
    print(item.price)  # prints '30'
    print(item.category)  # prints "Food"
    print(item.get_detail())  # prints "Oreo Biscuits@30-Food"
