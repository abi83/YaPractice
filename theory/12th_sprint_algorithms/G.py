"""
From decimal to binary
"""

def main():
    with open('input.txt') as file:
        data = int(file.read().strip())
        answer = ''
        while data != 0:
            answer += str(data % 2)
            data = data // 2

        print(answer[::-1])


if __name__ == '__main__':
    main()