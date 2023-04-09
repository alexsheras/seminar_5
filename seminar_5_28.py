a, b = int(input("Введите число a: ")), int(input("Введите число b: "))

def summa(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return summa(a + 1, b - 1)


print(summa(a,b))