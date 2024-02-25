import random

random_integers = [random.randint(1, 1000) for _ in range(250)]

random_integers.reverse()

print(random_integers)