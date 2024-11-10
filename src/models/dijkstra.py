import heapq

def dijkstra(grafo, inicio):
    distancias = {cidade: float('inf') for cidade in grafo}#cidades com o peso infinito
    distancias[inicio] = 0#inicio definido como 0 (cidade de partida - centro)

    caminho = {cidade: [] for cidade in grafo}#[] recebe o menor caminho (return)
    caminho[inicio] = [inicio]#define o caminho 0 (centro) ate ele mesmo (ponto inicial do algoritmo)

    filaPrioridade = [(0, inicio)]#define o centro como prioridade (distancia (peso) 0)

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
                caminho[vizinho] = caminho[cidadeAtual] + [vizinho]#passa o menor caminho seguindo do vizinho
                heapq.heappush(filaPrioridade, (distancia, vizinho))#passa o caminho mais curto p/ while

    return caminho