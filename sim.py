import time
from grid import Grid
from bus import Onibus

class Simulacao:
    def __init__(self, malha: Grid, onibus: Onibus):
        """
        malha: instância de Grid
        onibus: instância de Onibus (ônibus escolar)
        """
        self.malha = malha
        self.onibus = onibus
        # Planeja rota inicial
        self.onibus.planejar(self.malha)

    def passo(self):
        """
        Avança um passo na rota do ônibus.
        Retorna coordenada (linha, coluna) ou None se terminar.
        """
        return self.onibus.proximo_passo()

    def alternar_obstaculo(self, celula):
        """
        Adiciona ou remove obstáculo e replaneja a rota.
        celula: tupla (linha, coluna)
        """
        self.malha.alternar_obstaculo(celula)
        self.onibus.planejar(self.malha)
