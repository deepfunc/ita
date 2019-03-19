"""矩阵用数组表示的方式进行计算
"""


def mul1_square_matrix(matrix_a, matrix_b):
    """定义法求解方阵相乘
    """
    n = len(matrix_a)
    matrix_c = create_empty_square_matrix(n)

    for i in range(n):
        for j in range(n):
            c_ij = 0
            for k in range(n):
                c_ij += matrix_a[i][k] * matrix_b[k][j]

    return matrix_c


def create_empty_square_matrix(n):
    """创建空的方阵
    """
    return [[0 for i in range[n]] for i in range(n)]
    pass
