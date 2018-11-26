from utils.base_expansion import get_base_b_expansion


def play(b, exponent, m):
    binary_exponent = get_base_b_expansion(exponent, 2)
    ret = modular_exponentiation(b, binary_exponent, m)
    print('({base} to the power {exponent} mod {m}) is: {ret}'.format(
        base=b,
        exponent=exponent,
        m=m,
        ret=ret
    ))


def modular_exponentiation(b, binary_exponent, m):
    """模指数运算，利用 n 的二进制展开式，详情看离散数学
    """
    result = 1
    power = b % m

    for a in reversed(binary_exponent):
        if a == 1:
            result = (result * power) % m
        power = (power * power) % m

    return result
