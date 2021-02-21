"""
Числа фибоначи f(0) = 1, f(1) = 1, f(2) = 2, f(i) = f(i-1) + f(i-2)
Выведите единственное число – последние k цифр числа Fn.
0 1
1 1
2 2
3 3
4 5
5 8
6 13
"""


def f(n, k):
    if n in [0, 1]:
        return 1
    previous, before_previous = 1, 1
    answer = 0
    for i in range(1, n):
        answer = (before_previous + previous) % 10**k
        before_previous = previous
        previous = answer

    return answer



if __name__ == '__main__':
    n, k = input().split()
    print(f(int(n), int(k)))