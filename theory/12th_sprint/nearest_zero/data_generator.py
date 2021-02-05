from random import randint


with open('input.txt', 'w') as file:
    n = int(file.readline().strip())
    street = map(int, file.readline().strip().split())
