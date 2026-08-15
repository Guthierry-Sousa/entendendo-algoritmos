estados = set(['mt', 'wa', 'or', 'ca', 'az', 'nv', 'id', 'ut'])

estacoes = {
    '1': set(['id', 'nv', 'ut']),
    '2': set(['wa', 'mt', 'id']),
    '3': set(['or', 'nv', 'ca']),
    '4': set(['nv', 'ut']),
    '5': set(['ca', 'az'])
}

estacoes_finais = []

while estados:
    melhor_estacao = None
    estados_cobertos = set()

    for estacao, estados_estacao in estacoes.items():

        cobertos = estados_estacao & estados

        if len(cobertos) > len(estados_cobertos):

            estados_cobertos = cobertos
            melhor_estacao = estacao

    estacoes_finais.append(melhor_estacao)
    estados -= estados_cobertos

print("Estações selecionadas (Aproximação):", estacoes_finais)