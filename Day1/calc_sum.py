try:
    a = input("Введи первое число: ").replace(",", ".")
    b = input("Введи второе число: ").replace(",", ".")

    a = float(a)
    b = float(b)

    print(f"Сумма {a} + {b} = {a + b}")

except ValueError:
    print("Ошибка...")

input("Нажми Enter, чтобы выйти...")