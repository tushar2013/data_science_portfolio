#!/home/neo/anaconda3/bin/python

class Car:
    def __init__(self, make, model, variant, speedo, manufacture_year):
        self.make = make
        self.model = model
        self.variant = variant
        self.__speedo = speedo
        self.__manufacture_year = manufacture_year

    def get_make(self):
        '''
        This is a public function, which return the make of the car.
        '''
        return self.make.upper()

    def get_model(self):
        '''
        This is a public function, which return the model of the car.
        '''
        return self.model.upper()

    def get_variant(self):
        '''
        This is a public function, which return the variant of the car.
        '''
        return self.variant.upper()

    def get_speedo(self):
        '''
        This is a public function, which return the no. on the speedometer of the car.
        '''
        return self.__speedo

    def __get_manufacture_year(self):
        '''
        This is a private function, which return the manufacture year of the car.
        '''
        return self.__manufacture_year

new_car = Car('skoda', 'kushaq', 'monte carlo', 1000, 2022)

print(f'Getting the make of the car using get_make() function')
print(new_car.get_make())
print('------------------------------------------------------')
print(f'Getting the make of the car using make variable')
print(new_car.make)
print('======================================================')
print(f'Getting the model of the car using get_model() function')
print(new_car.get_model())
print('------------------------------------------------------')
print(f'Getting the model of the car using model variable')
print(new_car.model)
print('======================================================')
print(f'Getting the variant of the car using get_variant() function')
print(new_car.get_variant())
print('------------------------------------------------------')
print(f'Getting the variant of the car using variant variable')
print(new_car.variant)
print('======================================================')
print(f'Getting the speedo of the car using get_speedo() function')
# Since it is a public function it can be called normally.
print(new_car.get_speedo())
print('------------------------------------------------------')
print(f'Getting the speedo of the car using __speedo variable')
# Since this variable is private it cannot be called normally.
# new_car.__speedo
print(new_car._Car__speedo)
print('======================================================')
print(f'Getting the manufacture_year of the car using get_manufacture_year() function')
print(new_car._Car__get_manufacture_year())
# Since this function is private it cannot be called normally.
# new_car.__get_manufacture_year()
print('------------------------------------------------------')
print(f'Getting the manufacture_year of the car using __manufacture_year variable')
print(new_car._Car__manufacture_year)
# Since this varuable is private it cannot be called normally.
# new_car.__manufacture_year
print('======================================================')
