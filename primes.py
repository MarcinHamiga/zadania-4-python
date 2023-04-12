def primes(start = 1):
    while True:
        prime = True
        if start == 1:
            yield start
            start += 1
        else:
            for x in range(2, start//2):
                if start % x == 0:
                    prime = False
            if prime:
                yield start
                start += 1


generator = primes()
for x in range(20):
    print(next(generator))
