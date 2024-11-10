def entradaUsuario(grafo):
    #lista vazia p/ iterar com os dados recebidos
    entregas = []

    #dados a serem recebidos do terminal
    while True:
        cidadeDestino = (
            input('Digite a cidade para onde quer entregar: ').strip()
            .upper()
            .replace('B', 'Belem_')
            .replace('C', 'Curitiba_')
            .replace('S', 'SaoPaulo_')
            .replace('R', 'Recife_')
        )

        if cidadeDestino not in grafo:
            print('Cidade não existente, por favor insira uma cidade válida.')
            break#para o codigo se a cidade nao existir

        peso = float(input('Digite o peso da carga: '))
        prioridade = input('Entrega prioritária? (S/N): ').strip().upper() == 'S'

        entregas.append((cidadeDestino, peso, prioridade))#adiciona os valores recebidos na lista

        mais_entregas = input('Deseja realizar mais uma entrega? (S/N): ').strip().upper()
        if mais_entregas != 'S':
            break#se nao houver mais entregas, parar o codigo
    
    return entregas#cidade, peso e prioridade (ordem)