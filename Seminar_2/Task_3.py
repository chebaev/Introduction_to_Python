"""Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

Пример:

- Для n = 3: {1: 2.0, 2: 2.25, 3: 2.37 }"""


def is_number(temp):
    try:
        float(temp)
        return True
    except ValueError:
        return False


def input_number():
    flag = True
    while flag:
        number = input('Введите число: ')
        if is_number(number) and int(number) != 0:
            return int(number)
        else:
            print("Ввели не число. Введите число больше 0")


def main():
    number = input_number()
    my_dict = {}

    for elem in range(1, number + 1):
        my_dict.__setitem__(elem, round((1 + 1/elem)**elem, 2))
    print(f"Для n = {number}: {my_dict}")


main()
