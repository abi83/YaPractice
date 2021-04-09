import string
import random


def polynomial_hash(string, base=1000, module=123_987_123):
    my_hash = 0
    string_len = len(string)

    for n, s in enumerate(string):
        my_hash += ord(s)*(base**(string_len-n-1))

    return my_hash % module


def string_generator(size=8, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))


hashes = {}
mem = 0

while True:
    a = string_generator(random.randint(4, 20))
    try:
        if hashes[polynomial_hash(a)] != a:
            print(hashes[polynomial_hash(a)], a)
            break
    except KeyError:
        hashes[polynomial_hash(a)] = a

    # showing used memory
    if hashes.__sizeof__() // 1024 > mem:
        mem = hashes.__sizeof__() // 1024
        print(mem)

