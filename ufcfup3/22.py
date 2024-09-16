def floyds_triangle(n):
    number = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(number, end=" ")
            number += 1
        print()

n = int(input(""))

floyds_triangle(n)