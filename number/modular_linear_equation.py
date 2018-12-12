from number.gcd import extended_euclid


def play(a, b, n):
    ret = solver(a, b, n)
    solution = '{a}x ≡ {b} (mod {n}), {ret}'
    if type(ret) == str:
        print(solution.format(a=a, b=b, n=n, ret=ret))
    else:
        print(solution.format(a=a, b=b, n=n, ret='has solutions:'))
        print(ret)


def solver(a, b, n):
    (d, x, y) = extended_euclid(a, n)
    if b % d == 0:
        t = (x * (b // d)) % n
        ret = []

        for i in range(d):
            ret.append((t + i * (n // d)) % n)

        return ret
    else:
        return 'no solutions.'
    pass
