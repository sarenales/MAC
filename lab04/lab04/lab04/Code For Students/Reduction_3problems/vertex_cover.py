
def partial_validity_check(cover, graph):
    for i in range(len(graph)):
        for j in range(i+1,len(graph)):  
              if ((graph[i][j]==1) and (cover[i]==0) and (cover[j]==0)):
                  return False
    return True


def solve_vc(graph):
    n = len(graph)
    cover = [None]*n
    return recursive_vertex_cover_2(graph, cover)



def next_None(cover):
    for i in range(len(cover)):
        if cover[i] == None:
            return i
    return None
    
    

def recursive_vertex_cover_2(graph, cover):

 
    if not partial_validity_check(cover, graph):
      return [1]*len(cover)
    else:
      v = next_None(cover)
      if v == None:
          return cover
      else:
        copy_cover = list(cover)
        cover[v] = 0
        c0 = recursive_vertex_cover_2(graph, cover)
        copy_cover[v] = 1
        c1 = recursive_vertex_cover_2(graph, copy_cover)
        return c0 if c0.count(1) < c1.count(1) else c1

    
