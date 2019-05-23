def hello():
    print('Hello, this is my fibo')

def fib(n):
    a = b = 1
    for i in range(n - 2):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    hello()
    for i in range(1,10):
        print(fib(i))