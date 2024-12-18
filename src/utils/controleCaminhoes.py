class Caminhoes:
    def __init__(self, capacidadeToco=8, capacidadeTruck=14):
        self.capacidadeToco = capacidadeToco
        self.capacidadeTruck = capacidadeTruck
        self.pesoTotal = {
                            'Toco': 0,
                            'Truck': 0
                        }


    def alocarCarga(self, pesoCarga, prioridade, prazo):
        #define o caminhao conforme a capacidade e o peso da carga
        if prioridade and pesoCarga <= self.capacidadeToco and prazo < 2:
            tipoCaminhao = 'Toco'
            capacidadeCaminhao = self.capacidadeToco
        else:
            tipoCaminhao = 'Truck'
            capacidadeCaminhao = self.capacidadeTruck

        #atualizar a carga
        self.pesoTotal[tipoCaminhao] += pesoCarga
        porcentagemUsada = (self.pesoTotal[tipoCaminhao] / capacidadeCaminhao) * 100

        #verifica se a capacidade foi ultrapassada (gera erro)
        if self.pesoTotal[tipoCaminhao] > capacidadeCaminhao:
            porcentagemUltrapassada = porcentagemUsada - 100
            raise ValueError(f'A Capacidade do {tipoCaminhao}, foi ultrapassada em {porcentagemUltrapassada:.2f}%.')


    def printCaminhoes(self):
        print('Informações dos Caminhões:')

        for tipo, capacidade in [('Toco', self.capacidadeToco), ('Truck', self.capacidadeTruck)]:
            pesoAtual = self.pesoTotal[tipo]

            porcentagemUsada = (pesoAtual / capacidade) * 100
            porcentagemRestante = 100 - porcentagemUsada

            print(f'\nCaminhão Tipo: {tipo}')
            print(f'Peso Atual: {pesoAtual} / {capacidade} Toneladas.')
            print(f'Porcentagem Utilizada: {porcentagemUsada:.2f}%')
            print(f'Porcentagem Restante: {porcentagemRestante:.2f}%')