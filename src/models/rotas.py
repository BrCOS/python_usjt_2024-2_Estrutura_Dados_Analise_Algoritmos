from src.models.dijkstra import dijkstra

#agrupa entregas por centro para serem processadas
#calcula o caminho agrupado mais curto com o dijkstra
#return rota otimizada e destinos agrupados por centro

def otimizarRotas(grafo, entregas):
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
    for cidade, peso, prioridade in entregas:
        for centro, prefixoCentro in centros.items():
            if cidade.startswith(prefixoCentro):#verifica o prefixo das cidades
                centroGrupo[centro].append((cidade, peso, prioridade))#agrupa as cidades por centro (tupla)

    rota = {}#dicionario p/ retornar o caminho final

    #itera sobre o dicionario centroGrupo -> centro (chave), cidade[] (valor)
    for centro, destinos in centroGrupo.items():
        if destinos:#garante se tem entregas p/ centro atual
            #criar lista que tem so o nome das cidades destino do centro atual
            cidadesDestino = [destino[0] for destino in destinos]#acessa o index 0 da lista (cidade destino)
            
            rotaDijkstra = dijkstra(grafo, centro, cidadesDestino)#calcula o menor caminho com base no centro e no grafo
            rota[centro] = rotaDijkstra#centro (chave) e lista ordenada do dijkstra (valores)

    return rota, centroGrupo