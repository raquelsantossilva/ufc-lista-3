def fat(m):
    fact = 1
    for i in range(1, m+1):
        fact *= i
    return fact

def funcao(x, n):
    conta = 0
    for i in range(n+1):
        conta += (-1)**i * (x**(2*i+1)/fat(2*i+1))
    return conta
