#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sort.insertion
import sort.merge
import search.find_maximum_subarray
import number.power
import number.gcd
import number.modular_exponentiation
import number.modular_linear_equation
import search.binary_search_tree
import number.fibonacci
import utils.matrix as matrix
from enum import Enum


# sort.insertion.play()
# sort.merge.play()
# search.find_maximum_subarray.play()
# number.power.play_by_power_cd(3, 4)
# number.gcd.play_by_euclid(30, 21)
# number.gcd.play_by_gcd(30, 21)
# number.gcd.play_by_extended_gcd(30, 21)
# number.modular_exponentiation.play(3, 644, 645)
# number.modular_linear_equation.play(14, 30, 100)
# search.binary_search_tree.play()
# number.power.play_by_quick_power1(16, 10)
# number.fibonacci.play_fib1(6)
# number.fibonacci.play_fib2(6)
# number.fibonacci.play_fib3(12)

# a = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [1, 2, 3, 4],
#     [5, 6, 7, 8]
# ]
# b = [
#     [5, 6, 7, 8],
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [1, 2, 3, 4]
# ]
# a = [
#     [7, 8],
#     [9, 10]
# ]
# b = [
#     [11, 12],
#     [13, 14]
# ]
# print(matrix.mul_square_matrix_recursive(
#     matrix_a=a,
#     row_range_of_matrix_a=range(len(a)),
#     col_range_of_matrix_a=range(len(a[0])),
#     matrix_b=b,
#     row_range_of_matrix_b=range(len(b)),
#     col_range_of_matrix_b=range(len(b[0]))
# ))

class Month(Enum):
    Jan = 1
    Feb = 2
    Mar = 3
    Apr = 4
    May = 5
    Jun = 6
    Jul = 7
    Aug = 8
    Sep = 9
    Oct = 10
    Nov = 11
    Dec = 12


# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)
