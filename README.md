# Trajeto Escolar Inteligente

Simulador de roteirização de linhas de transporte escolar usando o algoritmo A\* com replanejamento dinâmico e interface interativa em Streamlit.

## 🔍 Descrição

Este projeto demonstra a aplicação do algoritmo A\* em um grid 2D com obstáculos estáticos e dinâmicos para roteirização de múltiplas paradas (ônibus escolar). Inclui:

* Busca heurística (A\*) com heurística de Manhattan.
* Sequenciamento guloso de paradas.
* Replanejamento de rota em tempo real ao adicionar/remover obstáculos.
* Interface interativa em Streamlit para visualização e animação.
* Benchmarks de performance para planejamento e replanejamento.

## 🚀 Recursos

* **A**\*: Encontra caminhos ótimos em grafos ponderados não-negativos.
* **Roteirização Gulosa**: Seleciona sempre a parada mais próxima.
* **Replanejamento Dinâmico**: Atualiza a rota ao detectar novos obstáculos.
* **UI Intuitiva**: Permite configurar grid, paradas e obstáculos; visualiza trajeto passo a passo.
* **Performance**: Planejamento e replanejamento em menos de 1 ms para grids 15×15.

## 📁 Estrutura de Diretórios

```
├── astar.py           # Implementação do A* com heurística de Manhattan
├── grid.py            # Classe Grid: malha 2D, vizinhança e obstacles toggle
├── routing.py         # Roteirização gulosa para múltiplas paradas
├── bus.py             # Classe Ônibus: gerencia segmentos e progresso da rota
├── sim.py             # Simulação de rota e wrapper para UI
├── medir_simples.py   # Script de benchmark de tempo de planejamento e replanejamento
├── ui.py              # Aplicação Streamlit para interação e animação
└── README.md          # Este arquivo
```

## ⚙️ Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/Kndofc/projetoia.git
   ```
2. Crie um ambiente virtual e instale dependências:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .\.venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```
3. (Opcional) Instale o Streamlit globalmente:

   ```bash
   pip install streamlit
   ```

## 🎬 Uso

### 1. Executar benchmarks

```bash
python medir_simples.py
```

### 2. Iniciar a interface Streamlit

```bash
streamlit run ui.py
```

* Defina o tamanho do grid, insira coordenadas de paradas e obstáculos.
* Clique em *Iniciar Rota* e observe a animação passo a passo.

## 📚 Módulos Principais

* **astar.py**: busca informada A\*.
* **grid.py**: modelagem de malha com obstáculos.
* **routing.py**: lógica gulosa para múltiplas paradas.
* **bus.py**: gerencia execução da rota por passos.
* **sim.py**: conecta `bus.py` e `grid.py` para simular itinerário.
* **medir\_simples.py**: mede tempos de planejamento.
* **ui.py**: interface gráfica baseada em Streamlit.

## 🎯 Contribuindo

1. Faça um *fork* do projeto.
2. Crie uma *branch* para sua feature: `git checkout -b feature/nova-funcionalidade`.
3. Commit suas mudanças: `git commit -m "Adiciona recurso X"`.
4. *Push* para a *branch*: `git push origin feature/nova-funcionalidade`.
5. Abra um *Pull Request*.
