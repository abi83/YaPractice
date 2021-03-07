def biggest_union_number(numbers):
    temp_arr = [element for element in numbers]
    biggest_number = ''
    while temp_arr:
        max_ = max(temp_arr)
        temp_arr.remove(max_)
        biggest_number += max_
    return biggest_number


def key_generator(item, max_size=4):
    return (item*4)[:max_size]


if __name__ == '__main__':
    with open('input.txt') as file:
        n = file.readline()
        numbers = file.readline().split()
    print(biggest_union_number(numbers))
    numbers.sort(key=key_generator, reverse=True)
    print(''.join(numbers))