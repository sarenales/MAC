


def merge(l1, l2):
    # Precondicion: l1 y l2 estan ordenadas de menor a mayor    
    if l1==[]:
        return l2
    elif l2==[]:
        return l1
    elif l1[0]<l2[0]:
        return [l1[0]] +merge(l1[1:], l2)
    else:
        return [l2[0]] +merge(l2[1:], l1)



def mergeSort(miLista):
    if miLista==[] or len(miLista)==1:
        return miLista
    else:
        mitad = (len(miLista))//2
        izq = mergeSort(miLista[:mitad])
        der = mergeSort(miLista[mitad:])
        completa = merge(izq,der)
        return completa
    

# Para probar tu programa borra """


miLista1 = [54,26,93,17,77,31,44,55,20]
miLista2 = [1, 2, 3, 4, 5]
miLista3 = [2,1]
miLista4 = []

assert(mergeSort(miLista1) == [17, 20, 26, 31, 44, 54, 55, 77, 93])
assert(mergeSort(miLista2) == [1,2,3, 4, 5])
assert(mergeSort(miLista3) == [1,2])
assert(mergeSort(miLista4) == [])
