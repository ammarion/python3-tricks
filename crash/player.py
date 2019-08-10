# lottery_player_dict = {
#     'name': 'Ammar',
#     'numbers': (6,7,8,95,4)
# }
# class LotteryPlayer:
#     def __init__(self):
#         self.name = 'Ammar',
#         self.numbers = (5, 9, 12, 3, 1, 21)
#
#     def total(self):
#         return sum(self.numbers)
#
#
# player = LotteryPlayer()
#
# print(player.name)
# print(player.total())


# class Store:
#     def __init__(self, name):
#         self.name = name
#         self.items = []
#
#     def add_items(self, name, price):
#         item = {'name': name, 'price': price}
#         return self.items.append(item)
#
#     def stock_price(self):
#         return sum([item['price'] for item in self.items])
#
#
# store = Store('BestBuy')

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.makrs = []

    def average(self):
        return sum(self.makrs) / len(self.makrs)

    @staticmethod
    def go_to_school():
        print(f'I am going to school')



anna = Student("Anna", "MIT")
anna.makrs.append(56)
anna.makrs.append(71)
print(anna.average())
anna.go_to_school()

