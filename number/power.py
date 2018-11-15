def play(base, exponent):
    print('%d to the power %d is %d' % (base, exponent, power(base, exponent)))


def power(base, exponent):
    """用分治算法求乘方，最坏运行时间为: O(lgn)
    """
    if exponent == 1:
        return base

    if exponent % 2 == 0:
        ret = power(base, exponent / 2)
        return ret * ret
    else:
        ret = power(base, (exponent - 1) / 2)
        return ret * ret * base
    pass
