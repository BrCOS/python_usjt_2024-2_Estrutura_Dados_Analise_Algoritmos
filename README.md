# Estrutura de Dados e Análise de Algoritmos
##### Otimização Logística com Múltiplos Centros de Distribuição 


## Time

| Nome                             |RA         |
| ---------------------------------| --------- |
| Bruno Costa Carvalho             | 821116933 |
| Erik Akio Matsumoto              | 821115561 |
| Gabriel Guardiano do Nascimento  | 821145633 |
| Mariana de Moraes Marcondes      | 821116771 |
| Renan Moura Silva                | 821145633 | 
| Vinícius Peralta                 | 821222997 |


## Objetivo

Desenvolver um algorítmo que otimize o roteamento de entregas entre centros de distribuição e cidades próximas, considerando a capacidade dos caminhões, prioridade das entregas, e distâncias entre locais, para minimizar o tempo e a distância percorrida.

## Parâmetros Utilizados

- 2 Caminhões por centro (Truck e Toco), com 14 e 8 toneladas cada, respectivamente.
- Os motoristas dirigem em uma velocidade média de 90 km/h por 10 horas diárias.
- Entregas de com prioridade e com uma distância menor do que 300km do centro de distribuição mais perto, devem ser enviadas através do caminhão toco.
- É gerado um grafo para cada centro de distribuição, considerando as cidades de destino.
- O algoritmo de Dijkstra é utilizado para gerar a ordem das entregas com base na distância e prioridade.
