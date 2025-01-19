def eratosthenes_sieve(limit):
    primes = list(range(3, limit + 1, 2))
    for i in range(len(primes)):
        step = primes[i]
        if not step:
            continue
        i += step
        if i >= len(primes):
            break
        for j in range(i, len(primes), step):
            primes[j] = None
    primes = [2] + list(filter(None, primes))
    return primes

def main(*args, **kwargs):
    primes = eratosthenes_sieve(1000000)
    print(len(primes))
    print(primes[:10])
    print(primes[-5:])

if __name__ == '__main__':
    main()
