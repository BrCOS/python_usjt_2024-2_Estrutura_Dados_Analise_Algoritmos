from data.dicionarioGrafo import grafo
from src.utils.inputEntregas import entradaUsuario
from src.models.processarEntregas import processarEntregas

def main():
    entregas = entradaUsuario(grafo)
    processarEntregas(grafo, entregas)

main()