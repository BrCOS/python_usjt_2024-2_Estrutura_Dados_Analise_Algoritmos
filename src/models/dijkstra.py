import heapq

def dijkstra(grafo, centro, destinos):
    distancias = {cidade: float('inf') for cidade in grafo}#cidades com o peso infinito
    distancias[centro] = 0#inicio definido como 0 (cidade de partida - centro)

    caminhos = {cidade: [] for cidade in grafo}#[] recebe o menor caminho (return)
    caminhos[centro] = [centro]#define o caminho 0 (centro) ate ele mesmo (ponto inicial do algoritmo)

    filaPrioridade = [(0, centro)]#define o centro como prioridade (distancia (peso) 0)

    #continuar enquanto tiver elementos na lista []
    while filaPrioridade:#while pq a [] nao tem tamanho fixo
        #heapq p/ processar a menor distancia (peso) das cidades
        #heappop p/ remover as cidades ja processadas da [] (com o menor caminho) ate acabar as cidades
        distanciaAtual, cidadeAtual = heapq.heappop(filaPrioridade)#passa o peso e a cidade com menor distancia pro dicionario

        #ignora caminhos mais longos
        if distanciaAtual > distancias[cidadeAtual]:
            continue
        
        #acesso aos vizinhos e seus pesos da cidade atual
        for vizinho, peso in grafo[cidadeAtual].items():
            distancia = distanciaAtual + peso

            #compara o peso (distancia) com a atual e atualiza a []
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia#atualiza a cidade com o menor caminho encontrado
                caminhos[vizinho] = caminhos[cidadeAtual] + [vizinho]#passa o menor caminho seguindo do vizinho
                heapq.heappush(filaPrioridade, (distancia, vizinho))#passa o caminho mais curto p/ while
        
    #filtra os destinos que tem um caminho
    caminhoDestinos = {}
    for destino in destinos:
        if destino in caminhos:#verifica se o destino esta no dicionario caminhos (se tem um caminho)
            caminhoDestinos[destino] = caminhos[destino]#passa o destino como chave e o valor eh o caminho de caminhos

    #evitar que ponto seja re-visitado
    rota = [centro]#começa com o centro
    visitados = set(rota)

    #ordenar pela menor distancia (peso) - ordem crescente
    destinosOrdem = sorted(destinos, key=lambda d: distancias[d])#distancia do centro ate o destino (0 - cidade destino)

    #percorre cada destino ordenado
    for destino in destinosOrdem:
        for ponto in caminhoDestinos[destino]:
            if ponto not in visitados:#se nao foi visitado, adiciona como visitado
                rota.append(ponto)
                visitados.add(ponto)

    return rota