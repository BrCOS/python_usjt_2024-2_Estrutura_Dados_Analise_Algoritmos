import math

def calcularPrazo(distancia, velocidadeMedia=70, horasTrabalhadas=10):

    #20 peso do grafo = 700km
    distanciaKm = (distancia / 20) * 700

    if distanciaKm <= 20:
        return 1#entrega em 1 dia
    
    horasTotal = distanciaKm / velocidadeMedia
    diasTotal = horasTotal / horasTrabalhadas

    #arredonda para o dia inteiro mais proximo
    dias = math.ceil(diasTotal)

    return dias