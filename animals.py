from abc import ABC, abstractmethod

class animal(ABC):

    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def print_name_and_2nd_arg(self):
        pass


class mammals(animal):
    height = ''

    def __init__(self, name: str, height: float):
        self.name = name
        self.height = height

    def print_name_and_2nd_arg(self):
        print(f'name : {self.name}, height : {self.height}')


class bird(animal):
    age = 0

    def __init__(self, _name : str, age: int):
        super().__init__(_name)
        self.age = age

    def print_name_and_2nd_arg(self):
        print(f'name : {self._name}, age : {self.age}')


class insect(animal):
    def __init__(self, _name : str, weight: float):
        super().__init__(_name)
        self.weight = weight

    def print_name_and_2nd_arg(self):
        print(f'name : {self._name}, weight : {self.weight}')


class reptile(animal):
    legs = 0

    def __init__(self, _name : str, legs: int):
        super().__init__(_name)
        self.legs = legs

    def print_name_and_2nd_arg(self):
        print(f'name : {self._name}, number of legs : {self.legs}')


class fish(animal):
    type_of_skin = ''

    def __init__(self, _name : str, type_of_skin: str):
        super().__init__(_name)
        self.type_of_skin = type_of_skin

    def print_name_and_2nd_arg(self):
        print(f'name : {self._name}, type of skin : {self.type_of_skin}')
