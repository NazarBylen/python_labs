from animals import *

mammals = mammals('Lyoxa', 45.6)
bird = bird('Oleksandr', 3)
insect = insect('Oleksiy', 0.5)
reptile = reptile('Oleksandr', 4)
fish = fish('Oleksandr', 'dirty skin (idk what types of skin fish have))')

def print_animals():
    mammals.print_name_and_2nd_arg()
    bird.print_name_and_2nd_arg()
    insect.print_name_and_2nd_arg()
    reptile.print_name_and_2nd_arg()
    fish.print_name_and_2nd_arg()


def main():
    print_animals()

if __name__ == '__main__':
    main()
