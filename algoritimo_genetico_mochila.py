import random

# Função de aptidão (fitness)
def calcula_fitness(cromossomo, pesos_e_valores, peso_maximo):
    valor_total = 0
    peso_total = 0
    for i, gene in enumerate(cromossomo):
        if gene == 1:
            peso_total += pesos_e_valores[i][0]
            valor_total += pesos_e_valores[i][1]
    if peso_total > peso_maximo:
        return 0  # Penalidade se o peso exceder o limite
    return valor_total

# Função para criar um cromossomo aleatório
def cria_cromossomo(tamanho):
    return [random.randint(0, 1) for _ in range(tamanho)]

# Função de seleção por torneio
def selecao_por_torneio(populacao, fitness, k=3):
    selecionados = random.sample(list(enumerate(fitness)), k)
    melhor = max(selecionados, key=lambda x: x[1])
    return populacao[melhor[0]]

# Função de cruzamento (crossover)
def crossover(pai1, pai2):
    ponto_de_corte = random.randint(1, len(pai1) - 1)
    filho1 = pai1[:ponto_de_corte] + pai2[ponto_de_corte:]
    filho2 = pai2[:ponto_de_corte] + pai1[ponto_de_corte:]
    return filho1, filho2

# Função de mutação
def mutacao(cromossomo, taxa_mutacao=0.01):
    for i in range(len(cromossomo)):
        if random.random() < taxa_mutacao:
            cromossomo[i] = 1 if cromossomo[i] == 0 else 0
    return cromossomo

# Algoritmo genético
def algoritmo_genetico(pesos_e_valores, peso_maximo, num_cromossomos, geracoes):
    populacao = [cria_cromossomo(len(pesos_e_valores)) for _ in range(num_cromossomos)]
    historico_melhores = []

    for geracao in range(geracoes):
        fitness = [calcula_fitness(c, pesos_e_valores, peso_maximo) for c in populacao]
        nova_populacao = []

        # Guardar o melhor da geração
        melhor_cromossomo = max(populacao, key=lambda c: calcula_fitness(c, pesos_e_valores, peso_maximo))
        historico_melhores.append([calcula_fitness(melhor_cromossomo, pesos_e_valores, peso_maximo), melhor_cromossomo])

        # Seleção, cruzamento e mutação
        while len(nova_populacao) < num_cromossomos:
            pai1 = selecao_por_torneio(populacao, fitness)
            pai2 = selecao_por_torneio(populacao, fitness)
            filho1, filho2 = crossover(pai1, pai2)
            nova_populacao.append(mutacao(filho1))
            if len(nova_populacao) < num_cromossomos:
                nova_populacao.append(mutacao(filho2))

        populacao = nova_populacao

    return historico_melhores

# Exemplo de execução
pesos_e_valores = [
    [2, 10], [4, 30], [6, 300], [8, 10], [8, 30], 
    [8, 300], [12, 50], [25, 75], [50, 100], [100, 400]
]
peso_maximo = 100
numero_de_cromossomos = 150
geracoes = 50

resultado = algoritmo_genetico(pesos_e_valores, peso_maximo, numero_de_cromossomos, geracoes)

# Imprimir os melhores indivíduos de cada geração
for melhor in resultado:
    print(melhor)
