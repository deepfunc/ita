"""矩阵用数组表示的方式进行计算
"""


def play_test():
    # a = [[1, 2, 9], [3, 4, 10]]
    # b = [[5, 6], [7, 8], [11, 12]]
    a = [[1, 2],
         [3, 4]]
    b = [[123, 456],
         [777, 888]]
    print(mul1_matrix(a, b))


# def quick_square_matrix_power1(matrix, n_of_matrix, exponent):
#     """方阵快速幂算法，逻辑类似整数快速幂
#     可以这样计算因为矩阵乘法是满足结合律的
#     """
#     ret = create_unit_matrix(n_of_matrix)
#
#     while exponent != 0:
#         if exponent & 1:
#             ret =
#         a *= a
#         b >>= 1
#
#     return ret


def mul1_matrix(matrix_a, matrix_b):
    """定义法求解矩阵相乘
    m x n，n x s，结果是 m x s
    """
    m = len(matrix_a)
    n = len(matrix_b)
    s = len(matrix_b[0])
    matrix_c = create_empty_matrix(m, s)

    for i in range(m):
        for j in range(s):
            c_ij = 0
            for k in range(n):
                c_ij += matrix_a[i][k] * matrix_b[k][j]
            matrix_c[i][j] = c_ij

    return matrix_c


def create_empty_square_matrix(n):
    """创建空的方阵
    """
    return create_empty_matrix(n, n)


def create_empty_matrix(m, n):
    """创建空的矩阵
    """
    return [[0 for j in range(n)] for i in range(m)]


def create_unit_matrix(n):
    """创建单位矩阵
    """
    return [[0 if i != j else 1 for j in range(n)] for i in range(n)]
