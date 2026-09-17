from dog_Mona import *

import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statistics 


Dog.instantiate_from_csv("/Users/monaabouassi/Library/Mobile Documents/com~apple~CloudDocs/BME 2315/MODULE 1/BME2315-Module-1/MONA_ABOUASSI_MODULE 1 INDIVIDUAL ASSIGNMENT/dog data set.csv")

dog1 = Dog("German Pinscher", 1, 43.0, "Rizzo")  
dog2 = Dog("Cavalier King Charles Spaniel", 2, 30.5, "Winston")
dog3 = Dog("Chihuahua", 2, 15.6, "Cheeto")

print(dog1)

print(dog2.age)

print(dog2.get_age())

print(Dog.sum_ages())

with open("/Users/monaabouassi/Library/Mobile Documents/com~apple~CloudDocs/BME 2315/MODULE 1/BME2315-Module-1/MONA_ABOUASSI_MODULE 1 INDIVIDUAL ASSIGNMENT/dog data set.csv", newline="") as f:
    reader = csv.reader(f)
    headers = next(reader) # Get the first row
    for h in headers:
        print(h)

Dog.instantiate_from_csv("/Users/monaabouassi/Library/Mobile Documents/com~apple~CloudDocs/BME 2315/MODULE 1/BME2315-Module-1/MONA_ABOUASSI_MODULE 1 INDIVIDUAL ASSIGNMENT/dog data set.csv")

print(Dog.get_dog("Pug"))

working_dogs = range(len(Dog.filter(Dog.all_dogs, breedgroup = "Working")))

print(f'Number of Working Dog breeds = {len(working_dogs)}')

toy_dogs = range(len(Dog.filter(Dog.all_dogs, breedgroup = "Toy")))

print(f'Number of Toy Dog breeds = {len(toy_dogs)}')

age_Working_dogs = []
age_Toy_dogs = []

for dog in Dog.filter(Dog.all_dogs, breedgroup = "Working"):
    age_Working_dogs.append(dog.age)
for dog in Dog.filter(Dog.all_dogs, breedgroup = "Toy"):
    age_Toy_dogs.append(dog.age)

x_Working_dog_bar = (statistics.mean(age_Working_dogs))
x_Toy_dog_bar = (statistics.mean(age_Toy_dogs))

age_Working_dog_stdev = (statistics.stdev(age_Working_dogs))
age_Toy_dog_stdev = (statistics.stdev(age_Toy_dogs))

print(f'x_Working_dog_bar = {x_Working_dog_bar}, age_Working_dog_stdev {age_Working_dog_stdev}')
print(f'x_Toy_dog_bar = {x_Toy_dog_bar}, age_Toy_dog_stdev {age_Toy_dog_stdev}')

Dog_breedgroup_cols = ['Working Dogs', 'Toy Dogs']
mean_breedgroup = [x_Working_dog_bar, x_Toy_dog_bar]
stdev_breedgroup = [age_Working_dog_stdev, age_Toy_dog_stdev]
yerr = [np.zeros(len(mean_breedgroup)), stdev_breedgroup]

plt.bar(Dog_breedgroup_cols, mean_breedgroup, yerr=yerr, capsize=10, color=["blue", "orange"])
plt.title("Average Lifespan of Breedgroups")
plt.xlabel("Breedgroup")
plt.ylabel("Average Lifespan (age)")
plt.show()

#First, define two empty lists that will hold these data:

breed_age = []
breed_weight = []

#Next, fill these empty lists with data from the dataset. 

for dog in Dog.all_dogs:
    breed_age.append(dog.age)

for dog in Dog.all_dogs:
    breed_weight.append(dog.weight)

#Next, define the independent variable (which will be plotted on the x-axis) and the dependent variable (which will be plotted on the y-axis).

X = [breed_age]  # Independent variable
y = [breed_weight]   # Dependent variable

#Now we can visualize these data on our scatter plot, by typing the following:

plt.scatter(X, y, color='blue')
plt.xlabel('Average Lifespan')
plt.ylabel('Average Weight')
plt.title('Scatter Plot of Average Lifespan vs Average Weight')
plt.show()