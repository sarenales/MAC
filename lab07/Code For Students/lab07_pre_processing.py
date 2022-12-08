import copy

def actualizar_clausula(clauses, assignment):
    f = copy.deepcopy(clauses)
    for i in range(len(assignment)):
        if assignment[i]==1:
            f = [clause for clause in f if i not in clause]
            for clause in f:
                while -i in clause:
                    clause.remove(-i)
        elif assignment[i] == 0:
            f = [clause for clause in f if -i not in clause]
            for clause in f:
                while i in clause:
                    clause.remove(i)
    return f

def elemento_solo(num_variables, clauses, assignment):
    # buscamos aquellos literales que tengan solo un elemento
    lista = [clause[0] for clause in clauses if len(clause) == 1]
    if list:
        for i in lista:
            if i > 0:
                assignment[i] = 1
            else: 
                assignment[-i]= 0
            # hay que actualizar las clausula
        nueva_clausula = actualizar_clausula(clauses, assignment) 
        return True, nueva_clausula
    else:
        return False,clauses

def solo_una_vez(num_variables, clauses, assignment):            
   contar = [0]*len(assignment)
   
   for clause in clauses:
       for a in clause:
           contar[abs(a)]+1
   
   lista = []
   
   for k in range(0, len(contar)):
       if contar[k]==1:
           lista.append(k)
   
   if lista:
       for x in lista:
           if any(x in sublist for sublist in clauses):
               assignment[x] = 1
           else:
                   assignment[x] = 0
       nueva_clausula1 = actualizar_clausula(clauses, assignment) # hay que actualizar las clausula
       return True, nueva_clausula1 
   else:
        return False, clauses
        

def sat_preprocessing(num_variables, clauses, assignment):
    
    update = True
    while update:
        update = False   
        # TODO
        # usa funciones auxiliares       
       
        # buscamos aquellos literales que tengan solo un elemento
        update1, clausulas = elemento_solo(num_variables, clauses, assignment)
                    
        # buscamos aquellos lietrales que aparezcan solo una vez
        update2, clausulas = solo_una_vez(num_variables, clauses, assignment)
                
        update = update1 or update2
     
        if [] in clauses:
            return ([[1], [-1]], assignment) # caso de que salga tod bien se vacia
        else:
            if (clauses == []) or (not update): # si queda algo, no se encuentra una asignacion true
                     return (clauses, assignment)  # se devulve clausula reducida con su asignacion
                

    


def test():
    
    def correct_pre_processing(clauses, assig):
        for var in range(1, len(assig)):
            if assig[var] != None:
                for c in clauses:
                    if var in c or -var in c:
                        return False
        return True  
           
    
    ans = sat_preprocessing(1, [[1]], [None, None])
    
    assert ans == ([], [None, 1])
    
    if not correct_pre_processing(ans[0], ans[1]):
        print("Hay variables con un valor asignado que no han sido eliminadas de las clausulas")
    
    assert ([[1],[-1]]) == sat_preprocessing(1, [[1], [-1]], [None,None])[0]
    
    
    ans = sat_preprocessing(4, [[4], [-3, -1], [3, -4, 2, 1], [1, -3, 4], [-1, -3, -4, 2], [4, 3, 1, 2], [4, 3],[1, 3, -4], [3, -4, 1], [-1]], [None, None, None, None, None])
    
    assert ans[0] == []
    assert ans[1][1] == 0
    assert ans[1][4] == 1
    
    if not correct_pre_processing(ans[0], ans[1]):
        print("Hay variables con un valor asignado que no han sido eliminadas de las clausulas")
    
    
    ans = sat_preprocessing(5, [[4, -2], [-1, -2], [1], [-4],
                                [5, 1, 4, -2, 3], [-1, 2, 3, 5],
                                [-3, -1], [-4], [4, -1, 2]], 
                                [None, None, None, None, None, None])
    assert ans[0] == [[1],[-1]]            
    
    
    
    ans = sat_preprocessing(6, [[-5, 3, 2, 6, 1], [5, 6, 2, 4],
                                [3, 5, 2, -1, 4], [1], [2, 1, 4, 3, 6],
                                [-1, -5, 2, 3], [-3, 2, -5, 6, -4]], 
                                [None, None, None, None, None, None, None])
    assert ans[0] == [[5, 6, 2, 4], [3, 5, 2, 4], [-5, 2, 3], [-3, 2, -5, 6, -4]]
    assert ans[1][1] == 1
    
    if not correct_pre_processing(ans[0], ans[1]):
        print("Hay variables con un valor asignado que no han sido eliminadas de las clausulas")
    
    
    ans = sat_preprocessing(7, [[-5, 3, 2, 6, 1], [5, 6, 2, 4],
                                [3, 5, 2, -1, 4], [1], [2, 1, 4, 3, 6],
                                [-1, -5, 2, 3], [-3, 2, -5, 6, -4, 7]], 
                                [None, None, None, None, None, None, None, None] )
    assert ans[0] == []
    assert ans[1][1] == 1
    assert ans[1][4] == 1
    assert ans[1][6] == 1
    assert ans[1][7] == 1
    
   
    if not correct_pre_processing(ans[0], ans[1]):
        print("Hay variables con un valor asignado que no han sido eliminadas de las clausulas")
    
    ans = sat_preprocessing(6, [[-6, -4, 5, -1, ], [1,2,3,6,-5], [4,6], [-4, -3], [-1], [1,6,-5,-4], [3,5,-6,-5,-1]],
                                [None, None, None, None, None, None, None])
    
    assert ans[0] == []
    assert ans[1][1] == 0
    assert ans[1][2] == 1
    assert ans[1][3] == 0
    assert ans[1][5] == 0
    
    if not correct_pre_processing(ans[0], ans[1]):
        print("Hay variables con un valor asignado que no han sido eliminadas de las clausulas")
    
    
test()
