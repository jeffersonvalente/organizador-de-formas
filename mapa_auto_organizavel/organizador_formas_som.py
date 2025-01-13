import pygame
import numpy as np
import random
from minisom import MiniSom

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Organizador de Formas com SOM")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TRIANGLE_COLOR = (0, 255, 255)
CIRCLE_COLOR = (255, 255, 0)
SQUARE_COLOR = (255, 0, 255)

# Configurações das entradas
NUM_TIPOS = 3  # Triângulo, Círculo, Quadrado
NUM_ENTRADAS = 10  # Por tipo
entradas = []
agrupadas = {0: [], 1: [], 2: []}  # Para armazenar as posições agrupadas

# Posições fixas para empilhamento
posicoes_agrupamento = {
    0: (200, HEIGHT // 2),  # Triângulos
    1: (400, HEIGHT // 2),  # Círculos
    2: (600, HEIGHT // 2),  # Quadrados
}

# Ponto inicial para organização
ponto_inicial = (50, HEIGHT // 2)

# Gera entradas iniciais em posições aleatórias
def gerar_entradas():
    for tipo in range(NUM_TIPOS):
        for _ in range(NUM_ENTRADAS):
            entrada = {
                "x": random.randint(50, WIDTH - 50),
                "y": random.randint(50, HEIGHT - 50),
                "tipo": tipo,  # 0 = Triângulo, 1 = Círculo, 2 = Quadrado
                "agrupado": False
            }
            entradas.append(entrada)

gerar_entradas()

# Inicializa o SOM
data = np.array([[entrada["x"], entrada["y"], entrada["tipo"]] for entrada in entradas])
normalized_data = data / np.max(data, axis=0)  # Normaliza os dados
som = MiniSom(10, 10, 3, sigma=1.0, learning_rate=0.5)
som.random_weights_init(normalized_data)

# Treina o SOM antes de iniciar o loop
som.train(normalized_data, num_iteration=1000)

# Inicializa o bonequinho
boneco = {
    "x": WIDTH // 2,
    "y": HEIGHT // 2,
    "carregando": None,
    "destino": None,
    "estado": "buscar",
    "alvo": None,
    "etapa": "para_inicial"  # Nova etapa para gerenciar o ponto inicial
}

# Função para mover o boneco para uma entrada ou destino
def mover_boneco(destino):
    if abs(boneco["x"] - destino[0]) >= 2:
        boneco["x"] += 2 if boneco["x"] < destino[0] else -2

    if abs(boneco["y"] - destino[1]) >= 2:
        boneco["y"] += 2 if boneco["y"] < destino[1] else -2

    # Atualiza a posição do elemento carregado
    if boneco["carregando"] is not None:
        boneco["carregando"]["x"] = boneco["x"]
        boneco["carregando"]["y"] = boneco["y"] - 20

# Função para desenhar as entradas
def desenhar_entradas():
    for entrada in entradas:
        if not entrada["agrupado"] and entrada != boneco["carregando"]:
            x, y, tipo = entrada["x"], entrada["y"], entrada["tipo"]
            if tipo == 0:  # Triângulo
                pontos = [(x, y - 10), (x - 10, y + 10), (x + 10, y + 10)]
                pygame.draw.polygon(screen, TRIANGLE_COLOR, pontos)
            elif tipo == 1:  # Círculo
                pygame.draw.circle(screen, CIRCLE_COLOR, (x, y), 10)
            elif tipo == 2:  # Quadrado
                pygame.draw.rect(screen, SQUARE_COLOR, (x - 10, y - 10, 20, 20))

# Função para desenhar os elementos agrupados
def desenhar_agrupados():
    for tipo, elementos in agrupadas.items():
        color = [TRIANGLE_COLOR, CIRCLE_COLOR, SQUARE_COLOR][tipo]
        base_x, base_y = posicoes_agrupamento[tipo]
        for i, (x, y) in enumerate(elementos):
            pos_x = base_x
            pos_y = base_y - (i * 20)  # Empilha verticalmente
            if tipo == 0:  # Triângulo
                pontos = [(pos_x, pos_y - 10), (pos_x - 10, pos_y + 10), (pos_x + 10, pos_y + 10)]
                pygame.draw.polygon(screen, color, pontos)
            elif tipo == 1:  # Círculo
                pygame.draw.circle(screen, color, (pos_x, pos_y), 10)
            elif tipo == 2:  # Quadrado
                pygame.draw.rect(screen, color, (pos_x - 10, pos_y - 10, 20, 20))

# Função para desenhar o elemento carregado pelo boneco
def desenhar_carregando():
    if boneco["carregando"] is not None:
        tipo = boneco["carregando"]["tipo"]
        x, y = boneco["x"], boneco["y"] - 20  # O elemento "flutua" acima do boneco
        if tipo == 0:  # Triângulo
            pontos = [(x, y - 10), (x - 10, y + 10), (x + 10, y + 10)]
            pygame.draw.polygon(screen, TRIANGLE_COLOR, pontos)
        elif tipo == 1:  # Círculo
            pygame.draw.circle(screen, CIRCLE_COLOR, (x, y), 10)
        elif tipo == 2:  # Quadrado
            pygame.draw.rect(screen, SQUARE_COLOR, (x - 10, y - 10, 20, 20))
    else:
        pass

# Loop principal do jogo
rodando = True
clock = pygame.time.Clock()

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # Limpa a tela
    screen.fill(WHITE)

    # Desenha entradas e agrupados
    desenhar_entradas()
    desenhar_agrupados()
    desenhar_carregando()

    # Lógica de movimentação e organização
    if boneco["estado"] == "buscar":
        # Encontra a próxima entrada não agrupada
        if boneco["carregando"] is None:
            for entrada in entradas:
                if not entrada["agrupado"]:
                    boneco["destino"] = (entrada["x"], entrada["y"])
                    boneco["alvo"] = entrada  # Define temporariamente o elemento a ser alcançado
                    boneco["estado"] = "movendo_para_entrada"
                    break

    elif boneco["estado"] == "movendo_para_entrada":
        # Move até a entrada
        mover_boneco(boneco["destino"])
        if abs(boneco["x"] - boneco["destino"][0]) < 2 and abs(boneco["y"] - boneco["destino"][1]) < 2:
            boneco["carregando"] = boneco["alvo"]
            boneco["alvo"] = None
            boneco["estado"] = "levando_para_grupo"
            boneco["destino"] = ponto_inicial  # Primeiro vai para o ponto inicial
            boneco["etapa"] = "para_inicial"

    elif boneco["estado"] == "levando_para_grupo":
        # Move o elemento para o ponto inicial ou grupo final
        mover_boneco(boneco["destino"])
        if abs(boneco["x"] - boneco["destino"][0]) < 2 and abs(boneco["y"] - boneco["destino"][1]) < 2:
            if boneco["etapa"] == "para_inicial":
                # Chegou ao ponto inicial, agora vai para o grupo final
                tipo = boneco["carregando"]["tipo"]
                boneco["destino"] = posicoes_agrupamento[tipo]
                boneco["etapa"] = "para_grupo"
            elif boneco["etapa"] == "para_grupo":
                # Chegou ao grupo final
                tipo = boneco["carregando"]["tipo"]
                agrupadas[tipo].append((0, 0))  # Placeholder para renderização com lógica de empilhamento
                boneco["carregando"]["agrupado"] = True
                boneco["carregando"] = None  # Solta o elemento
                boneco["estado"] = "buscar"

    # Desenha o bonequinho
    pygame.draw.circle(screen, BLACK, (boneco["x"], boneco["y"]), 10)

    # Atualiza a tela
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
