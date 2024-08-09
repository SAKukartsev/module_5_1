class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_flor):
        if new_flor > self.number_of_floors or new_flor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_flor + 1):
                print(i)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
print(h1.name)
h1.go_to(5)
print(h2.name)
h2.go_to(10)