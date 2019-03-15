"""斐波那契数列的计算
"""


def play_fib1(n):
    print('fib1({n}) is {result}'.format(
        n=n,
        result=fib1(n)
    ))


def play_fib2(n):
    print('fib2({n}) is {result}'.format(
        n=n,
        result=fib2(n)
    ))


def fib1(n):
    """定义法递归求解
    """
    if n >= 2:
        return fib1(n - 1) + fib1(n - 2)
    elif n == 1:
        return 1
    else:
        # n == 0
        return 0
    pass


def fib2(n):
    """迭代法求解
    """
    if n <= 0:
        return 0

    x = 0
    y = 1
    i = 1

    # 保持循环不变式
    # x 是 f(i - 1)，是偶数如：2、4、6...
    # y 是 f(i)，是奇数如：3、5、7...
    while i < n:
        # 这一步左边 y 是 f(n - 1)，x 是 f(n - 2)
        x = y + x

        # 这一步左边 x 是 f(n - 1)，y 是 f(n - 2)
        y = x + y
        i += 2

    return y if i == n else x
    pass
