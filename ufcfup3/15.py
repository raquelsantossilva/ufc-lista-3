def funcao(n):
    num = 1
    num1 = 1
    for i in range(1, n+1):
        num *= i
        num1 += 1/num

    return num1