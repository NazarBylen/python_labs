from abc import ABC, abstractmethod


class animal(ABC):

    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def print_name_and_2nd_arg(self):
        pass


class mammals(animal):

    def __init__(self, name: str, height: float):
        super().__init__(name)
        self.height = height

    def print_name_and_2nd_arg(self):
        print(f'name : {self._name}, height : {self.height}')


class bird(animal):

    def __init__(self, name: str, age: int = 0):
        super().__init__(name)
        self.age = age

    def print_name_and_2nd_arg(self):
        print(f'name : {self._name}, age : {self.age}')


class insect(animal):
    def __init__(self, _name: str, weight: float = 0):
        super().__init__(_name)
        self.weight = weight

    def print_name_and_2nd_arg(self):
        print(f'name : {self._name}, weight : {self.weight}')


class reptile(animal):

    def __init__(self, _name: str, legs: int = 0):
        super().__init__(_name)
        self.legs = legs

    def print_name_and_2nd_arg(self):
        print(f'name : {self._name}, number of legs : {self.legs}')


class fish(animal):

    def __init__(self, _name: str, type_of_skin: str = ''):
        super().__init__(_name)
        self.type_of_skin = type_of_skin

    def print_name_and_2nd_arg(self):
        print(f'name : {self._name}, type of skin : {self.type_of_skin}')
