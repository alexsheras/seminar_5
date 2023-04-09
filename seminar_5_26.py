A = int(input("Введите число A: "))
B = int(input("Введите его степень B: "))

def power(A, B):
    if (B == 1):
        return (A)
    if (B != 1):
        return (A * power(A, B - 1))

print("Результат возведения в степень равен:", power(A, B))