class User:
    
    def __init__(self, name, mail, age, money):
        self.name = name
        self.mail = mail
        self.age = age
        self.money = money
    
    def get_info(self):
        print(self.name)
        print(self.age)


admin = User('Admin', 'Fr@mail.ru', 20, 1000)
admin.get_info()