class Restaurant:
    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} offers great {self.cusine_type} food")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now officially open")


restaurant = Restaurant('coco', 'American')
restaurant.describe_restaurant()

restaurant1 = Restaurant('bobo', 'Mexican')
restaurant1.describe_restaurant()

restaurant2 = Restaurant('chco', 'Sudanese')
restaurant2.describe_restaurant()