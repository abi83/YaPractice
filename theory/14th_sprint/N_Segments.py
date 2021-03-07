def segments_crossing(a, b) -> bool:
    if max(a) < min(b) or max(b) < min(a):
        return False
    return True


def segmentation(arr: list) -> list:
    segments = []
    print('base: ', arr)
    arr = set(tuple(x) for x in arr)
    print('set: ', arr)
    arr = list(list(x) for x in arr)
    print('list again', arr)
    arr.sort(key=lambda x: max(x))
    print('sorted', arr)
    for new_element in arr:
        changed = False
        for index in range(len(segments)):
            if segments_crossing(segments[index], new_element):
                segments[index] = [
                    min(segments[index]+new_element),
                    max(segments[index]+new_element)
                ]
                changed = True
        if not changed:
            segments.append(new_element)

    # segments.sort(key=lambda x: max(x))
    # return set(tuple(x) for x in segments)
    print('output: ', segments)
    return segments


if __name__ == '__main__':
    arr = []
    with open('input.txt') as file:
        n = int(file.readline())
        for i in range(n):
            arr.append([int(x) for x in file.readline().split()])

    answers = segmentation(arr)
    # print(answers)
    for answer in answers:
        # breakpoint()
        print(' '.join([str(x) for x in answer]))
        # breakpoint()
