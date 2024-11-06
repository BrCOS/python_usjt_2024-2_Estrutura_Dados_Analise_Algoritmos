import heapq

def dijkstra(grafo, inicio):
    distancias = {cidade: float('inf') for cidade in grafo}
    distancias[inicio] = 0
    rota = {cidade: [] for cidade in grafo}
    rota[inicio] = [inicio]
    
    filaPrioridade = [(0, inicio)]

    while filaPrioridade:
        distanciaAtual, cidadeAtual = heapq.heappop(filaPrioridade)

        if distanciaAtual > distancias[cidadeAtual]:
            continue

        for vizinho, peso in grafo[cidadeAtual].items():
            distancia = distanciaAtual + peso

            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                rota[vizinho] = rota[cidadeAtual] + [vizinho]
                heapq.heappush(filaPrioridade, (distancia, vizinho))
    
    return rota
