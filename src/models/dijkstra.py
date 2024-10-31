import heapq

def dijkstra(grafo, inicio):
    distancias = {cidade: float('inf') for cidade in grafo}
    distancias[inicio] = 0
    caminho = {cidade: None for cidade in grafo}

    filaPrioridade = [(0, inicio)]

    while filaPrioridade:
        distanciaAtual, cidadeAtual = heapq.heappop(filaPrioridade)

        if distanciaAtual > distancias[cidadeAtual]:
            continue

    for vizinho, peso in grafo[cidadeAtual].items():
        distancia = distanciaAtual + peso

        if distancia < distancias[vizinho]:
            distancias[vizinho] = distancia
            caminho[vizinho] = cidadeAtual
            heapq.heappush(filaPrioridade, (distancia, vizinho))
    
    return distancias, caminho