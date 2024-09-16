def funcao(n):
    serie = 0
    for i in range(1,n + 1):
        serie += (i**2 + 1)/(i + 3)
    return serie



n = int(input(""))
res = funcao(n)
print(res)
