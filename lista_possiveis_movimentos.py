def lista_movimentos_possiveis (B, cs):
    numero = []
    naipe = []
    for carta in B:
        if len(carta) == 2:
            numero.append (carta [0])
            naipe.append (carta [1])
        else:
            numero.append (10)
            naipe.append (carta [2])
    movimentos = []
    if cs == 0:
        return []
    elif cs >= 3:
            if naipe [cs] == naipe [cs - 3]:
                movimentos.append (3)
            if numero [cs] == numero [cs -3]:
                movimentos.append (3)
            if numero [cs] == numero [cs - 1]:
                movimentos.append (1)
            if naipe[cs] == naipe [cs - 1 ] :
                movimentos.append (1)
    else:
        if numero [cs] == numero [cs - 1]:
            movimentos.append (1)
        if naipe[cs] == naipe [cs - 1 ] :
            movimentos.append (1)
    return movimentos