def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    ...  # TODO реализовать итеративный алгоритм нахождения факториала
    if n < 0:
        raise ValueError("Только не отрицательные целые числа")

    n_ = 1
    for i in range(1, n + 1):
        n_ *= i
    return n_


if __name__ == '__main__':
    n_ = 3
    result = factorial_iterative(n_)
    print(f"Факториал числа {n_} равен {result}")