# success try id: 48467871


def key_trainer(game_field: str,
                one_person_power: int,
                cases: [str, list] = '123456789'):
    """
    Checks if keyboard data can be processed with twice 'power'
    """
    return sum(
        0 < game_field.count(timer) <= one_person_power * 2 for timer in cases
    )


def console_input():
    return int(input()), input() + input() + input() + input()


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
