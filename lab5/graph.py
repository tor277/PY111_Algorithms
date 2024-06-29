from typing import Union

import networkx as nx
from matplotlib import pyplot


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    ...  # TODO c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы

    path = nx.single_source_dijkstra_path_length(graph, 0)
    return path[max(graph.nodes)]

if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = [
    (0, 1, 5),
    (0, 2, 11),
    (1, 2, 11),
    (1, 3, 43),
    (2, 3, 43),
    (2, 4, 2),
    (3, 4, 2),
    (3, 5, 23),
    (4, 5, 23),
    (4, 6, 43),
    (5, 6, 43),
    (5, 7, 22),
    (6, 7, 22),
    (6, 8, 12),
    (7, 8, 12),
    (7, 9, 6),
    (8, 9, 6),
    (8, 10, 8),
    (9, 10, 8)

]
    # TODO записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней
    graph = nx.DiGraph()
    graph.add_weighted_edges_from(stairway_graph)

    print(stairway_path(graph))  # 72

    nx.draw_networkx(graph, node_color='#7FFF00', node_size=1000, with_labels=True)
    pyplot.show()
