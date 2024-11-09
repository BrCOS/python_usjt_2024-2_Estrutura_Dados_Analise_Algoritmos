from src.models.dijkstra import dijkstra

def otimizarRotas(grafo, cidadeDestino):
    centros = {
        'Belem_Centro': 'Belem',
        'Recife_Centro': 'Recife',
        'SaoPaulo_Centro': 'SaoPaulo',
        'Curitiba_Centro': 'Curitiba'
    }

    #agrupa os centros pelas cidades passadas
    #centro = chave e lista vazia (cidades) = valores
    centroGrupo = {centro: [] for centro in centros}

    #passa as cidades para a [] do dicionario centroGrupo
    for cidade in cidadeDestino:
        for centro, prefixoCentro in centros.items():
            if cidade.startswith(prefixoCentro):#verifica o prefixo das cidades
                centroGrupo[centro].append(cidade)#agrupa as cidades por centro

    rota = {}#dicionario p/ retornar o caminho final

    #itera sobre o dicionario centroGrupo -> centro (chave), cidade[] (valor)
    for centro, cidadeGrupo in centroGrupo.items():
        caminhosDijkstra = dijkstra(grafo, centro)#calcula o menor caminho com base no centro e no grafo

        caminhoGrupo = []#caminho final dos centros
        cidadeVisitada = set()#set p/ n ter cidades duplicadas (ja visitadas)

        #uso do alg. de dijkstra
        #p/ cada cidade da lista com base no centro
        for cidade in cidadeGrupo:
            for ponto in caminhosDijkstra[cidade]:#percorre o menor caminho
                if ponto not in cidadeVisitada:#ponto == aresta
                    caminhoGrupo.append(ponto)#adiciona o caminho final na lista
                    cidadeVisitada.add(ponto)#adiciona as cidades que ja visitadas

        #caminho p/ cada centro
        #centro (chave) e cidades [] (valores)
        rota[centro] = caminhoGrupo #rota[centro] += caminhoGrupo -> duplica as cidades (valores)

    return rota