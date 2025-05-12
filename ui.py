import streamlit as st
import matplotlib.pyplot as plt
import time
from grid import Grid
from bus import Onibus
from sim import Simulacao

# Cores para paradas (estrelas)
CORES_PARADAS = ['orange', 'red', 'purple', 'cyan', 'magenta', 'yellow', 'brown', 'pink']

# --- Configuração da página ---
st.set_page_config(layout="wide")
st.title("Trajeto Escolar Inteligente")
st.sidebar.title("Controles")

# --- Inputs da Sidebar ---
# Tamanho da malha (grid)
tamanho = st.sidebar.slider("Tamanho da malha", 5, 30, 15)

# Paradas de alunos
entrada_paradas = st.sidebar.text_input(
    "Paradas (formato: (r1,c1),(r2,c2),...)",
    "(2,3),(5,5),(10,2)"
)
botao_definir = st.sidebar.button("Definir Paradas")

# Obstáculos dinâmicos
entrada_obs = st.sidebar.text_input(
    "Obstáculos (formato: (r1,c1),(r2,c2),...)",
    ""
)
botao_obs = st.sidebar.button("Adicionar/Remover Obstáculos")

# Iniciar simulação
botao_iniciar = st.sidebar.button("Iniciar Rota")

# --- Estado Persistente ---
if 'obstaculos' not in st.session_state:
    st.session_state['obstaculos'] = []
if 'paradas' not in st.session_state:
    st.session_state['paradas'] = []
if 'malha' not in st.session_state:
    st.session_state['malha'] = Grid(tamanho, tamanho, obstaculos_atuais=st.session_state['obstaculos'])

# --- Definir paradas ---
if botao_definir:
    try:
        texto = entrada_paradas.strip()
        lista = [tuple(map(int, p.strip('() ').split(','))) for p in texto.split('),(')]
        st.session_state['paradas'] = lista
        st.sidebar.success(f"Paradas: {lista}")
        # recriar malha e limpar sim
        st.session_state['malha'] = Grid(tamanho, tamanho, obstaculos_atuais=st.session_state['obstaculos'])
        st.session_state.pop('sim', None)
        st.session_state.pop('posicoes', None)
    except:
        st.sidebar.error("Formato inválido. Use: (r1,c1),(r2,c2),...")

# --- Adicionar/Remover obstáculos ---
if botao_obs:
    try:
        texto = entrada_obs.strip()
        parts = texto.split('),(')
        celulas = []
        for part in parts:
            p = part.strip('() ')
            r, c = map(int, p.split(','))
            celulas.append((r, c))
        for cel in celulas:
            if cel in st.session_state['obstaculos']:
                st.session_state['obstaculos'].remove(cel)
                st.sidebar.write(f"Obstáculo removido em {cel}")
            else:
                st.session_state['obstaculos'].append(cel)
                st.sidebar.write(f"Obstáculo adicionado em {cel}")
        # recriar malha e limpar sim
        st.session_state['malha'] = Grid(tamanho, tamanho, obstaculos_atuais=st.session_state['obstaculos'])
        st.session_state.pop('sim', None)
        st.session_state.pop('posicoes', None)
    except:
        st.sidebar.error("Formato inválido. Use: (r1,c1),(r2,c2),...")

# --- Atualiza malha se tamanho mudou ---
if st.session_state['malha'].linhas != tamanho:
    st.session_state['malha'] = Grid(tamanho, tamanho, obstaculos_atuais=st.session_state['obstaculos'])
    st.session_state.pop('sim', None)
    st.session_state.pop('posicoes', None)

# --- Iniciar simulação ---
if botao_iniciar:
    if not st.session_state['paradas']:
        st.sidebar.error("Defina as paradas antes de iniciar.")
    else:
        malha = st.session_state['malha']
        garagem = (0, 0)
        onibus = Onibus(garagem, st.session_state['paradas'], cor='blue')
        sim = Simulacao(malha, onibus)
        st.session_state['sim'] = sim
        st.session_state['posicoes'] = []
        st.sidebar.success("Simulação iniciada!")

# --- Recupera estado ---
malha = st.session_state['malha']
sim = st.session_state.get('sim', None)
posicoes = st.session_state.get('posicoes', [])

# --- Plot ---
col1, col2 = st.columns(2)

with col1:
    st.write("### Mapa estático")
    fig, ax = plt.subplots()
    ax.imshow(malha.malha, origin='lower', cmap='gray_r')
    # garagem
    ax.scatter(0, 0, marker='s', color='green', s=100, label='Garagem')
    # paradas com cores distintas
    for idx, p in enumerate(st.session_state['paradas']):
        cor = CORES_PARADAS[idx % len(CORES_PARADAS)]
        ax.scatter(p[1], p[0], marker='*', color=cor, s=200, label=f'Parada {idx+1}')
        ax.text(p[1]+0.3, p[0]+0.3, str(idx+1), color='white', fontsize=12, weight='bold')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.legend(loc='upper right')
    st.pyplot(fig)

with col2:
    st.write("### Simulação passo a passo")
    if sim:
        placeholder = st.empty()
        while True:
            pos = sim.passo()
            if pos is None:
                st.success("Rota concluída!")
                break
            posicoes.append(pos)
            fig2, ax2 = plt.subplots()
            ax2.imshow(malha.malha, origin='lower', cmap='gray_r')
            # rota até agora
            xs = [p[1] for p in posicoes]
            ys = [p[0] for p in posicoes]
            ax2.plot(xs, ys, '-', marker='*', markersize=12, color='blue')
            # garagem e paradas com cores distintas
            ax2.scatter(0, 0, marker='s', color='green', s=100)
            for idx, p in enumerate(st.session_state['paradas']):
                cor = CORES_PARADAS[idx % len(CORES_PARADAS)]
                ax2.scatter(p[1], p[0], marker='*', color=cor, s=200)
                ax2.text(p[1]+0.3, p[0]+0.3, str(idx+1), color='white', fontsize=12, weight='bold')
            ax2.set_xticks([])
            ax2.set_yticks([])
            placeholder.pyplot(fig2)
            time.sleep(0.1)
    else:
        st.write("Defina paradas e inicie para ver a simulação.")