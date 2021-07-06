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


if __name__ == '__main__':
    power, data = int(input()), input() + input() + input() + input()
    points = key_trainer(data, power)
    print(points)
