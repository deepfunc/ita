def play_by_power_cd(base, exponent):
    print('{base} to the power {exponent} by power_cd(base, exponent) is {result}'.format(
        base=base,
        exponent=exponent,
        result=power_cd(base, exponent)
    ))


def power_cd(base, exponent):
    """用分治算法求乘方，最坏运行时间为: O(lgn)
    """
    if exponent == 1:
        return base

    if exponent % 2 == 0:
        ret = power_cd(base, exponent / 2)
        return ret * ret
    else:
        ret = power_cd(base, (exponent - 1) / 2)
        return ret * ret * base
    pass
