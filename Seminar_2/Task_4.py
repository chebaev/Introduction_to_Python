"""Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в
 одной строке одно число."""
from random import randint


def fill_list(number):
    temp_list = []
    for _ in range(number):
        temp_list.append(randint(-number, number + 1))
    return temp_list


def writing_to_file(_path, my_list):
    with open(_path, "w+") as data:
        for elem in my_list:
            data.write(str(elem))
            data.write('\n')


def reading_file_plus_derivative(path):
    summa = 0

    with open(path, 'r') as data:
        values = data.read().split("\n")
    for i in values:
        if i != '':
            summa = summa + int(i)
    return summa

def is_number(temp):
    try:
        float(temp)
        return True
    except ValueError:
        return False

def input_number():
    flag = True
    while flag:
        number = input('Введите число элементов: ')
        if is_number(number):
            if int(number) != 0:
                return int(number)
            else:
                print(f"Произведение элемента {number} = {number}")
                exit()
        else:
            print("Ввели не число")


def main():
    path = "file.txt"
    N = input_number()
    writing_to_file(path, fill_list(N))
    summa = reading_file_plus_derivative(path)
    print(f"Произведение  {N} элементов = {summa}")


main()
