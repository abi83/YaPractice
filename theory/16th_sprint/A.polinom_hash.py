"""
Hash = (s[1]*a**(n-1) + s[2]*a**(n-2)...s[n-1]*a+s[n]) mod m
"""


def polynomial_hash(base, module, string):
    my_hash = 0
    string_len = len(string)

    for n, s in enumerate(string):
        my_hash += ord(s)*(base**(string_len-n-1))

    return my_hash % module


if __name__ == '__main__':
    with open('input.txt') as file:
        a = int(file.readline())
        m = int(file.readline())
        s = file.readline()

    print(polynomial_hash(a, m, s))
