def funcao(n, k):
    f1 = 1
    f2 = 1
    var = n - k
    vft = 1
    conta = 1
    for i in range(1, n+1):
        f1 *= i
    for i in range(1, k+1):
        f2 *= i
    for i in range(1, var + 1):
        vft *= i
    conta = f1/(f2 * vft)
    return conta


