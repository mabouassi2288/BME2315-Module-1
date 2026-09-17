from dog_Mona import *

dog1 = Dog("German Pinscher", 1, 43.0, "Rizzo")  
dog2 = Dog("Cavalier King Charles Spaniel", 2, 30.5, "Winston")
dog3 = Dog("Chihuahua", 2, 15.6, "Cheeto")

print(dog1)

print(dog2.age)

print(dog2.get_age())

print(Dog.sum_ages())