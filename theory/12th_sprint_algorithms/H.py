"""
Addition of binary numbers
"""

def main():
    with open('input.txt') as file:
        a, b = file.read().strip().split('\n')
        s3 = 0
        answer = ''
        for i in range(max(len(a), len(b)) + 1):
            # breakpoint()
            try:
                s1 = int(a[-i-1])
            except IndexError:
                s1 =0
            try:
                s2 = int(b[-i-1])
            except IndexError:
                s2 = 0
            if s1 + s2 + s3 < 2:
                answer += str(s1+s2 + s3)
                s3 = 0
            else:
                answer += str((s1 + s2 + s3) % 2)
                s3 = 1

        if answer[-1] == '0':
            answer = answer[:-1]
        print(answer[::-1])

if __name__ == '__main__':
    main()
