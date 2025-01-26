def eratosthenes_sieve(limit):
    primes = list(range(3, limit + 1, 2))
    for i in range(len(primes)):
        step = primes[i]
        if not step:
            continue
        i += step * (step >> 1)
        if i >= len(primes):
            break
        for j in range(i, len(primes), step):
            primes[j] = None
    primes = [2] + list(filter(None, primes))
    return primes

def is_prime(n):
    if n < 2:
        return False
    elif n <= 3:
        return True
    elif 1 != n % 6 != 5:
        return False
    for i in range(5, round(pow(n, .5)) + 1, 6):
        if not (n % i and n % (i + 2)):
            return False
    return True

def find_goldbach(n, primes=None):
    if primes is None:
        primes = eratosthenes_sieve(n >> 1)
    for i in primes:
        if is_prime(n - i):
            return (i, n - i)
    return None

def find_all_goldbach_pairs(n, primes=None):
    if primes is None:
        primes = eratosthenes_sieve(n >> 1)
    pairs = []
    for i in primes:
        if is_prime(n - i):
            pairs.append((i, n - i))
    return pairs

def main(*args, **kwargs):
    primes = eratosthenes_sieve(1000000)
    print(len(primes))
    print(primes[:10])
    print(primes[-5:])

if __name__ == '__main__':
    main()
