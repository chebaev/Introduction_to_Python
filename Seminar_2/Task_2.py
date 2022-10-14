"""Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:
пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)"""


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
            print("Ввели не число")


def calculations(num):
    if num == 1:
        return 1
    else:
        return num * calculations(num - 1)


def main():
    list_number = []
    num = input_number()
    for elem in range(1, num + 1):
        list_number.append(calculations(elem))
    print(f"Произведения чисел от 1 до {num}:  {list_number}")


main()
