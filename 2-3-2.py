def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def primes():
    value = 2
    while True:
        if is_prime(value):
            yield value
        value += 1
