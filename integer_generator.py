def positive_ints(start = 0):
    while True:
        yield start
        start += 1

def squares(start = 0):
    for i in positive_ints(start):
        yield i ** 2


def pythagorean_triples(start = 0):
    for c in positive_ints(start):
        for b in range(1, c):
            for a in range(1, b):
                if a ** 2 + b ** 2 == c ** 2:
                    yield (a, b ,c)


def select(iterable, n):
    result = []
    iterator = iter(iterable)
    for i in range(n):
        result.append(next(iterator))
    return result

if __name__ == "__main__":
    start = int(input("Podaj liczbę startową\n> "))
    end = int(input("Podaj ilość elementów\n> "))
    print(select(positive_ints(start), end))
    print(select(squares(start), end))
    print(select(pythagorean_triples(start), end))