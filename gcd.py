import sys

m = int(sys.argv[1])
n = int(sys.argv[2])

def gcd(m,n):
    while n != 0:
        r = m % n
        m = n
        n = r

    return m

print("GCD = %d" % gcd(m, n))




