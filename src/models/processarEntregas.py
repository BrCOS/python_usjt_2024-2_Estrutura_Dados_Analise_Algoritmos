from src.models.rotas import otimizarRotas
from src.utils.prazo import calcularPrazo
from src.utils.caminhoes import definirCaminhao

def processarEntregas(grafo, entregas):
    cidadesDestino = [entrega[0] for entrega in entregas]#acessa o primeiro index da lista (cidade)
    rotasCentros = otimizarRotas(grafo, cidadesDestino)#recebe a rota ja otimizada (dicionario (centro - chave) e ([] de cidades - valores))

    for entrega in entregas:
        cidade, peso, prioridade = entrega#lista de cidades, peso e prioridade do usuario
        for centro, rota in rotasCentros.items():#acessa o centro e a cidade do dicionario
            if cidade in rota:#define o caminhao
                tipoCaminhao, capacidadeRestanteCaminhao, porcentagemUsadaCaminhao, porcentagemRestanteCaminhao = definirCaminhao(peso, prioridade, centro)
                
                distanciaTotal = 0#peso total (distancia) zerado

                #percorrendo a lista de cidades da rota
                for i in range(len(rota) - 1):#-1 p/ nao fugir do index da []
                    cidadeAtual = rota[i]#indice atual da []
                    proximaCidade = rota[i+1]#proxima cidade da [] (a ser entregue)

                    #repassa no grafo p/ garantir que tem uma conexao entre as cidades
                    if cidadeAtual in grafo and proximaCidade in grafo[cidadeAtual]:
                        distanciaTotal += grafo[cidadeAtual][proximaCidade]#passa o peso (distancia) entre as cidades p/ calcular o prazo

                prazo = calcularPrazo(distanciaTotal)
                
                print('\nInformações de Entrega:')
                print(f'Centro: {centro}')
                print(f'Rota: {' -> '.join(rota)}')
                print(f'Cidade de Destino: {cidade}')
                print(f'Prazo de Entrega: {prazo} dias')
                print('Informações do Caminhão:')
                print(f'Caminhão: {tipoCaminhao}')
                print(f'Porcentagem Usada do Caminhão: {porcentagemUsadaCaminhao:.2f}%')
                print(f'Capacidade Restante do Caminhão: {capacidadeRestanteCaminhao:.2f} Ton. ou {porcentagemRestanteCaminhao:.2f}%')