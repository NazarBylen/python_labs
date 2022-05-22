from animals import *

animal = animal('Slavik')
mammals = mammals('Lyoxa', 45.6)
bird = bird(3)
insect = insect(0.5)
reptile = reptile(4)
fish = fish('dirty skin (idk what types of skin fish have))')


def print_animals():
    print(animal.name)
    print(mammals.get_name_and_2nd_arg())
    print(bird.get_name_and_2nd_arg())
    print(insect.get_name_and_2nd_arg())
    print(reptile.get_name_and_2nd_arg())
    print(fish.get_name_and_2nd_arg())


print_animals()
