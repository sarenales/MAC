#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 17:11:15 2022

@author: yo
"""

from pysat.solvers import Minisat22
from pysat.card import CardEnc

def prueba():
    clauses = [[1,2],[-1,-2]]
    with Minisat22(bootstrap_with=clauses) as sat: ## le llamamos sat 
        return sat.solve(), sat.get_model()
    
def prueba2():
    list_var = [i for i in range(1,3) ]
    constraint = CardEnc.atmost(list_var, 1)
    return constraint.clauses    
print(prueba())
print(prueba2())
