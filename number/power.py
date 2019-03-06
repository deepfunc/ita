def play_by_power_cd(base, exponent):
    print('{base} to the power {exponent} by power_cd(base, exponent) is {result}'.format(
        base=base,
        exponent=exponent,
        result=power_cd(base, exponent)
    ))


def play_by_power_quick1(base, exponent):
    print('{base} to the power {exponent} by power_quick1(a, b) is {result}'.format(
        base=base,
        exponent=exponent,
        result=power_quick1(base, exponent)
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


def power_quick1(a, b):
    """快速幂算法之一

    指数可以转换为二进制表示，例如：
    11 的二进制是 1011，11 = 2³×1 + 2²×0 + 2¹×1 + 2º×1
    这个算法从二进制的右边开始遍历，如果最右边是 1 则结果乘以 a
    每次循环结尾将 a 翻倍，这个在纸上验算一下就知道。还有将 b 右移一位，开始判断下一位

    时间复杂度分析
    传统算法是乘 n 次，时间复杂度是 O(n)
    而这个算法把 n 次循环变为二进制表示的位数循环，比如 1111 是 15，跟位数的关系是 2 的 4 次方减 1
    所以时间复杂度是 O(lgn)
    """
    ret = 1

    while b != 0:
        if b & 1:
            ret *= a
        a *= a
        b >>= 1

    return ret
