# Módulo para implementar o algoritmo A* sobre um grid 2D com obstáculos
import heapq
from typing import List, Tuple
from grid import Grid

def heuristica(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    """
    Estimativa de custo (distância de Manhattan) entre dois pontos na malha
    a, b: tuplas (linha, coluna)
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def encontrar_caminho(
    grid: Grid,
    inicio: Tuple[int, int],
    destino: Tuple[int, int]
) -> List[Tuple[int, int]]:
    """
    Encontra o caminho ótimo de inicio até destino usando A*.
    Retorna lista de células [(r0,c0), ..., (rn,cn)], ou [] se sem caminho.
    """
    # fila de prioridade: (prioridade, célula)
    fila: List[Tuple[int, Tuple[int, int]]] = []
    heapq.heappush(fila, (0, inicio))
    veio_de = {inicio: None}
    custo_ate = {inicio: 0}

    while fila:
        _, atual = heapq.heappop(fila)  #tira o nó de menor f = g + h
        if atual == destino:
            break
        for vizinho in grid.vizinhos(atual):
            novo_custo = custo_ate[atual] + 1
            if vizinho not in custo_ate or novo_custo < custo_ate[vizinho]:
                custo_ate[vizinho] = novo_custo
                prioridade = novo_custo + heuristica(vizinho, destino)
                heapq.heappush(fila, (prioridade, vizinho))
                veio_de[vizinho] = atual

    # se não alcançou destino
    if destino not in veio_de:
        return []

    # reconstrói o caminho
    caminho: List[Tuple[int, int]] = []
    nodo = destino
    while nodo is not None:
        caminho.append(nodo)
        nodo = veio_de[nodo]
    caminho.reverse()
    return caminho

