"""Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:

6782 -> 23
0,56 -> 11"""


def is_number(temp):
    try:
        float(temp)
        return True
    except ValueError:
        return False


# def is_summ(text):
#     summ = 0
#     flag = 0
#     text = str(text)
#     text = text.split('.')
#     whole_part = int(text[0])
#     if whole_part < 0:
#         whole_part = whole_part * -1
#         flag = 1

#     print(whole_part)
#     fractional_part = int(text[1])

#     while whole_part != 0:
#         summ = summ + (whole_part % 10)
#         whole_part = whole_part // 10

#     while fractional_part != 0:
#         summ = summ + (fractional_part % 10)
#         fractional_part = fractional_part // 10
#     if flag == 1:
#         return summ

def is_summ(text_number):
    summa = 0
    for elem in text_number:
        if elem != '-' and elem != '.':
            summa = summa + int(elem)
    return summa


def input_number():
    flag = True
    while flag:
        number = input('Введите число: ')
        if is_number(number):
            return number
        else:
            print("Ввели не число")


def main():
    num = input_number()
    summ = is_summ(num)
    print(f"{num} -> {summ}")


main()
