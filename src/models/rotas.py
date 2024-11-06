from .dijkstra import dijkstra

def rotas(grafo, cidadeDestino):
    centros = {
        'Belem_Centro': 'Belem',
        'Recife_Centro': 'Recife',
        'SaoPaulo_Centro': 'SaoPaulo',
        'Curitiba_Centro': 'Curitiba'
    }

    centroGrupo = {}

    for centro in centros:
        centroGrupo[centro] = []

    for cidade in cidadeDestino:
        for centro, prefixo in centros.items():
            if cidade.startswith(prefixo):
                centroGrupo[centro].append(cidade)
                break

    rota = {}

    for centro, cidadeGrupo in centroGrupo.items():
        caminhosDijkstra = dijkstra(grafo, centro)

        caminhoGrupo = []
        
        cidadeIncluida = set()

        for cidade in cidadeGrupo:
            for ponto in caminhosDijkstra[cidade]:
                if ponto not in cidadeIncluida:
                    caminhoGrupo.append(ponto)
                    cidadeIncluida.add(ponto)

        rota[centro] = caminhoGrupo

    return rota