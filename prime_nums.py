def generate_primes(ceiling: int):
    primes = [True] * (ceiling+1)
    primes[0] = primes[1] = False
    
    for i in range(2, int(ceiling**0.5)+1):
        if primes[i]:
            for j in range(i*i, ceiling+1, i):
                primes[j] = False

    for i in range(2, ceiling+1):
        if primes[i]:
            yield i

if __name__ == '__main__':
    n = input("Do której liczby chcesz szukać liczb pierwszych?\n> ")
    for prime in generate_primes(int(n)):
        print(prime)