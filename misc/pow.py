# pow.py

def pow(x, n):
    def power(x, n):
        if n == 0:
            return 1
        v = power(x, n / 2)
        if n % 2 == 0:
            return v * v
        else:
            return v * v * x
    if n < 0:
        return 1 / power(x, -n)
    else:
        return power(x, n)

print pow(2, 2)

