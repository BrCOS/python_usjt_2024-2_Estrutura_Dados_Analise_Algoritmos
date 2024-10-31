grafo = {
    #centro belem
    'Belem_Centro': {'Belem_1': 85, 'Belem_2': 95},
    'Belem_1': {'Belem_Centro': 85, 'Belem_2': 15, 'Belem_3': 70},
    'Belem_2': {'Belem_Centro': 95, 'Belem_1': 15, 'Belem_4': 55},
    'Belem_3': {'Belem_1': 70, 'Belem_4': 90, 'Belem_5': 100},
    'Belem_4': {'Belem_2': 55, 'Belem_3': 90, 'Belem_5': 10},
    'Belem_5': {'Belem_3': 100, 'Belem_4': 10},

    #centro recife
    'Recife_Centro': {'Recife_1': 60, 'Recife_2': 80},
    'Recife_1': {'Recife_Centro': 60, 'Recife_2': 25, 'Recife_3': 95},
    'Recife_2': {'Recife_Centro': 80, 'Recife_1': 25, 'Recife_4': 75},
    'Recife_3': {'Recife_1': 95, 'Recife_4': 65, 'Recife_5': 85},
    'Recife_4': {'Recife_2': 75, 'Recife_3': 65, 'Recife_5': 20},
    'Recife_5': {'Recife_3': 85, 'Recife_4': 20},

    #centro sao paulo
    'SaoPaulo_Centro': {'SaoPaulo_1': 10, 'SaoPaulo_2': 15, 'Curitiba_Centro': 90},
    'SaoPaulo_1': {'SaoPaulo_Centro': 10, 'SaoPaulo_2': 8, 'SaoPaulo_3': 20},
    'SaoPaulo_2': {'SaoPaulo_Centro': 15, 'SaoPaulo_1': 8, 'SaoPaulo_4': 30},
    'SaoPaulo_3': {'SaoPaulo_1': 20, 'SaoPaulo_4': 5, 'SaoPaulo_5': 45},
    'SaoPaulo_4': {'SaoPaulo_2': 30, 'SaoPaulo_3': 5, 'SaoPaulo_5': 7},
    'SaoPaulo_5': {'SaoPaulo_3': 45, 'SaoPaulo_4': 7, 'Curitiba_1': 70},

    #centro curitiba
    'Curitiba_Centro': {'Curitiba_1': 5, 'Curitiba_2': 15, 'SaoPaulo_Centro': 90},
    'Curitiba_1': {'Curitiba_Centro': 5, 'Curitiba_2': 10, 'Curitiba_3': 40, 'SaoPaulo_5': 70},
    'Curitiba_2': {'Curitiba_Centro': 15, 'Curitiba_1': 10, 'Curitiba_4': 6},
    'Curitiba_3': {'Curitiba_1': 40, 'Curitiba_4': 9, 'Curitiba_5': 20},
    'Curitiba_4': {'Curitiba_2': 6, 'Curitiba_3': 9, 'Curitiba_5': 10},
    'Curitiba_5': {'Curitiba_3': 20, 'Curitiba_4': 10}
}