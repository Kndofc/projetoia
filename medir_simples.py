from grid import Grid
from bus import Onibus
import time

# 1) Configurações de teste
malha = Grid(15, 15, obstaculos_atuais=[(3,3),(5,5),(7,7),(2,10),(10,2)])
garage, paradas = (0,0), [(4,4),(8,2),(12,10)]
onibus = Onibus(garage, paradas, cor="blue")

# 2) Medir o planejamento inicial
t0 = time.perf_counter()
onibus.planejar(malha)
t1 = time.perf_counter()
print(f"Planejamento inicial: {(t1-t0)*1000:.2f} ms")

# 3) Medir o replanejamento
malha.alternar_obstaculo((6,6))
t2 = time.perf_counter()
onibus.planejar(malha)
t3 = time.perf_counter()
print(f"Replanejamento:       {(t3-t2)*1000:.2f} ms")
