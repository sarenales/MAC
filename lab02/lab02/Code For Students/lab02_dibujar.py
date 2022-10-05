#  pipinstall network
#  python3 -m pip install -U pip
#  python3 -m pip intall -U matplotlib

import para_dibujar as dib

def test():
    g1 = [[0, 1, 1, 0, 0],
          [1, 0, 1, 1, 1],
          [1, 1, 0, 1, 1],
          [0, 1, 1, 0, 1],
          [0, 1, 1, 1, 0]]
    
    G1 = dib.nuevo_formato(g1)
    dib.dibujar(G1)
    
    g2 = [[1,1,1,0],
          [1,0,1,0],
          [1,0,0,1],
          [0,1,0,1]]
    G2 = dib.nuevo_formato(g2)
    dib.dibujar(G2)
    
    
    
       
test()
