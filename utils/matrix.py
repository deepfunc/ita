"""矩阵用数组表示的方式进行计算
"""
import number.power as power


def quick_square_matrix_power(matrix, exponent):
    """方阵快速幂算法，逻辑类似整数快速幂
    可以这样计算因为矩阵乘法是满足结合律的
    """
    n = len(matrix)
    ret = create_unit_matrix(n)

    while exponent != 0:
        if exponent & 1:
            ret = mul_matrix(matrix, ret)
        matrix = mul_matrix(matrix, matrix)
        exponent >>= 1

    return ret


def mul_matrix(matrix_a, matrix_b):
    """定义法求解矩阵相乘
    m x n，n x s，结果是 m x s
    """
    m = len(matrix_a)
    n = len(matrix_b)
    s = len(matrix_b[0])
    ret = create_empty_matrix(m, s)

    for i in range(m):
        for j in range(s):
            c_ij = 0
            for k in range(n):
                c_ij += matrix_a[i][k] * matrix_b[k][j]
            ret[i][j] = c_ij

    return ret


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


def mul_square_matrix_recursive(*,
                                matrix_a, row_range_of_matrix_a, col_range_of_matrix_a,
                                matrix_b, row_range_of_matrix_b, col_range_of_matrix_b):
    """递归分治计算矩阵相乘，两个矩阵必须是方阵并且 n 要是 2 的幂

    矩阵分块采用下标计算
    """
    n = len(row_range_of_matrix_a)
    if not power.is_power_of_2(n):
        raise ValueError('n of square_matrix must be power of 2!')

    matrix_ret = create_empty_square_matrix(n)

    if n == 1:
        matrix_ret[0][0] = \
            matrix_a[row_range_of_matrix_a.start][col_range_of_matrix_a.start] * \
            matrix_b[row_range_of_matrix_b.start][col_range_of_matrix_b.start]
    else:
        # C11 = A11 * B11 + A12 * B21
        add_matrix_by_idx(
            matrix_a=mul_square_matrix_recursive(
                matrix_a=matrix_a,
                row_range_of_matrix_a=range(
                    row_range_of_matrix_a.start,
                    row_range_of_matrix_a.start + len(row_range_of_matrix_a) // 2
                ),
                col_range_of_matrix_a=range(
                    col_range_of_matrix_a.start,
                    col_range_of_matrix_a.start + len(col_range_of_matrix_a) // 2
                ),
                matrix_b=matrix_b,
                row_range_of_matrix_b=range(
                    row_range_of_matrix_b.start,
                    row_range_of_matrix_b.start + len(row_range_of_matrix_b) // 2
                ),
                col_range_of_matrix_b=range(
                    col_range_of_matrix_b.start,
                    col_range_of_matrix_b.start + len(col_range_of_matrix_b) // 2
                ),
            ),
            matrix_b=mul_square_matrix_recursive(
                matrix_a=matrix_a,
                row_range_of_matrix_a=range(
                    row_range_of_matrix_a.start,
                    row_range_of_matrix_a.start + len(row_range_of_matrix_a) // 2
                ),
                col_range_of_matrix_a=range(
                    col_range_of_matrix_a.start + len(col_range_of_matrix_a) // 2,
                    col_range_of_matrix_a.stop
                ),
                matrix_b=matrix_b,
                row_range_of_matrix_b=range(
                    row_range_of_matrix_b.start + len(row_range_of_matrix_b) // 2,
                    row_range_of_matrix_b.stop
                ),
                col_range_of_matrix_b=range(
                    col_range_of_matrix_b.start,
                    col_range_of_matrix_b.start + len(col_range_of_matrix_b) // 2
                ),
            ),
            matrix_ret=matrix_ret,
            row_range_of_matrix_ret=range(0, n // 2),
            col_range_of_matrix_ret=range(0, n // 2)
        )

        # C12 = A11 * B12 + A12 * B22
        add_matrix_by_idx(
            matrix_a=mul_square_matrix_recursive(
                matrix_a=matrix_a,
                row_range_of_matrix_a=range(
                    row_range_of_matrix_a.start,
                    row_range_of_matrix_a.start + len(row_range_of_matrix_a) // 2
                ),
                col_range_of_matrix_a=range(
                    col_range_of_matrix_a.start,
                    col_range_of_matrix_a.start + len(col_range_of_matrix_a) // 2
                ),
                matrix_b=matrix_b,
                row_range_of_matrix_b=range(
                    row_range_of_matrix_b.start,
                    row_range_of_matrix_b.start + len(row_range_of_matrix_b) // 2
                ),
                col_range_of_matrix_b=range(
                    col_range_of_matrix_b.start + len(col_range_of_matrix_b) // 2,
                    col_range_of_matrix_b.stop
                ),
            ),
            matrix_b=mul_square_matrix_recursive(
                matrix_a=matrix_a,
                row_range_of_matrix_a=range(
                    row_range_of_matrix_a.start,
                    row_range_of_matrix_a.start + len(row_range_of_matrix_a) // 2
                ),
                col_range_of_matrix_a=range(
                    col_range_of_matrix_a.start + len(col_range_of_matrix_a) // 2,
                    col_range_of_matrix_a.stop
                ),
                matrix_b=matrix_b,
                row_range_of_matrix_b=range(
                    row_range_of_matrix_b.start + len(row_range_of_matrix_b) // 2,
                    row_range_of_matrix_b.stop
                ),
                col_range_of_matrix_b=range(
                    col_range_of_matrix_b.start + len(col_range_of_matrix_b) // 2,
                    col_range_of_matrix_b.stop
                ),
            ),
            matrix_ret=matrix_ret,
            row_range_of_matrix_ret=range(0, n // 2),
            col_range_of_matrix_ret=range(n // 2, n)
        )

        # C21 = A21 * B11 + A22 * B21
        add_matrix_by_idx(
            matrix_a=mul_square_matrix_recursive(
                matrix_a=matrix_a,
                row_range_of_matrix_a=range(
                    row_range_of_matrix_a.start + len(row_range_of_matrix_a) // 2,
                    row_range_of_matrix_a.stop
                ),
                col_range_of_matrix_a=range(
                    col_range_of_matrix_a.start,
                    col_range_of_matrix_a.start + len(col_range_of_matrix_a) // 2
                ),
                matrix_b=matrix_b,
                row_range_of_matrix_b=range(
                    row_range_of_matrix_b.start,
                    row_range_of_matrix_b.start + len(row_range_of_matrix_b) // 2
                ),
                col_range_of_matrix_b=range(
                    col_range_of_matrix_b.start,
                    col_range_of_matrix_b.start + len(col_range_of_matrix_b) // 2
                ),
            ),
            matrix_b=mul_square_matrix_recursive(
                matrix_a=matrix_a,
                row_range_of_matrix_a=range(
                    row_range_of_matrix_a.start + len(row_range_of_matrix_a) // 2,
                    row_range_of_matrix_a.stop
                ),
                col_range_of_matrix_a=range(
                    col_range_of_matrix_a.start + len(col_range_of_matrix_a) // 2,
                    col_range_of_matrix_a.stop
                ),
                matrix_b=matrix_b,
                row_range_of_matrix_b=range(
                    row_range_of_matrix_b.start + len(row_range_of_matrix_b) // 2,
                    row_range_of_matrix_b.stop
                ),
                col_range_of_matrix_b=range(
                    col_range_of_matrix_b.start,
                    col_range_of_matrix_b.start + len(col_range_of_matrix_b) // 2
                ),
            ),
            matrix_ret=matrix_ret,
            row_range_of_matrix_ret=range(n // 2, n),
            col_range_of_matrix_ret=range(0, n // 2)
        )

        # C22 = A21 * B12 + A22 * B22
        add_matrix_by_idx(
            matrix_a=mul_square_matrix_recursive(
                matrix_a=matrix_a,
                row_range_of_matrix_a=range(
                    row_range_of_matrix_a.start + len(row_range_of_matrix_a) // 2,
                    row_range_of_matrix_a.stop
                ),
                col_range_of_matrix_a=range(
                    col_range_of_matrix_a.start,
                    col_range_of_matrix_a.start + len(col_range_of_matrix_a) // 2
                ),
                matrix_b=matrix_b,
                row_range_of_matrix_b=range(
                    row_range_of_matrix_b.start,
                    row_range_of_matrix_b.start + len(row_range_of_matrix_b) // 2
                ),
                col_range_of_matrix_b=range(
                    col_range_of_matrix_b.start + len(col_range_of_matrix_b) // 2,
                    col_range_of_matrix_b.stop
                ),
            ),
            matrix_b=mul_square_matrix_recursive(
                matrix_a=matrix_a,
                row_range_of_matrix_a=range(
                    row_range_of_matrix_a.start + len(row_range_of_matrix_a) // 2,
                    row_range_of_matrix_a.stop
                ),
                col_range_of_matrix_a=range(
                    col_range_of_matrix_a.start + len(col_range_of_matrix_a) // 2,
                    col_range_of_matrix_a.stop
                ),
                matrix_b=matrix_b,
                row_range_of_matrix_b=range(
                    row_range_of_matrix_b.start + len(row_range_of_matrix_b) // 2,
                    row_range_of_matrix_b.stop
                ),
                col_range_of_matrix_b=range(
                    col_range_of_matrix_b.start + len(col_range_of_matrix_b) // 2,
                    col_range_of_matrix_b.stop
                ),
            ),
            matrix_ret=matrix_ret,
            row_range_of_matrix_ret=range(n // 2, n),
            col_range_of_matrix_ret=range(n // 2, n)
        )

    return matrix_ret


def add_matrix_by_idx(*,
                      matrix_a,
                      matrix_b,
                      matrix_ret, row_range_of_matrix_ret, col_range_of_matrix_ret):
    """矩阵加法

    注意是使用下标计算的
    """
    m = len(row_range_of_matrix_ret)
    n = len(col_range_of_matrix_ret)

    for i in range(m):
        for j in range(n):
            matrix_ret[row_range_of_matrix_ret.start + i][col_range_of_matrix_ret.start + j] = \
                matrix_a[i][j] + matrix_b[i][j]

    return matrix_ret
