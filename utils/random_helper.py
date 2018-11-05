import random


def get_random_numbers_lte_100(length):
    return random.sample(range(101), length)


def get_random_numbers_gte_negative100_lte_100(length):
    return random.sample(range(-100, 101), length)
