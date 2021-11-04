def InsertionSort(lista):
    for j in range(1, len(lista)):
        i = j
        while i != 0:
            if lista[i] < lista[i-1]:
                aux = lista[i-1]
                lista[i-1] = lista[i]
                lista[i] = aux

            i-=1

    return lista

    
lis = [2, 6, 5, 1, 3, 4]
print(InsertionSort(lis))

