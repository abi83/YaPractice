def uglify(text):
    answer = ''
    even = True
    for index in range(len(text)):
        if even:
            answer += text[index].lower()
        else:
            answer += text[index].upper()
        even = not even

    return answer


if __name__ == '__main__':
    text = 'Some random text to uglify'
    print(uglify(text))