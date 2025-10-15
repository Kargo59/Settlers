import random

#module to assign random values to nodes in the catan game

random_dict = {
    'aaa': 1,
    'bbb': 1
}

print(random_dict)

fruits = ["Apple", "Pear", "Peach", "Banana"]
prices = [0.35, 0.40, 0.40, 0.28]

shuffled = random.shuffle(prices)
print(prices)

fruit_dictionary = dict(zip(fruits, (prices)))

print(fruit_dictionary)

