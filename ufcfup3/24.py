# n!/(n-k)!
def fatorial(x):
    fact = 1
    for i in range(1, x+1):
        fact *= i
    return fact

def comb(n, k):
    sub = n-k
    conta = fatorial(n)//(fatorial(sub)*fatorial(k))
    return conta


num = int(input(""))

for i in range(num):
    for j in range(i+1):
        print(comb(i, j), end=" ")
    print()
