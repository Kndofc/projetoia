# Módulo para calcular a rota de um ônibus escolar com várias paradas
from typing import List, Tuple
from astar import encontrar_caminho
from grid import Grid

def calcular_rota(
    inicio: Tuple[int, int],
    paradas: List[Tuple[int, int]],
    grid: Grid
) -> List[Tuple[Tuple[int, int], List[Tuple[int, int]]]]:
    """
    Sequência de paradas via heurística de menor caminho:
      1. Começa em `inicio`, escolhe a parada mais próxima (A*);
      2. Vai até ela, remove da lista;
      3. Repete até não restarem paradas.
    Retorna lista de tuplas (parada, caminho).
    """
    restantes = paradas.copy()
    rota: List[Tuple[Tuple[int, int], List[Tuple[int, int]]]] = []
    atual = inicio

    while restantes:
        melhor_parada = None
        melhor_caminho: List[Tuple[int, int]] = []
        menor_tamanho = float('inf')

        # testa cada parada e escolhe a de menor caminho
        for p in restantes:
            caminho = encontrar_caminho(grid, atual, p)
            if caminho and len(caminho) < menor_tamanho:
                menor_tamanho = len(caminho)
                melhor_parada = p
                melhor_caminho = caminho

        if not melhor_parada:
            # nenhuma parada acessível, encerra
            break

        rota.append((melhor_parada, melhor_caminho))
        restantes.remove(melhor_parada)
        atual = melhor_parada

    return rota
