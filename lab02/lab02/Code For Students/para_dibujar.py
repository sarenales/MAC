import networkx as nx
import matplotlib.pyplot as plt



#Construye un grafo a partir de su matriz de adyacencia
def nuevo_formato(matriz):
    G = nx.Graph()
    G.add_nodes_from(range(0,len(matriz)))
    for i in range(0,len(matriz)):
        for j in range(i, len(matriz)):
            if matriz[i][j]==1:
                G.add_edge(i,j)
    return G

#Dibuja un grafo  
#Pre: Necesita el formato devuelto por nuevo_formato(grafo)    
def dibujar(grafo):
    nx.draw(grafo)
    plt.show()
    plt.clf()

