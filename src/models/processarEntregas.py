from src.utils.prazo import calcularPrazo
from src.utils.controleCaminhoes import Caminhoes

#recebe a rota otimizada do rotas.py
#calcula prazo de cada entrega
#aloca caminhoes

def processarEntregas(grafo, rotasOtimizadas, centroGrupo):
    #iterar sobre cada centro (chave) e destinos (valores)
    for centro, destinos in centroGrupo.items():
        #verificar se tem destinos no dicionario
        if destinos:
            rota = rotasOtimizadas[centro]#passa o centro atual como chave

            #instancia da classe caminhoes p/ cada centro (cria objeto p/ cada centro)
            controleCaminhoes = Caminhoes()

            #soma do peso (distancia) percorridas nas cidades da rota
            distanciaTotal = 0
            
            #armazena os prazos de entrega de cada cidade
            prazosEntrega = {}

            #percorre a lista de cidades da rota
            for i in range(len(rota) - 1):#-1 p/ nao fugir do index da []
                cidadeAtual = rota[i]#indice atual da []
                proximaCidade = rota[i+1]#proxima cidade da [] (a ser entregue)

                #repassa o grafo p/ garantir que tem uma conexao entre as cidades
                if cidadeAtual in grafo and proximaCidade in grafo[cidadeAtual]:
                    distanciaTotal += grafo[cidadeAtual][proximaCidade]#passa o peso (distancia) entre as cidades p/ calcular o prazo

                    #iterar sobre os destinos da [] do centro atual
                    for destino, peso, prioridade in destinos:
                        #garante que a cidade atual == ao destino da [] (o caminhao esta indo p/ cidade de destino)
                        if proximaCidade == destino:
                            #usado um try por conta do erro personalizado na classe caminhoes
                            try:
                                #chama o metodo da classe caminhoes p/ alocar o peso da carga no caminhao
                                controleCaminhoes.alocarCarga(peso, prioridade)
                            except ValueError as e:#caso capacidade ultrapassada aconteca
                                print(f'Erro no Centro {centro}: {e}')#informa o centro e a msg da classe
                                return

                            #calcular os prazos de entrega (distancia acumulada ate o destino)
                            prazoEntrega = calcularPrazo(distanciaTotal)

                            #passa a cidade destino como chave e o prazo como valor do dic
                            prazosEntrega[destino] = prazoEntrega
            
            print(f'\nInformações de Entrega para o Centro: {centro}')
            print(f'Rota: {' -> '.join(rota)}')
            for destino, peso, prioridade in destinos:
                print(f'\nCidade de Destino: {destino}')
                print(f'Peso da Carga: {peso} toneladas')
                print(f'Prazo de Entrega: {prazosEntrega[destino]} dias.\n')

            controleCaminhoes.printCaminhoes()