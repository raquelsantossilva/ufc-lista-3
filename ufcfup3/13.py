def funcao(x):
    a,b =0,1
    for i in range(1, 2):
        b=1
    for i in range(2, x+1):
        a, b = b, a+b
    return b

