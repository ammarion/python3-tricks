class Restaurant:
    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type

    def describe_restaurant(self):
        print(f"{restaurant.restaurant_name} offers great {restaurant.cusine_type} food")

    def open_restaurant(self):
        print(f"{restaurant.restaurant_name} is now officially open")


restaurant = Restaurant('coco', 'American')
print(restaurant.restaurant_name)
print(restaurant.cusine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()