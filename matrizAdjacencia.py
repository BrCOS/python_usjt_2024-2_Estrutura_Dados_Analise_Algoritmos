def criaMatrizAdjacencia(grafo):

    vertices = list(grafo.keys())
    totalVertices = len(vertices)

    matrizAdjacencia = []

    for i in range(totalVertices):
        linha = []

        for j in range(totalVertices):
            linha.append(0)

        matrizAdjacencia.append(linha)

    for i, vertice_origem in enumerate(vertices):
        for vertice_destino, peso in grafo[vertice_origem].items():
            j = vertices.index(vertice_destino)
            matrizAdjacencia[i][j] = peso

    for linha in matrizAdjacencia:
        print(linha)