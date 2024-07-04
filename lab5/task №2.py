"""
Задача №2. Консенсус DNA рядов
При чтении DNA последовательностей могут возникать единичные ошибки, выражающиеся в неверной букве в строке.
Для решения данной проблемы требуемое место читается несколько раз, после чего строится консенсус-строка,
в которой на каждом месте будет стоять тот символ, что чаще всего встречался в этом месте суммарно во всех чтениях.
Т.е. для строк
ATTA
ACTA
AGCA
ACAA

S = ‘ATTA ACTA …’
data = [‘ATTA’,
             ‘ACTA’…
]
data =[
[‘A’, ‘T’, ‘T’,’A’],
…]
консенсус-строка будет ACTA (в первой ячейке чаще всего встречалась A, во второй – C, в третьей – Т, в четвертой – снова А).
Для входного списка из N строк одинаковой длины построить консенсус-строку.

Def func(data: iterable)->str:
	pass

"""


from typing import Iterable


def consensus_string(data: Iterable) -> str:
    if not data:
        return ""

    str_lenght = len(data[0])
    consensus = []

    char_counts = [{} for _ in range(str_lenght)]

    for sequence in data:
        for i, char in enumerate(sequence):
            if char in char_counts[i]:
                char_counts[i][char] += 1
            else:
                char_counts[i][char] = 1

    for counts in char_counts:
        most_common_char = max(counts, key=counts.get)
        consensus.append(most_common_char)

    return ''.join(consensus)


if __name__ == '__main__':
    data = [
        "ALTA",
        "ACTA",
        "AGCA",
        "ALAA"
    ]

    consensus_string = consensus_string(data)
    print(consensus_string)  # ALTA
