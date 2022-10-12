
def is_satisfied(num_variables, clauses, assignment):
     # Prendicion: len(assignment) = num_variables + 1
     
     # TODO: 
     # - Programar el codigo esta funcion
     # - Puedes definir funciones auxiliares si lo estimas oportuno

     for c in clauses:
         satisfied = 0
         i = 0
         while i < len(c) and not satisfied :
             x = c[i]
             if x < 0:
                 val = 1 - assignment[-x]
             else:
                 val = assignment[x]
             satisfied = val
             i += 1
         if not satisfied:
             return False
     return True
 
    ## El coste es de O(2n*m) en el caso peor, siendo n el número de variables y m el número de clausulas,
    ## ya que recorremos cada variable en cada clausula. Las clausulas pueden tener un máximo de 2n variables
    ## (las variables y sus negaciones).
     
   

def test():
    num_variables = 4
    clauses = [[1,2,-3],[2,-4],[-1,3,4]]
    assignment = [0,1,1,1,1]
    assert is_satisfied(num_variables, clauses, assignment)

    assignment = [0,1,0,1,1]
    assert not is_satisfied(num_variables, clauses, assignment)
    
    clauses = [[-3, -1], [2, -3, -4, -1], [-1, -4], [-3], [-1, -2], [-3, 4, -2], [-1, -4, 2]]
    assignment = [0,0,0,1,0]
    assert not is_satisfied(num_variables, clauses, assignment)
    
    num_variables = 5
    clauses = [[1, -5, 4], [-1, 5, 3, 4], [-3, -4]]
    assignment = [0,0,0,1,0,1]
    assert not is_satisfied(num_variables, clauses, assignment)
    
    clauses = [[-3, -1], [-1, -4, -2]]
    assignment = [0,0,0,0,0]
    assert  is_satisfied(num_variables, clauses, assignment)
    
    clauses = [[-15, -4, 14], [-7, -4, 13], [-2, 18, 11], [-12, -11, -6], [7, 17, 4], 
               [4, 6, 13], [-15, -9, -14], [14, -4, 8], [12, -5, -8], [6, -5, -2], 
               [8, -9, 10], [-15, -11, -12], [12, 16, 17], [17, -9, -12], [-12, -4, 11], 
               [-18, 17, -9], [-10, -12, -11], [-7, 15, 2], [2, 15, 17], [-15, -7, 10], 
               [1, -15, 11], [-13, -1, -6], [-7, -11, 2], [-5, 1, 15], [-14, -13, 18], 
               [14, 12, -1], [18, -16, 9], [5, -11, -13], [-6, 10, -16], [-2, 1, 4], 
               [-4, -11, 8], [-8, 18, 1], [-2, 15, -13], [-15, -12, -10], 
               [-18, -14, -6], [1, -17, 10], [10, -13, 2], [2, 17, -3], [14, 1, -17], 
               [-16, -2, -11], [16, 7, 15], [-10, -6, 16], [4, -5, 10], [8, 10, -12], 
               [1, -9, -14], [18, -9, 11], [16, 7, 12], [-5, -14, -13], [1, 18, 5], 
               [11, 16, 5], [-8, 12, -2], [-6, -2, -13], [18, 16, 7], [-3, 9, -13], 
               [-1, 3, 12], [-10, 7, 3], [-15, -6, -1], [-1, -7, -3], [1, 5, 13], 
               [7, 6, -9], [1, -4, 3], [6, 8, 1], [12, 14, -8], [12, 5, -13], 
               [-12, 15, 9], [-17, -8, 3], [17, -6, 8],[-3, -14, 4]]
    assignment = [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]
       
    assert not is_satisfied(20,clauses,assignment)
    
test()    

