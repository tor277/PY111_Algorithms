from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    ...  # TODO реализовать алгоритм сортировки подсчетами
    if not container:
        return container

    max_value = max(container)
    count = [0] * (max_value + 1)

    for num in container:
        count[num] += 1

    arr = [0] * len(container)
    index = 0

    for i in range(max_value + 1):
        for _ in range(count[i]):
            arr[index] = i
            index += 1

    return arr


if __name__ == '__main__':
    data = [5, 3, 8, 9, 1, 6, 2, 2]
    print(sort(container=data))