
import copy
from time import time
from para_dibujar import dibujar, nx
from pysat.solvers import Minisat22
from pysat.card import CardEnc



def answer_sat(graph, k):
        code = reduce_VC_to_SAT(graph,k)
        with Minisat22(bootstrap_with=code) as sat:
            return sat.solve(), sat.get_model()
        
def sol(graph):
   # with Minisat22(bootstrap_with=[]) as sat:
           answer = binary_search(graph, 0, len(graph)-1)
           print("El minimo vertex_cover contiene: " + str(answer[0]) + 
                 " nodos \n" + "La respuesta del SAT-solver es:" + str(answer[1][0:len(graph)]) + 
                 "\n" + "Corresponde al vertex_cover:"
                 +  str([1 if elem > 0 else 0 for elem in answer[1][0:len(graph)]]))
           # dibujar(graph)        
    
    
def reduce_VC_to_SAT(graph, k):
    # ejercicio 1
    # devulve la lista de clausulas al pasar el grafo
    
    num_clauses = 0
    resul = []
    for i in range(len(graph)):
        for j in range(i+1, len(graph)):
            if graph[i][j] == 1:
                new_clause = [i+1,j+1]
                resul.append(new_clause)
                num_clauses = num_clauses + 1
    list_var = [a for a in range(1, len(graph)+1)]
    constraint = CardEnc.atmost(list_var, k)
    num_clauses = num_clauses + len(constraint.clauses)
    return resul + constraint.clauses


def binary_search(graph, low, high):
    # ejercicio 2
    
    k = (high+low)//2
    boolen , modelo = answer_sat(graph, k)
    if high > low:
        if boolen == False:
            return binary_search(graph, k+1, high)
        elif boolen == True:
            return binary_search(graph,low, k)
    else:
        return (k, modelo)
     

    
            
def cover_2(graph):     
    #ejercicio 3
    """while hay aristas sin cubrir:
        e = una arista sin cubrir
        añade los dos nodos de e al cover
        elimina las aristas adyacentes a los dos nodos"""
    
    VC = []
    g = copy.deepcopy(graph)
    cont_aristas_total = 0
    i=0
    for i in range(len(g)):
       cont_aristas_total += g[i].count(1) 
    cont_aristas_total = ((cont_aristas_total-len(g))//2)
    # print("total de aristas: ",cont_aristas_total)
    
    while cont_aristas_total>0:  
        for i in range(len(g)):
            for j in range(i+1, len(g)):
                if g[i][j] != None:
                    valor = g[i][j]
                    if valor == 1:
                        # anadimos los dos nodos de la arista
                        VC.append(i)
                        VC.append(j)
                        # print(VC)
                        # disminuimos cont
                        cont_aristas_total = cont_aristas_total - (g[i][i+1:len(g)]).count(1) - (g[j][i+1:len(g)]).count(1)
                        # print("quedan",cont_aristas_total, " aristas")
                        # aristas visitadas = None
                        g[i][j] = None
                        g[j][i] = None #ns si hace falta realmente
                        # print(g)
                        # eliminar aristas adyacentes de los nodos
                        for a in range(len(g[i])):
                            if g[i][a] == 1:
                                g[i][a] = None
                        for b in range(len(g[j])):
                            if g[j][b] == 1:
                                g[j][b] = None
                        # print(g)
    return(len(VC))
                    

    


def greedy(graph): 
    #ejercicio 4
    """while hay aristas sin cubrir:
        v= el nodo que mas aristas cubra 
        añade v al cover
        elimina las aristas adyacentes a v"""
    
    g = copy.deepcopy(graph)
    # contamos el numero de aristas por cada nodo
    num_aristas_nodo = []
    cont_aristas_total = 0 
    for i in range(0, len(g)):
        num_aristas_nodo.append((g[i].count(1))-1)
        cont_aristas_total += g[i].count(1) 
    #print("Inicial:",num_aristas_nodo)
    cont_aristas_total = (cont_aristas_total - len(g))//2
    #print("Numero de aristas totales: ", cont_aristas_total, "\n")
    
    seleccionados = []
    c=0
    while cont_aristas_total > 0:
        
        # buscamos el indice del nodo con mayor numero de aristas
        pos_mayor = num_aristas_nodo.index(max(num_aristas_nodo))
        #print("Mayor de la vuelta ", c, ", es el de la posicion/fila: " ,pos_mayor)
        
        # anadimos el mayor de la lista
        seleccionados.append(pos_mayor)
        #print("Seleccionados para el VC de la vuelta : " ,seleccionados)
        
        
        cont_aristas_total = cont_aristas_total - g[pos_mayor].count(1)
        #print("Tenemos ahora ", cont_aristas_total, " arista(s) sin cubrir.")
        
        # 0 de la lista de numero aristas nodos
        num_aristas_nodo[pos_mayor] = -1
        #print("Resto de la vuelta antes : " ,num_aristas_nodo)
        
        for i in range(len(num_aristas_nodo)):
            if i != pos_mayor:
                num_aristas_nodo[i] = num_aristas_nodo[i]-1
                
        
        
        # -1 en el grafo adyacencias
        # for i in range(len(g[pos_mayor])):
        #         for j in range(i, len(g)):
        #             if i != j:
        #                 valor = g[i][j]
        #                 if valor == 1:
        #                     num_aristas_nodo[i] -=1
        #                     print("Resto de la vuelta depue : " ,num_aristas_nodo)
        #                     for d in range(len(g[j])):
        #                         g[i][d] = -1
        #                     print("Grafo: ",g)
                    
        #print("--------------")
        c+=1
    return(len(seleccionados)) 
                 
    

if __name__ == '__main__':    
    
    g0 =[[1, 0, 1, 0, 0],
         [0, 1, 0, 1, 0],
         [1, 0, 1, 1, 0],
         [0, 1, 1, 1, 1],
         [0, 0, 0, 1, 1]]
        
    start_time = time()
    voraz = greedy(g0)
    factor = cover_2(g0)
    print("Respuesta para el grafo g0")
    print("El algoritmo greedy devuelve: " + str(voraz)) 
    print("El algoritmo cover_2 devuelve: " + str(factor))
    sol(g0)
    elapsed_time = time() - start_time   
    print("Elapsed time: %0.10f seconds." % elapsed_time + "\n")   

    
    g1 = [[1, 1, 1],
          [1, 1, 0],
          [1, 0, 1]]
    
    start_time = time()
    voraz = greedy(g1)
    factor = cover_2(g1)
    print("Respuesta para el grafo g1")
    print("El algoritmo greedy devuelve: " + str(voraz)) 
    print("El algoritmo cover_2 devuelve: " + str(factor))
    sol(g1)
    elapsed_time = time() - start_time   
    print("Elapsed time: %0.10f seconds." % elapsed_time + "\n")   

    g2 = [[1, 1, 1, 1],
          [1, 1, 0, 1],
          [1, 0, 1, 1],
          [1, 1, 1, 1]]
    
    start_time = time()
    voraz = greedy(g2)
    factor = cover_2(g2)
    print("Respuesta para el grafo g2")
    print("El algoritmo greedy devuelve: " + str(voraz)) 
    print("El algoritmo cover_2 devuelve: " + str(factor))
    sol(g2)
    elapsed_time = time() - start_time   
    print("Elapsed time: %0.10f seconds." % elapsed_time + "\n")   
    
    g3 = [[1, 0, 1, 1, 0],
          [0, 1, 1, 0, 1],
          [1, 1, 1, 1, 1],
          [1, 0, 1, 1, 0],
          [0, 1, 1, 0, 1]]
    
    start_time = time()
    voraz = greedy(g3)
    factor = cover_2(g3)
    print("Respuesta para el grafo g3")
    print("El algoritmo greedy devuelve: " + str(voraz)) 
    print("El algoritmo cover_2 devuelve: " + str(factor))
    sol(g3)
    elapsed_time = time() - start_time   
    print("Elapsed time: %0.10f seconds." % elapsed_time + "\n")   
    
    g4 = [[1, 0, 1, 0],
          [0, 1, 1, 0],
          [1, 1, 1, 1],
          [0, 0, 1, 1]]
    
    
    start_time = time()
    voraz = greedy(g4)
    factor = cover_2(g4)
    print("Respuesta para el grafo g4")
    print("El algoritmo greedy devuelve: " + str(voraz)) 
    print("El algoritmo cover_2 devuelve: " + str(factor))
    sol(g4)
    elapsed_time = time() - start_time   
    print("Elapsed time: %0.10f seconds." % elapsed_time + "\n")   
    
    g5 =  [[1, 1, 1, 0, 0, 1],
           [1, 1, 1, 0, 0, 0],
           [1, 1, 1, 1, 1, 0],
           [0, 0, 1, 1, 1, 0],
           [0, 0, 1, 1, 1, 1],
           [1, 0, 0, 0, 1, 1]]
    
    start_time = time()
    voraz = greedy(g5)
    factor = cover_2(g5)
    print("Respuesta para el grafo g5")
    print("El algoritmo greedy devuelve: " + str(voraz)) 
    print("El algoritmo cover_2 devuelve: " + str(factor))
    sol(g5)
    elapsed_time = time() - start_time   
    print("Elapsed time: %0.10f seconds." % elapsed_time + "\n")   
    
    g6 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

    
    start_time = time()
    voraz = greedy(g6)
    factor = cover_2(g6)
    print("Respuesta para el grafo g6")
    print("El algoritmo greedy devuelve: " + str(voraz)) 
    print("El algoritmo cover_2 devuelve: " + str(factor))
    sol(g6)
    elapsed_time = time() - start_time   
    print("Elapsed time: %0.10f seconds." % elapsed_time + "\n")   
         
    g7 = [[1, 1, 1, 0, 0, 0],
          [1, 1, 0, 1, 1, 0],
          [1, 0, 1, 1, 0, 1],
          [0, 1, 1, 1, 0, 0],
          [0, 1, 0, 0, 1, 0],
          [0, 0, 1, 0, 0, 1]]

    
    start_time = time()
    voraz = greedy(g7)
    factor = cover_2(g7)
    print("Respuesta para el grafo g7")
    print("El algoritmo greedy devuelve: " + str(voraz)) 
    print("El algoritmo cover_2 devuelve: " + str(factor))
    sol(g7)
    elapsed_time = time() - start_time   
    print("Elapsed time: %0.10f seconds." % elapsed_time + "\n")   
           
    g8 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    
    start_time = time()
    voraz = greedy(g8)
    factor = cover_2(g8)
    print("Respuesta para el grafo g8")
    print("El algoritmo greedy devuelve: " + str(voraz)) 
    print("El algoritmo cover_2 devuelve: " + str(factor))
    sol(g8)
    elapsed_time = time() - start_time   
    print("Elapsed time: %0.10f seconds." % elapsed_time + "\n")   
          
    
    g = nx.circulant_graph(200, [1,3, 199, 200])
    g9 = [[0 for i in range(0,200)] for j in range(0,200)]
    for i in range(200):
        g9[i][i] = 1
    for edge in g.edges:
        g9[edge[0]][edge[1]] = 1
        g9[edge[1]][edge[0]] = 1
    
    start_time = time()
    voraz = greedy(g9)
    factor = cover_2(g9)
    print("Respuesta para el grafo g9")
    print("El algoritmo greedy devuelve: " + str(voraz)) 
    print("El algoritmo cover_2 devuelve: " + str(factor))
    sol(g9)
    elapsed_time = time() - start_time   
    print("Elapsed time: %0.10f seconds." % elapsed_time + "\n")   
    
    
    g = nx.circulant_graph(100, [1,3,5,7,9,10,15,18, 20, 23, 25, 30, 40, 50, 60, 65, 70, 80, 81])
    g10 = [[0 for i in range(0,100)] for j in range(0,100)]
    for i in range(100):
        g10[i][i] = 1
    for edge in g.edges:
        g10[edge[0]][edge[1]] = 1
        g10[edge[1]][edge[0]] = 1
    
    
    start_time = time()
    voraz = greedy(g10)
    factor = cover_2(g10)
    print("Respuesta para el grafo g10")
    print("El algoritmo greedy devuelve: " + str(voraz)) 
    print("El algoritmo cover_2 devuelve: " + str(factor))
    sol(g10)
    elapsed_time = time() - start_time   
    print("Elapsed time: %0.10f seconds." % elapsed_time + "\n")   
    
    
    g11 = [[0 for i in range(0,200)] for j in range(0,200)]
    for i in range(0,200):
        g11[i][i] = 1
        g11[len(g11)-1][i] = 1
        g11[i][len(g11)-1] = 1
        
    
    start_time = time()
    voraz = greedy(g11)
    factor = cover_2(g11)
    print("Respuesta para el grafo g11")
    print("El algoritmo greedy devuelve: " + str(voraz)) 
    print("El algoritmo cover_2 devuelve: " + str(factor))
    sol(g11)
    elapsed_time = time() - start_time   
    print("Elapsed time: %0.10f seconds." % elapsed_time + "\n")   
    
    g12 = [[1 for i in range(0,300)] for j in range(0,300)]
    for i in range(0,300):
        g12[i][i] = 1
        
    start_time = time()
    voraz = greedy(g12)
    factor = cover_2(g12)
    print("Respuesta para el grafo g12")
    print("El algoritmo greedy devuelve: " + str(voraz)) 
    print("El algoritmo cover_2 devuelve: " + str(factor))
    sol(g12)
    elapsed_time = time() - start_time   
    print("Elapsed time: %0.10f seconds." % elapsed_time + "\n")   
    
