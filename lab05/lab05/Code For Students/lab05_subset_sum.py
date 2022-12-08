
from time import time
import itertools


# la funcion has_sum, dada una coleccion de positivos y un valor "value", decide si
# una subcoleccion de positivos que sumen "value" o no.    
def has_sum(value, collection):
  # Pre: value>=0 y los elementos de collection son positivos
  if value==0:
      return True
  elif collection==[]:
      return False
  elif collection[0] > value:
      return has_sum(value, collection[1:])
  else:
      return has_sum(value-collection[0], collection[1:]) or has_sum(value,collection[1:])


# la funcion subset, dada una coleccion de positivos y un valor "value", si existe
# una subcoleccion de positivos que sumen "value" devuelve dicha subcoleccion.
# En otro caso devuelve la lista [None].    
def subset(value, collection):
    if value==0:
        return []
    elif collection==[]:
        return [None]
    elif collection[0] > value:
        return subset(value, collection[1:])
    else:
        # metemos en l los elementos que sumen ese valor
        l = subset(value-collection[0], collection[1:])
        if l!=[None]:   # me devuelve bien
            return  [collection[0]]+l
        else:
            return subset(value,collection[1:])
            

# funcion auxiliar para añadir un elemento en una lista de listas              
def add(e, ll):
    return [[e]+elem for elem in ll]



# la funcion all_subsets me devuelve una lista con todas las posibles soluciones
def all_subsets(value, collection):
    if value==0:
        return [[]]
    elif collection==[]:
        return [None]
    elif collection[0] > value:
        return all_subsets(value, collection[1:])
    else:
        # si ha ido bien, metemos en l los elementos que sumen ese valor
        l1 = all_subsets(value-collection[0], collection[1:])
        # si ha ido mal, no metemos
        l2 = all_subsets(value,collection[0])
        if l1==[None] and l2!=[None]:
            return l2
        elif l1!=[None] and l2==[None]:
            return add(collection[0],l1)
        elif l1!=[None] and l2!=[None]:
            return l2+add(collection[0], l1)
        else: 
            return [None]
                          
        

def test():
    
    # coleccion 0
    collection0 = [3, 11, 8, 13, 16, 1, 6]
    value0 = 59
    
    
    # Primera coleccion
    collection1 = [3, 11, 8, 13, 16, 1, 6]
    value1 = 21
    

    sol11 = [3, 11, 1, 6]
    perm11 = [list(t) for t in itertools.permutations(sol11)]
    perm12 = [[13, 8], [8, 13]]
   
    # Segunda coleccion
    collection2 = [518533, 1037066, 2074132, 1648264,
                   796528, 1593056, 686112, 1372224,
                   244448, 488896, 977792, 1955584,
                   1411168, 322336, 644672, 1289344,
                   78688, 157376, 314752, 629504, 1259008]
    value2 = 2463098
    
    sol21 = [1037066, 796528, 629504] 
    perm21 =[list(t) for t in itertools.permutations(sol21)]
    
    # Tercera coleccion
    collection3 = [15, 22, 14, 26, 32, 9, 16, 8]
    value3 = 53
    
    
    sol31 = [15, 22, 16]
    perm31 = [list(t) for t in itertools.permutations(sol31)]
    sol32 = [14, 15, 16, 8]
    perm32 = [list(t) for t in itertools.permutations(sol32)]   
    sol33 = [9, 22, 14, 8]
    perm33 = [list(t) for t in itertools.permutations(sol33)]
    
    #Cuarta coleccion
    collection4 = [1,5,6]
    value4 = 6
    perm41 = [[6], [1, 5], [5, 1]]
    
    
    #Quinta coleccion
    collection5 = [4,5,1]
    value5 = 6
    perm51 = [[1, 5], [5, 1]]
    
    #Sexta coleccion
    collection6 = [6, 400,100, 6, 10, 20, 30, 40, 3, 4]
    value6 = 7
    perm61 = [[3, 4], [4, 3]]
    
    
#   DESCOMENTAR PARA PROBAR HAS_SUM
#######################################################    
    assert not has_sum(value0, collection0)
    assert has_sum(value1, collection1)
    assert has_sum(value2, collection2)
    assert has_sum(value3, collection3)
    assert has_sum(value4, collection4)
    assert has_sum(value5, collection5)
    assert has_sum(value6, collection6)
    
    
#   DESCOMENTAR PARA PROBAR SUBSET
###############################################################
    assert subset(value0, collection0) == [None]
    assert subset(value1, collection1) in perm11 + perm12 
    assert subset(value2, collection2) in perm21
    assert  subset(value3, collection3) in perm31 + perm32 + perm33
    assert subset(value4, collection4) in perm41 
    assert subset(value5, collection5) in perm51
    assert subset(value6, collection6) in perm61
    

##   DESCOMENTAR PARA PROBAR ALL_SUBSETS    
##############################################################
    assert all_subsets(value0, collection0) == [None]

    all_solutions1 = all_subsets(value1, collection1)
    assert len(all_solutions1) == 2
    assert all_solutions1[0] in perm11 + perm12
    assert all_solutions1[1] in perm11 + perm12
    
    all_solutions2 = all_subsets(value2, collection2)
    assert len(all_solutions2) == 1
    assert all_solutions2[0] in perm21
    
        
    all_solutions3 = all_subsets(value3, collection3)
    assert len(all_solutions3) == 3
    assert all_solutions3[0] in perm31 + perm32 + perm33
    assert all_solutions3[1] in perm31 + perm32 + perm33
    assert all_solutions3[2] in perm31 + perm32 + perm33
    
    
    all_solutions4 = all_subsets(value4, collection4)       
    assert len(all_solutions4) == 2
    assert all_solutions4[0] in perm41
    assert all_solutions4[1] in perm41
    
    all_solutions5 = all_subsets(value5, collection5)     
    assert len(all_solutions5) == 1
    assert all_solutions5[0] in perm51
    
    
### PARA MEDIR TIEMPO USA ESTA COLECCION QUE NO TIENE SUBSECCIONES
### QUE SUMEN VALUE6
####################################################################    
    # collection6 = list(range(1,25))
    # value6 = 301
    # assert subset(value6, collection6) == [None]
 
    
 
start_time = time()
test()
elapsed_time = time() - start_time   
print("Elapsed time: %0.10f seconds." % elapsed_time)   