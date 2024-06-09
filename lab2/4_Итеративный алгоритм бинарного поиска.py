from typing import Sequence


def binary_search(value: int, seq: Sequence) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    ...  # TODO реализовать итеративный алгоритм бинарного поиска
    left, right = 0, len(seq) - 1

    while left <= right:
        mid = (left + right) // 2

        if seq[mid] < value:
            left = mid + 1
        elif seq[mid] > value:
            right = mid - 1
        else:
            while mid > 0 and seq[mid - 1] == value:
                mid -= 1
            return mid

    raise ValueError("Нет такого элемента =(")

if __name__ == '__main__':
    mas_ = [2, 5, 1, 7, 5, 5]
    m = sorted(mas_)
    print(f'Массив: {m}')
    print(f'Индекс: {binary_search(5, m)}')