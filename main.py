import collections
from recordclass import RecordClass
from dataclasses import dataclass
import itertools
import numpy as np

def sep():
    print("-" * 30)
#All Cars
cars_input = [["Suzuki", "SX4", [4300, 1765, 1585], 117, 11, 5.4],
        ["Suzuki", "GrandVitara", [4175, 1775, 1610], 140, 9.5, 7],
        ["Suzuki","Jimny", [3645, 1645, 1725], 102, 10.3, 7.7],
        ["Audi","Q5", [4682, 2140, 1662], 140, 7.6, 6.3],
        ["Audi","Q2", [4484, 2024, 1616], 102, 9.6, 7],
        ["Audi","Q7", [5052, 2212, 1741], 210, 6.5, 6.7]]

# Task 1
with open('input.txt', 'r', encoding='utf-8') as f:
    str = ''
    for line in f:
        for i in line:
            if i.isalpha():
                str+=i.lower()
cnt = collections.Counter(str)
res1 = cnt.most_common(5)
print(res1)
sep()

# Task 2
Car = collections.namedtuple('Car', ['producer', 'model', 'dimensions', 'engine_power', 'time100', 'consumption100'])
cars = [Car(*inp) for inp in cars_input]

# Task 3
def dinamic(cars):
    return sorted(cars, key=lambda car: car.time100)[:3]

def highest(cars):
    return sorted(cars, key=lambda car: car.dimensions[2], reverse=True)[:3]
print("Highest: ", highest(cars))
print("Best dinamic: ", dinamic(cars))
sep()

# Task 4
class CarRc(RecordClass):
    producer: str
    model: str
    dimensions: list
    engine_power: float
    time100: float
    consumption100: float

    def boost(self):
        self.engine_power*=1.1

cars_rc = [CarRc(*inp) for inp in cars_input]
print("Before boost: \n", dinamic(cars_rc))
print("After boost:")
for car in cars_rc:
    car.boost()
print(dinamic(cars_rc))
sep()

# Task 5
@dataclass
class CarDc():
    producer: str
    model: str
    dimensions: list
    engine_power: float
    time100: float
    consumption100: float

    def transform_cons(self):
        return 235.21/self.consumption100

cars_dc = [CarDc(*inp) for inp in cars_input]
print("In 100km/l: ")
for car in cars_dc:
    print(car.consumption100)
print("In m/g: ")
for car in cars_dc:
    print(car.transform_cons())
sep()

# Task 6
def get_all_combinations():
    return [temp for temp in itertools.product(range(1,7),repeat=2)]

def make_sum(all_combinations):
    return [combination[0]+combination[1] for combination in all_combinations]


all_combinations = get_all_combinations()
print("All combinations: \n", all_combinations)
sum_of_combination = make_sum(all_combinations)
print(sum_of_combination)
print("Most popular sum: ")
most_popular = collections.Counter(sum_of_combination).most_common(3)
print(most_popular)
for tup in most_popular:
    print("Sum ", tup[0], " appears ", tup[1]," times")
sep()

# Task 7
my_data = np.genfromtxt('iris.csv', delimiter=',')
my_data = np.select([my_data>=3, my_data<3], [my_data, -my_data])
print(my_data)

