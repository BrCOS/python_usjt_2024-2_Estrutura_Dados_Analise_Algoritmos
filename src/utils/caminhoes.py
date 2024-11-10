def definirCaminhao(pesoCarga, prioridade):
    if prioridade and pesoCarga <= 20:
        tipoCaminhao = 'Toco'#tipo do caminhao
        capacidadeCaminhao = 8#capacidade em toneladas
    else:
        tipoCaminhao = 'Truck'
        capacidadeCaminhao = 14

    capacidadeRestante = capacidadeCaminhao - pesoCarga#valor num (provavel int)
    porcentagemUsada = (pesoCarga / capacidadeCaminhao) * 100#valor em porcentagem
    porcentagemRestante = 100 - porcentagemUsada#valor em porcentagem
        
    return tipoCaminhao, capacidadeRestante, porcentagemUsada, porcentagemRestante