class Dog:

    all_dogs = [] 

    def __init__(self, breed: str, age: float, weight: float, name: str = "n/a", breedgroup: str = "n/a"): 
        self.breed = breed
        self.age = age
        self.weight = weight
        self.name = name
        self.breedgroup = breedgroup

        # Append each new dog to the list upon initialization
        Dog.all_dogs.append(self)

    def __repr__(self):  
        return f"{self.name}: ({self.breed} | {self.breedgroup} | {self.age} | {self.weight})" 

    def get_age(self): 
        return self.age

    
    total = 0
    @classmethod
    def sum_ages(cls):
        total = 0
        for dog in Dog.all_dogs:
            total += dog.age
        return total