from animals import *

animal = animal('Slavik')
mammals = mammals('Lyoxa', 45.6)
bird = bird(3)
insect = insect(0.5)
reptile = reptile(4)
fish = fish('dirty skin (idk what types of skin fish have))')

def print_animals():
    print(animal.name)
    mammals.print_name_and_height()
    bird.print_name_and_age()
    insect.print_name_and_weight()
    reptile.print_name_and_legs()
    fish.print_name_and_type_of_skin()


def main():
    print_animals()

if __name__ == '__main__':
    main()
