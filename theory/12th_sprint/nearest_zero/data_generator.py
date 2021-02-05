from random import randint


with open('input.txt', 'w') as file:
    n = randint(0, 1_000_000)
    street = map(int, file.readline().strip().split())
