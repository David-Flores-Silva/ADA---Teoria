def divide(lista):
    pivote = lista[0]
    may = []
    men = []

    for i in range(1, len(lista)):
        if pivote > lista[i]:
            men.append(lista[i])  
        else:
            may.append(lista[i])
    
    orden = (men, pivote, may)
    return orden



def quickSort(lista):
    if(len(lista) < 2):
        return lista
    
    men, pivote, may = divide(lista)   
    return quickSort(men) + [pivote] + quickSort(may)


lis = [2, 6, 5, 1, 3, 4]
print(quickSort(lis))

