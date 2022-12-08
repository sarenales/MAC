import networkx as nx
import matplotlib.pyplot as plt



#Construye un grafo a partir de su matriz de adyacencia
def nuevo_formato(matriz):
    G = nx.Graph()
    G.add_nodes_from(range(len(matriz)))
    for i in range(len(matriz)):
        for j in range(i+1, len(matriz)):
            if matriz[i][j]==1:
                G.add_edge(i,j)
    return G

#Dibuja un grafo  
#Pre: Necesita el formato devuelto por nuevo_formato(grafo)    
def dibujar(grafo):
    nx.draw_shell(nuevo_formato(grafo), with_labels = True)
    plt.show()
    plt.clf()

