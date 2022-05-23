class animal:
    name = 'Slavik'

    def __init__(self, name: str):
        self.name = name


class mammals(animal):
    height = ''

    def __init__(self, name: str, height: float):
        super().__init__(name)
        self.height = height

    def print_name_and_height(self):
        print(f'name : {self.name}, height : {self.height}')


class bird(animal):
    age = 0

    def __init__(self, age: int):
        self.name = animal.name
        self.age = age

    def print_name_and_age(self):
        print(f'name : {self.name}, age : {self.age}')


class insect(animal):
    def __init__(self, weight: float):
        self.name = animal.name
        self.weight = weight

    def print_name_and_weight(self):
        print(f'name : {self.name}, weight : {self.weight}')


class reptile(animal):
    legs = 0

    def __init__(self, legs: int):
        self.name = animal.name
        self.legs = legs

    def print_name_and_legs(self):
        print(f'name : {self.name}, number of legs : {self.legs}')


class fish(animal):
    type_of_skin = ''

    def __init__(self, type_of_skin: str):
        self.name = animal.name
        self.type_of_skin = type_of_skin

    def print_name_and_type_of_skin(self):
        print(f'name : {self.name}, type of skin : {self.type_of_skin}')
