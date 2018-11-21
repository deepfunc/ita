def play_by_euclid(a, b):
    print('gcd({}, {}) by euclid(a, b) is: {}'.format(a, b, euclid(a, b)))


def play_by_gcd(a, b):
    print('gcd({}, {}) by gcd(a, b) is: {}'.format(a, b, gcd(a, b)))


def play_by_extended_gcd(a, b):
    d, x, y = extended_euclid(a, b)
    print('extended_gcd({a}, {b}) by extended_euclid(a, b) is: '
          '{d} = {a} * {x} + {b} * {y}'
          .format(a=a, b=b, d=d, x=x, y=y))


def euclid(a, b):
    """求最大公约数递归算法，运行时间为：O(lgb)，分析看算法导论 31 章内容
    """
    if b == 0:
        return a
    else:
        return euclid(b, a % b)
    pass


def gcd(a, b):
    """求最大公约数非递归算法
    """
    x, y = a, b

    while y != 0:
        r = x % y
        x = y
        y = r

    return x


def extended_euclid(a, b):
    """扩展欧几里得算法，同时求得贝祖恒等式
    """
    if b == 0:
        return a, 1, 0
    else:
        d1, x1, y1 = extended_euclid(b, a % b)
        d, x, y = d1, y1, x1 - (a // b) * y1
        return d, x, y
    pass
