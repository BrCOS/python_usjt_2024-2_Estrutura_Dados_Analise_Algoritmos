def definirCaminhao(pesoCarga, prioridade, centro):
    if prioridade and pesoCarga <= 20:
        tipoCaminhao = 'Toco'#tipo do caminhao
        capacidadeCaminhao = 8#capacidade em toneladas
    else:
        tipoCaminhao = 'Truck'
        capacidadeCaminhao = 14

    capacidadeRestante = capacidadeCaminhao - pesoCarga#valor num (provavel int)
    porcentagemUsada = (pesoCarga / capacidadeCaminhao) * 100#valor em porcentagem
    porcentagemRestante = 100 - porcentagemUsada#valor em porcentagem
    
    if pesoCarga > capacidadeCaminhao:
        print(
            f'ERRO: O peso máximo do caminhão {tipoCaminhao} do centro {centro}, foi atingido.'
            f'\nSua capacidade é de: {capacidadeCaminhao} e foi utilizado {porcentagemUsada}%'
            )
        
    return tipoCaminhao, capacidadeRestante, porcentagemUsada, porcentagemRestante