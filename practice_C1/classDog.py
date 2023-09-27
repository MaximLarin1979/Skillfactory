from classCat import Cat
class Dog(Cat):
    def get_pet(self):
        return f'{self.get_name()} {self.get_age()}'

dog_1 = Dog("Felix", "boy", 2)

print(dog_1.get_pet())