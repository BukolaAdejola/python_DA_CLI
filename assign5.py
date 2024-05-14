class Person():
 
    def __init__(self, name, weight, age, gender, height, profession):
        self.name = name
        self.weight = weight
        self.age = age
        self.gender = gender
        self.height = height
        self.profession = profession

    def running(self):
        '''
        weight (20 - 40) = 60kph
        weight (40 - 60) = 50kph
        weight (60 - 80) = 40kph
        weight (80 - 100) = 20kph
        weight >=100 = very slow
        '''
        if self.weight >= 100:
            print(f'The {self.name.capitalize()} speed is very slow')
        elif self.weight >= 80:
            print(f'The {self.name.capitalize()} speed is 20kph')
        elif self.weight >= 60:
            print(f'The {self.name.capitalize()} speed is 40kph')
        elif self.weight >= 40:
            print(f'The {self.name.capitalize()} speed is 50kph')
        elif self.weight >= 20:
            print(f'The {self.name.capitalize()} speed is a 60kph')
        else:
            print(f'The {self.name.capitalize()} speed is normal')


Person1 = Person(
    name = 'Chike',
    age = 18,
    gender = 'male',
    weight = 65,
    profession = 'Doctor',
    height = ''
    )

print(Person1.name)
print(Person1.weight)
print(Person1.running())