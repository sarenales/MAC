#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Tue Sep 13 12:12:55 2022

@author: 1002494-Silvia Arenales
"""

from numpy import log as ln
import math
import random

# ejercicio 1
# Calcular el valor absoluto de un numero negativo dado como entrada

numnegativo = int(input("Escribe un numero negativo: "))
print(f"El valor absoluto del numero es {abs(numnegativo)}")

# ejercicio 2
#  Suma dos números enteros (los dos números se proporcionan como entrada).

num1 = int(input("Escribe el primer numero: "))
num2 = int(input("Escribe el segundo numero: "))
print(f"La suma de los numeros es {(num1+num2)}")

# ejercicio 3
# Convierte la temperatura de grados Celsius (tCelsius como valor de entrada) a grados Fahrenheit:
    
gradosC = int(input("Escribe la temperatura en gradfos Celsius "))
print(f"La suma de los numeros es {(9/5)*gradosC+32}")

# ejercicio 4
# Calcula el área de una esfera (radio como entrada)

radio = int(input("Escribe el radio "))
print(f"La suma de los numeros es {4*math.pi*(radio^2)}")

# ejercicio 5
# Dados 3 números guardados en las variables a, b y c (de forma que a y b 
# tengan el mismo número y c sea mayor), programa las instrucciones assert que
# verifiquen que:
#    a y b son iguales
#    b es menor que c
#    c es mayor que a

a = int(input("Escribe el primer numero: "))
b = int(input("Escribe el segundo numero: "))
c = int(input("Escribe el tercer numero: "))

assert(a==b)
print("a=b")
assert(b<c)
print("b<c")
assert(c>a)
print("c>a")

print("Se verifican las tres")

# ejercicio 6
# Calcula la distancia euclı́dea entre dos puntos. Las coordenadas de cada punto
# se dan como entrada. 
print("Escribe el primer punto: ")
x1 = int(input("Escribe la coordenada x1: "))
y1 = int(input("Escribe la coordenada y1: "))
print("Escribe el segundo punto: ")
x2 = int(input("Escribe la coordenada x2: "))
y2 = int(input("Escribe la coordenada y2: "))

print(f"La distancia euclidea es {math.sqrt(((x2-x1)^2)+(y2-y1)^2)}")

# ejercicio 7

x = int(input("Escribe x : "))
y = int(input("Escribe y : "))

print(f"res = {5*(x^3)+math.sqrt((x^2)+(y^2))+(math.e)^(ln(x))}")


# ejercicio 8
lista = [1,2,3,4,5]
# Es una lista numerica, también podemos considerarlo como un array ya que son elementos del mismo tipo.

# ejercicio 9
# Inicializa una lista en Python en la que haya al menos 3 apariciones del numero
# 4. Sustituir todas las apariciones del numero 4 por 10.

lista2 = [1,3,4,5,3,4,3,10,2,4,5]

for index, value in enumerate(lista2):
    if value == 4:
        lista2[index] = 10
 
print(lista2)

# ejercicio 10
# La conjetura de Collatz.
# Imprime en la pantalla el numero de iteraciones necesario para reducir a 1 todos los numeros de una lista de numeros dada.

def collatz(n):
    i=0
    while n>1:
        if n%2 == 0:
            n =n/2
        else: 
            n = (n*3)+1
        i+=1
    return i
            

a = int(input("Escribe x : "))    
collatz(a)

# ejercicio 11
# Inicializa una matriz (lista de listas) de 6 × 3 con valores comprendidos entre -5 y 5.

matriz = [[random.randint(-5,5) for j in range(3)]for i in range(6)]
print(matriz)


# ejercicio 12
# Crea un metodo en Python que, dada una matriz cualquiera y un numero x,devuelva el numero de veces que x aparece en dicha matriz.

def contarNum(n, lista):
    return lista.count(n)

n1 = int(input("Escribe numero : "))
print("Escribe una lista de numeros (separar con un espacio) : ")
lista1 = list(map(int, input().split()))
contarNum(n1, lista1)

# ejercicio 13
# Crea un metodo en Python que devuelva si hay algun numero entre 4 y 7 en una matriz (lista de listas) de numeros

def numeroEntreCuatroSiete(lista):
    for i in range(len(lista)):
        for j in range (len(lista[i])):
            if lista[i][j] < 7 and lista[i][j]>4:
                print("True")
            else:   
                print("False")    
                
print("Escribe una matriz (la primera linea de enetrada es el num de filas de la matriz, separar con un espacio) : ")

n = int(input()) 
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])

numeroEntreCuatroSiete(a)

# Ejercicio 14
# Dadas una lista de numeros enteros, que siempre son positivos o negativos, y una lista de booleanos (True, False) con 
# el mismo tamano, crea una funcion que devuelva el numero de veces que un numero positivo es True y uno negativo
# es False en su correspondiente posicion.

def TF(list1,list2):
    a=0
    b=0
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]>0 and list2[j]==True:
                a+=1
            elif list1[i]<0 and list2[j]==False:
                b+=1
    return a,b
                

listaN = [-2, 3, 4, -7, 10, -234]
listaTF =  [True, True, True, True, False, False]

print(TF(listaN,listaTF))


