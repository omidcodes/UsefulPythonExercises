def recursive_fibo(n):
    if n <= 1:
        return n
    else:
        return (recursive_fibo(n - 1) + recursive_fibo(n - 2))
# ex : 0 1 1 2 3 5 8 13 21 34

if __name__ == '__main__':
    n = 10
    for i in range(n):
        print(recursive_fibo(i))
