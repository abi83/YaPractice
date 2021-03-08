def count_sort(arr):
    counts = {
        '0': 0,
        '1': 0,
        '2': 0,
    }
    for element in arr:
        counts[element] += 1
    answer = []
    for value, number in counts.items():
        answer += [value] * number
    return answer


if __name__ == '__main__':
    with open('input.txt') as file:
        n = file.readline()
        arr = file.readline().split()

    print(*count_sort(arr), sep=' ')
