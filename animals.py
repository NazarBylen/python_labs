class animal:
    name = 'Slavik'

    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name


class mammals(animal):
    def __init__(self, name: str, height: float):
        self.name = name
        self.height = height

    def get_name_and_2nd_arg(self):
        return self.name, self.height


class bird(animal):
    def __init__(self, age: int):
        self.name = animal.get_name(animal)
        self.age = age

    def get_name_and_2nd_arg(self):
        return self.name, self.age


class insect(animal):
    def __init__(self, weight: float):
        self.name = animal.get_name(animal)
        self.weight = weight

    def get_name_and_2nd_arg(self):
        return self.name, self.weight


class reptile(animal):
    def __init__(self, legs: int):
        self.name = animal.get_name(animal)
        self.legs = legs

    def get_name_and_2nd_arg(self):
        return self.name, self.legs


class fish(animal):
    def __init__(self, type_of_skin: str):
        self.name = animal.get_name(animal)
        self.type_of_skin = type_of_skin

    def get_name_and_2nd_arg(self):
        return self.name, self.type_of_skin
