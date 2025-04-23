
# Organizador de Formas com SOM — Visualização Interativa de Agrupamento com IA

Esse projeto mostra, de forma prática e animada, como algoritmos de redes neurais auto-organizáveis (SOM) conseguem agrupar dados com base em similaridade.  
Aqui, formas geométricas são geradas aleatoriamente e organizadas por um boneco animado, que simula o processo de classificação e agrupamento.

É uma forma direta de entender como SOMs funcionam — útil tanto pra aprender quanto pra ensinar.

---

## O que esse projeto faz

- Gera triângulos, círculos e quadrados aleatoriamente na tela
- Treina um SOM (Self-Organizing Map) para identificar agrupamentos
- Um boneco interativo coleta e organiza as formas de acordo com seus grupos
- Apresenta o resultado de forma visual e animada

---

## Requisitos

- Python 3.8 ou superior
- Bibliotecas:
  - pygame
  - numpy
  - minisom

---

## Como rodar

1. Clone o projeto:

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```

2. Instale as dependências:

```bash
pip install pygame numpy minisom
```

3. Execute o script principal:

```bash
python <nome_do_script>.py
```

---

## Como funciona

### Treinamento
- O SOM é treinado com base nas características das formas.
- São feitas 100 iterações para ajustar os pesos e definir os agrupamentos.

### Animação
- O boneco identifica uma forma desagrupada.
- Leva até a área inicial e depois até a área designada pelo SOM.
- Empilha visualmente conforme o tipo de forma.

---

## Aplicações práticas

- Didática: Ideal para explicar visualmente como SOMs funcionam.
- Simulações interativas: Agrupamento visual em tempo real.
- Exploração de IA visual: Demonstração clara de agrupamento auto-organizado.

---

## Por que usar?

Esse projeto traduz um conceito abstrato como redes neurais em algo que dá pra ver, mexer e entender.  
É útil pra quem tá estudando IA, precisa explicar SOM de forma acessível ou quer explorar visualmente como algoritmos classificam dados.

---

## Contribuições

Sugestões são bem-vindas.  
Se quiser melhorar a lógica, propor novas formas ou aumentar o nível de interatividade, manda um pull request ou issue.

---

## Contato

LinkedIn: https://www.linkedin.com/in/jefferson-hoy-valente/
