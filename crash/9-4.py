class Restaurant:
    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{restaurant.restaurant_name} offers great {restaurant.cusine_type} food")

    def open_restaurant(self):
        print(f"{restaurant.restaurant_name} is now officially open")

    def set_number_served(self, customers):
        self.number_served = customers

    def increment_number_served(self, inc_customers):
        self.number_served += inc_customers


restaurant = Restaurant('coco', 'American')
print(restaurant.restaurant_name)
print(restaurant.cusine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(5)
restaurant.increment_number_served(25)
print(restaurant.number_served)