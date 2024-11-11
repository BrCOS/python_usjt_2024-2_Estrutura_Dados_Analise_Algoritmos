from data.dicionarioGrafo import grafo
from src.utils.inputEntregas import entradaUsuario
from src.models.processarEntregas import processarEntregas
from src.models.rotas import otimizarRotas

def main():
    entregas = entradaUsuario(grafo)
    rotaOtimizada, centroGrupo = otimizarRotas(grafo, entregas)
    processarEntregas(grafo, rotaOtimizada, centroGrupo)

main()