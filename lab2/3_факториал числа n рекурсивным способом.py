def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n

    """
    ...  # TODO реализовать рекурсивный алгоритм нахождения факториала

    if isinstance(n, float):
        if n % 1 != 0:
            raise TypeError("Только не отрицательные целые числа")

    if not isinstance(n, int) or n < 0:
        raise ValueError("Только не отрицательные целые числа")

    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

if __name__ == '__main__':
    n_ = 3
    result = factorial_recursive(n_)
    print(f"Факториал числа {n_} равен {result}")
