# Módulo para criar e manipular uma malha 2D com obstáculos estáticos e dinâmicos
class Grid:
    def __init__(self, linhas, colunas, obstaculos_atuais=None):
        """
        linhas, colunas: dimensões da malha
        obstaculos_atuais: lista de tuplas (linha, coluna) bloqueadas inicialmente
        """
        self.linhas = linhas
        self.colunas = colunas
        # 0 = livre, 1 = obstáculo
        self.malha = [[0 for _ in range(colunas)] for _ in range(linhas)]
        if obstaculos_atuais:
            for (r, c) in obstaculos_atuais:
                if self.esta_no_intervalo((r, c)):
                    self.malha[r][c] = 1

    def esta_no_intervalo(self, celula):
        r, c = celula
        return 0 <= r < self.linhas and 0 <= c < self.colunas

    def esta_livre(self, celula):
        r, c = celula
        return self.malha[r][c] == 0

    def vizinhos(self, celula):
        """
        Retorna as células ortogonais livres (cima, baixo, esquerda, direita)
        """
        r, c = celula
        possiveis = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
        return [n for n in possiveis if self.esta_no_intervalo(n) and self.esta_livre(n)]

    def alternar_obstaculo(self, celula):
        """
        Alterna estado da célula: livre (0) para obstáculo (1) e vice-versa
        """
        r, c = celula
        if not self.esta_no_intervalo(celula):
            return
        self.malha[r][c] = 0 if self.malha[r][c] == 1 else 1

    def __str__(self):
        """
        Representação textual: █ para obstáculo, espaço para livre
        """
        linhas_texto = []
        for row in self.malha:
            linhas_texto.append(''.join('█' if cell else ' ' for cell in row))
        return "\n".join(linhas_texto)
