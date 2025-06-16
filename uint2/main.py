import uint2.oop.ex233, uint2.oop.ex234, uint2.oop.ex242
from uint2.Haython import *


def main233():
    one = uint2.oop.ex233.Ferret("Yellow")
    two = uint2.oop.ex233.Ferret()
    one.birthday()
    print(one.get_name())
    one.set_name("Sam2")
    print(one.get_name())
    print(two.get_name())
    print(uint2.oop.ex233.Ferret.count_animals)


def main234():
    p = uint2.oop.ex234.Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()


def main242():
    thing = uint2.oop.ex242.BigThing(7)
    print(f"{thing.size()}")
    cutie = uint2.oop.ex242.BigCat("mitzy", 7)
    print(cutie.size())


def main25():
    zoo_lst = [Dog("Brownie", 10), Cat("Zelda", 3), Skunk("Stinky", 0), Unicorn("Keith", 7), Dragon("Lizzy", 1450)]
    zoo_lst.extend([Dog("Doggo", 80), Cat("Kitty", 80), Skunk("Stinky Jr.", 80), Unicorn("Clair", 80), Dragon("McFly", 80)])
    for animal in zoo_lst:
        if animal.is_hungry():
            print(f"{type(animal).__name__} {animal.get_name()}")
            while animal.is_hungry():
                animal.feed()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        else:
            animal.breath_fire()
    print(Animal.zoo_name)


def main():
    main233()
    main234()
    main242()
    main25()


if __name__ == '__main__':
    main()

