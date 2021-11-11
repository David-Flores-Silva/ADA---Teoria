#from Proyecto.HeapSort import heapsort
#from Proyecto.InsertionSort import InsertionSort
#from Proyecto.QuickSort import quickSort

def Heap(lst):
    heapsort(lst)
    print(lst)

def Quick(lst):
    print(quickSort(lst))

def Insertion(lst):
    print(InsertionSort(lst))


print("Hola... ingrese los datos a ordenar \ncuando ya no desee mas entradas presione 100 \n")
entrada = int(input("number: "))
orden = []

while entrada != 100:
    orden.append(entrada)
    entrada = int(input("otro: "))

print("escoja el tipo de ordenamiento que desee realizar")
opcion = int(input("1. HeapSort \t 2. QuickSort \t 3. InsertionSort"))

if opcion == 1:
    Heap(orden)
elif opcion == 2:
    Quick(orden)
elif opcion == 3:
    Insertion(orden)


