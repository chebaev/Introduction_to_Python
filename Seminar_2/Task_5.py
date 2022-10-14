"""Реализуйте алгоритм перемешивания списка."""
import random


def shuffle_list(temp_list):
    len_list = len(temp_list)
    for index in range(len_list):
        random_index = random.randint(0, len_list - 1)
        temp = temp_list[index]
        temp_list[index] = temp_list[random_index]
        temp_list[random_index] = temp
    return temp_list


def save_list(number):
    i_list = []
    for _ in range(number):
        i_list.append(random.randint(0, number + 1))
    return i_list


int_list = save_list(30)
print(f"Исходный список:     {int_list}")
print(f"Перемешфнный список: {shuffle_list(int_list)}")
