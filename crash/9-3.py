class User:
    def __init__(self, first_name, last_name, email, title, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.title = title
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name} is a {self.age} years old {self.title} who lives in {self.city}")

    def greet_user(self):
        print(f"\nHello {self.first_name} {self.last_name}")


ammar = User('Ammar', 'Alim', 'A@gmail.com', 'Devops eng', 33, 'Seattle')
osman = User('Osman', 'Alim', 'O@gmail.com', 'SRE eng', 55, 'khartoum')
ali = User('Ali', 'Alim', 'Ali@gmail.com', 'Sec eng', 2, 'Seattle')

ammar.describe_user()
ammar.greet_user()
osman.describe_user()
osman.greet_user()
ali.describe_user()
ali.greet_user()