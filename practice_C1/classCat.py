class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    def get_age(self):
        return self.age

class Client:
    def __init__(self, f_name, s_name, city, balance):
        self.f_name = f_name
        self.s_name = s_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'Client : {self.f_name} {self.s_name}. {self.city}. Баланс: {self.balance} руб.'

client1 = Client("Иван", "Петров", "Москва", 50)
print(client1)