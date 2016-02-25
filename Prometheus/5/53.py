n = 9
m = 11
def super_fibonacci(n, m):
    if m == 0:
        return 0
    if m == 1:
        return 1
    if m >= n:
        return 1
    if m > 1 and m < n:
        fibo = []
        fibo.append(0)
        for i in range(m):
            fibo.append(1)
        position = m + 1
        fib = 0
        while position <= n:
            j = m
            fib = 0
            while j > 0:
                fib = fib + fibo[position - j]
                j = j - 1
            fibo.append(fib)
            position = position + 1
    return fibo[n]

def superFib1(n, m):
    A = [0]
    for i in range(m):
        A.append(1)
    i = m
    while i<=n:
        mm = i
        sum = 0
        looper = m - 1
        while looper >= 0:
            sum += A[mm]
            mm -= 1
            looper -= 1
        A.append(sum)
        i += 1
    return A[n]

print super_fibonacci(n, m)
print superFib1(n, m)