def definirCaminhao(pesoCarga, prioridade, centro):
    if prioridade and pesoCarga <= 35:
        tipoCaminhao = 'Toco'#tipo do caminhao
        capacidadeCaminhao = 8#capacidade em toneladas
    else:
        tipoCaminhao = 'Truck'
        capacidadeCaminhao = 14

    capacidadeRestanteCaminhao = capacidadeCaminhao - pesoCarga#valor num (provavel int)
    porcentagemUsadaCaminhao = (pesoCarga / capacidadeCaminhao) * 100#valor em porcentagem
    porcentagemRestanteCaminhao = 100 - porcentagemUsadaCaminhao#valor em porcentagem

    if pesoCarga > capacidadeCaminhao:
        print(f'ERRO: O peso máximo do caminhão {tipoCaminhao} do centro {centro}, foi atingido.
              \nSua capacidade é de: {capacidadeCaminhao} e foi utilizado {porcentagemUsadaCaminhao}%')
    
    return tipoCaminhao, capacidadeRestanteCaminhao, porcentagemUsadaCaminhao, porcentagemRestanteCaminhao