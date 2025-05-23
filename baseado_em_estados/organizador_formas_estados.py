import pygame
import numpy as np
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Organizador de Formas - Visualização 2D")

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

# Locais de agrupamento para cada tipo (definido dinamicamente)
locais_agrupamento = [None, None, None]

# Inicializa o bonequinho
boneco = {"x": WIDTH // 2, "y": HEIGHT // 2, "carregando": None, "destino": None, "estado": "buscar", "alvo": None}

# Função para mover o boneco para uma entrada ou destino
def mover_boneco(destino):
    if abs(boneco["x"] - destino[0]) >= 2:
        boneco["x"] += 2 if boneco["x"] < destino[0] else -2

    if abs(boneco["y"] - destino[1]) >= 2:
        boneco["y"] += 2 if boneco["y"] < destino[1] else -2

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

# Função para desenhar os locais de agrupamento
def desenhar_locais_agrupamento():
    for i, local in enumerate(locais_agrupamento):
        if local is not None:
            color = [TRIANGLE_COLOR, CIRCLE_COLOR, SQUARE_COLOR][i]
            pygame.draw.circle(screen, color, local, 15, 2)

# Função para desenhar os elementos agrupados
def desenhar_agrupados():
    for tipo, elementos in agrupadas.items():
        color = [TRIANGLE_COLOR, CIRCLE_COLOR, SQUARE_COLOR][tipo]
        for index, (x, y) in enumerate(elementos):
            if tipo == 0:  # Triângulo
                pontos = [(x, y - 10), (x - 10, y + 10), (x + 10, y + 10)]
                pygame.draw.polygon(screen, color, pontos)
            elif tipo == 1:  # Círculo
                pygame.draw.circle(screen, color, (x, y), 10)
            elif tipo == 2:  # Quadrado
                pygame.draw.rect(screen, color, (x - 10, y - 10, 20, 20))

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
        # Caso o boneco esteja vazio (nada carregando)
        pass  # Não desenha nada, mas mantém o controle

# Loop principal do jogo
rodando = True
clock = pygame.time.Clock()

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # Limpa a tela
    screen.fill(WHITE)

    # Desenha entradas, agrupados e locais de agrupamento
    desenhar_entradas()
    desenhar_locais_agrupamento()
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
            # Após alcançar o elemento, pega e atualiza o estado
            boneco["carregando"] = boneco["alvo"]
            boneco["alvo"] = None
            boneco["estado"] = "levando_para_grupo"

            # Define o local de agrupamento se ainda não existir
            tipo = boneco["carregando"]["tipo"]
            if locais_agrupamento[tipo] is None:
                locais_agrupamento[tipo] = (boneco["x"], boneco["y"])
            boneco["destino"] = locais_agrupamento[tipo]

    elif boneco["estado"] == "levando_para_grupo":
        # Move até o local de agrupamento
        mover_boneco(boneco["destino"])
        if abs(boneco["x"] - boneco["destino"][0]) < 2 and abs(boneco["y"] - boneco["destino"][1]) < 2:
            # Agrupa a entrada
            tipo = boneco["carregando"]["tipo"]
            agrupadas[tipo].append((boneco["destino"][0], boneco["destino"][1] + len(agrupadas[tipo]) * 20))
            boneco["carregando"]["agrupado"] = True
            boneco["carregando"] = None  # Solta o elemento
            boneco["estado"] = "buscar"

    # Desenha o bonequinho
    pygame.draw.circle(screen, BLACK, (boneco["x"], boneco["y"]), 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
