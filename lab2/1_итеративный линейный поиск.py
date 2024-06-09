"""
This module implements some functions based on linear search algo
"""

from typing import List

def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    ...  # TODO реализовать итеративный линейный поиск
    if not arr:
        raise ValueError("Массив не должен быть пустым")

    min_index = 0
    for i, value in enumerate(arr):
        if value < arr[min_index]:
            min_index = i
    return min_index


if __name__ == '__main__':
    mas_ = [1, 5, 1, 7]
    print(f'Массив: {mas_}')
    print(f'Индекс: {min_search(mas_)}')