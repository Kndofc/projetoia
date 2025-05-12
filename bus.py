from typing import List, Tuple
from routing import calcular_rota
from grid import Grid

class Onibus:
    """
    Representa um ônibus escolar que sai de uma garagem e visita várias paradas.

    A rota é calculada passo a passo, sempre escolhendo a próxima parada mais próxima.
    """
    def __init__(
        self,
        garagem: Tuple[int, int],
        paradas: List[Tuple[int, int]],
        cor=None
    ):
        """
        :param garagem: coordenada (linha, coluna) da garagem
        :param paradas: lista de coordenadas (linha, coluna) das paradas
        :param cor: cor opcional para visualização
        """
        self.garagem: Tuple[int, int] = garagem
        self.paradas: List[Tuple[int, int]] = paradas
        self.cor = cor
        self.rota: List[Tuple[Tuple[int, int], List[Tuple[int, int]]]] = []  # lista de (parada, caminho)
        self.indice_segmento: int = 0  # índice da parada atual em self.rota
        self.indice_passo: int = 0     # índice dentro do caminho atual

    def planejar(self, grid: Grid) -> None:
        """
        Calcula o roteiro completo (lista de paradas e caminhos) usando A*.
        """
        # calcular_rota retorna [(parada, caminho), ...]
        self.rota = calcular_rota(self.garagem, self.paradas, grid)
        self.indice_segmento = 0
        self.indice_passo = 0

    def proximo_passo(self) -> Tuple[int, int] or None: # type: ignore
        """
        Avança um passo na rota planejada.
        Retorna a coordenada (linha, coluna) do ônibus ou None se terminar.
        """
        # se não há mais segmentos, terminou
        if self.indice_segmento >= len(self.rota):
            return None

        parada, caminho = self.rota[self.indice_segmento]
        # se ainda há passos no caminho
        if self.indice_passo < len(caminho):
            pos = caminho[self.indice_passo]
            self.indice_passo += 1
            return pos

        # chegou na parada, vai para próximo segmento
        self.indice_segmento += 1
        self.indice_passo = 0
        return self.proximo_passo()
