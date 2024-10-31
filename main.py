from data.dicionarioGrafo import grafo
from src.models.dijkstra import dijkstra

def main():
    distancias, caminho = dijkstra(grafo, 'Belem_Centro')
    
    print('Distancias: ', distancias)
    print('\n')
    print('Caminho: ', caminho)

main()