# Algoritmo Genético para Problema da Mochila

Este projeto implementa um algoritmo genético para resolver o problema da mochila, onde o objetivo é maximizar o valor total de itens dentro de uma mochila sem exceder o peso máximo permitido. Cada geração do algoritmo evolui para produzir soluções melhores.

## Estrutura

- **Algoritmo Genético**: O algoritmo simula a evolução de uma população de cromossomos que representam combinações de itens a serem colocados na mochila.
- **Funções**:
  - **Fitness**: Avalia a qualidade de cada solução (cromossomo) baseado no valor total dos itens e na restrição de peso.
  - **Seleção por Torneio**: Seleciona os melhores indivíduos da população.
  - **Crossover**: Combina dois cromossomos pais para criar dois filhos.
  - **Mutação**: Faz mudanças aleatórias para manter a diversidade genética.

## Como Rodar o Código

### Pré-requisitos

- Python 3.x instalado na máquina.
- Não há dependências externas além de bibliotecas padrão do Python.

### Passos

1. **Clonar o Repositório**:
   ```bash
   git clone https://github.com/seuusuario/projeto-genetico-mochila.git
   cd projeto-genetico-mochila
