class Human:
    def __init__(self, name="Human"):
        self.name = name


class Animal:
    def __init__(self, name="Animal"):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passenger = []

    def addpassenger(self, Animal ):
        self.passenger.append(Animal)

    def addpassenger(self, human, ):
        self.passenger.append(human)

    def print_name_passenger(self):
        if self.passenger != []:
            print(f"Name {self.brand} passenger:")
            for passenger in self.passenger:
                print(passenger.name)




        else:
            print(f"No passenger in {self.brand}")


hum1 = Human("Sers")
hum2 = Human("Jack")
hum3 = Human("Dima")

ani1 = Animal("Hank")
ani2 = Animal("барсик")
ani3 = Animal("Husku")

auto1 = Auto("Mercedes")
auto2 = Auto("Tatra")
auto3 = Auto("Tesla")

auto1.print_name_passenger()
auto2.print_name_passenger()
auto3.print_name_passenger()

auto1.addpassenger(hum1)
auto1.addpassenger(hum2)
auto1.addpassenger(hum3)
auto2.addpassenger(hum2)
auto2.addpassenger(hum3)



auto3.addpassenger(ani1)
auto3.addpassenger(ani2)
auto3.addpassenger(ani3)



auto1.print_name_passenger()
auto2.print_name_passenger()
auto3.print_name_passenger()