# success try id: 47975118


def key_trainer(keyboard_data: str, one_person_power: int):
    """
    Checks if keyboard data can be processed with twice 'power'
    """
    return sum(
        [1 for y in '123456789' if (
                0 < keyboard_data.count(y) < one_person_power*2
        )]
    )


def key_trainer_2(keyboard_data: str, one_person_power: int):
    """
    Makes the same as key_trainer but with a more readable code
    """
    points = 0
    for symbol in '123456789':
        if 0 < keyboard_data.count(symbol) <= one_person_power*2:
            points += 1

    return points


def console_input():
    power = int(input())
    data = ''
    for line in range(0, 4):
        data += str(input())
    return power, data


def console_output(answer: [int, str]):
    print(answer)


def file_input():
    with open('input.txt') as file:
        power = int(file.readline().strip())
        data = file.read().strip().replace('\n', '')
    return power, data


def file_output(answer: [int, str]):
    with open('output.txt', 'w') as file:
        file.write(str(answer))


def main():
    power, data = console_input()
    points = key_trainer(data, power)
    console_output(points)


if __name__ == '__main__':
    main()
