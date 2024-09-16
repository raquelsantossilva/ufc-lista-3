def funcao(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    y = 0
    while fat > 0:
        y += fat % 10
        fat //= 10
    return y
