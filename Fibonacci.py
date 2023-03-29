from itertools import islice

class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        f = self.a
        self.a, self.b = self.b, self.a + self.b
        if f > self.n:
            raise StopIteration
        return f
    

def fibonacci_generator(n):
    Fib = Fibonacci(n)
    iterator = iter(Fib)
    try:
        while True:
            yield next(Fib)
    except StopIteration:
        pass

if __name__ == "__main__":
    for i in fibonacci_generator(100):
        print(i, end = " ")
    print()
    fibonacci = fibonacci_generator(10**10020)
    fibonacci_iterator = islice(iter(fibonacci), 10000, 10020, 1)

    with open("fibo.txt", "w") as f:
        for num in fibonacci_iterator:
            print(num)
            f.write(f"len:{len(str(num))}: {num}\n")
