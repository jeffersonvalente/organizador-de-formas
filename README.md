# Organizador de Formas com SOM 🚀

Simplifique a visualização de como algoritmos de redes neurais auto-organizáveis (Self-Organizing Maps - SOM) podem agrupar dados com eficiência. Este projeto combina inteligência artificial e animação interativa para demonstrar o processo de organização de formas geométricas.

Seja para entender o funcionamento de SOMs ou para criar experiências interativas, esta ferramenta oferece uma abordagem prática e envolvente.

## 🛠 Funcionalidades
- **Entradas Aleatórias:** Geração de triângulos, círculos e quadrados em posições aleatórias na tela.
- **Organização com SOM:** Uso de um SOM treinado para determinar as posições agrupadas para cada tipo de forma.
- **Boneco Interativo:** Um boneco busca, carrega e organiza cada forma nos locais designados.
- **Empilhamento Visual:** Formas são empilhadas verticalmente no local designado para cada tipo, garantindo clareza visual.

## 📋 Requisitos
- **Python 3.8+**
- Bibliotecas Python:
  - `pygame`
  - `numpy`
  - `minisom`

## ⚙️ Instalação

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>
   ```
2. Instale as dependências:
   ```bash
   pip install pygame numpy minisom
   ```

## ▶️ Como Executar

1. Execute o script principal:
   ```bash
   python <nome_do_script>.py
   ```
2. Observe o boneco organizando as formas na tela de maneira animada e interativa!

## 🧩 Como Funciona?

### Treinamento do SOM
- O algoritmo SOM é treinado antes de iniciar a animação, utilizando 100 iterações para ajustar os pesos e definir os agrupamentos.

### Movimentação do Boneco
1. **Busca de Formas:** O boneco identifica formas não agrupadas na tela.
2. **Transporte:** Ele carrega a forma até o ponto inicial e, em seguida, para o local de agrupamento final.
3. **Empilhamento:** Cada forma é empilhada verticalmente no local correspondente ao seu tipo.

### Renderização
A cada iteração:
- Formas não agrupadas são redesenhadas.
- Formas agrupadas são empilhadas em seus locais designados.
- O boneco e o elemento que ele está carregando são atualizados em tempo real.

## 🌟 Exemplos Práticos
- **Visualização de Redes Neurais:** Explore como SOMs agrupam dados de maneira auto-organizável.
- **Ferramenta Educacional:** Ideal para ensinar conceitos de IA e SOM de forma interativa.
- **Simulações Interativas:** Demonstre como elementos podem ser agrupados em categorias específicas.

## 📈 Benefícios Técnicos
- **Intuitivo e Visual:** Demonstração clara do funcionamento de redes neurais auto-organizáveis.
- **Personalizável:** Permite ajustes no número de formas, iterações do SOM e comportamento do boneco.
- **Didático:** Excelente para quem deseja aprender ou ensinar conceitos de SOM.

## 🤝 Contribuindo
Contribuições são bem-vindas! Sugestões e melhorias podem ser enviadas através de pull requests ou issues.

## 📢 Contato
Para dúvidas ou sugestões, entre em contato pelo [LinkedIn](https://www.linkedin.com/in/jefferson-hoy-valente-7352a0156/)]
