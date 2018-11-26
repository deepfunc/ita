def get_base_b_expansion(n, b):
    """构造 b 进制展开式
    """
    q = n
    result = []

    while q != 0:
        result.insert(0, q % b)
        q = q // b

    return result
