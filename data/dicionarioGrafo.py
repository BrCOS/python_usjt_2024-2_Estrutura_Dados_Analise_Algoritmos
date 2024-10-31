grafo = {
    # Centro Belém
    'Belem_1': {'Belem_2': 85, 'Belem_3': 95},
    'Belem_2': {'Belem_1': 85, 'Belem_3': 15, 'Belem_4': 70},
    'Belem_3': {'Belem_1': 95, 'Belem_2': 15, 'Belem_5': 55},
    'Belem_4': {'Belem_2': 70, 'Belem_5': 90, 'Belem_6': 100},
    'Belem_5': {'Belem_3': 55, 'Belem_4': 90, 'Belem_6': 10},
    'Belem_6': {'Belem_4': 100, 'Belem_5': 10},

    # Centro Recife
    'Recife_1': {'Recife_2': 60, 'Recife_3': 80},
    'Recife_2': {'Recife_1': 60, 'Recife_3': 25, 'Recife_4': 95},
    'Recife_3': {'Recife_1': 80, 'Recife_2': 25, 'Recife_5': 75},
    'Recife_4': {'Recife_2': 95, 'Recife_5': 65, 'Recife_6': 85},
    'Recife_5': {'Recife_3': 75, 'Recife_4': 65, 'Recife_6': 20},
    'Recife_6': {'Recife_4': 85, 'Recife_5': 20},

    # Centro São Paulo
    'SaoPaulo_1': {'SaoPaulo_2': 10, 'SaoPaulo_3': 15, 'Curitiba_1': 90},
    'SaoPaulo_2': {'SaoPaulo_1': 10, 'SaoPaulo_3': 8, 'SaoPaulo_4': 20},
    'SaoPaulo_3': {'SaoPaulo_1': 15, 'SaoPaulo_2': 8, 'SaoPaulo_5': 30},
    'SaoPaulo_4': {'SaoPaulo_2': 20, 'SaoPaulo_5': 5, 'SaoPaulo_6': 45},
    'SaoPaulo_5': {'SaoPaulo_3': 30, 'SaoPaulo_4': 5, 'SaoPaulo_6': 7},
    'SaoPaulo_6': {'SaoPaulo_4': 45, 'SaoPaulo_5': 7, 'Curitiba_2': 70},

    # Centro Curitiba
    'Curitiba_1': {'Curitiba_2': 5, 'Curitiba_3': 15, 'SaoPaulo_1': 90},
    'Curitiba_2': {'Curitiba_1': 5, 'Curitiba_3': 10, 'Curitiba_4': 40, 'SaoPaulo_6': 70},
    'Curitiba_3': {'Curitiba_1': 15, 'Curitiba_2': 10, 'Curitiba_5': 6},
    'Curitiba_4': {'Curitiba_2': 40, 'Curitiba_5': 9, 'Curitiba_6': 20},
    'Curitiba_5': {'Curitiba_3': 6, 'Curitiba_4': 9, 'Curitiba_6': 10},
    'Curitiba_6': {'Curitiba_4': 20, 'Curitiba_5': 10}
}