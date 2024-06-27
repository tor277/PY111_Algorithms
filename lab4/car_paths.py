from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    ...  # TODO решить задачу с помощью динамического программирования

    table = [[0] * m for _ in range(n)]
    table[0][0] = 1

    for i in range(n):
        for j in range(m):
            if i - 1 >= 0:
                table[i][j] += table[i - 1][j]
            if j - 1 >= 0:
                table[i][j] += table[i][j - 1]
            if i - 1 >= 0 and j - 1 >= 0:
                table[i][j] += table[i - 1][j - 1]
    return table

if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7