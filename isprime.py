def isprime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            print(n, 'equals', i, '*', n//i)
            break
    else:
        print(n, 'is a prime number')