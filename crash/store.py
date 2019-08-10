class Store:
    def __init__(self, name):
        self.name = name
        self.item = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):

    @staticmethod
    def store_details(store):
