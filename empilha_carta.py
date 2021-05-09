def empilha(lista, comeco, fim):
    i = lista[comeco]
    lista.remove(lista[comeco])
    lista.remove(lista[fim])
    lista.insert(fim, i)
    return lista