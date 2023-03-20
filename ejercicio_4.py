# Condicionales y recursividad

import os 
os.system ("clear")

cociente = 8 / 4
residuo = 8 % 4

print (cociente)
print (residuo)

print("/////////////////////////////////////////////////")

#Expresiones Booleanas

"""Una expresión booleana es una expresión que es cierta o falsa. En Python,
una expresión que es cierta tiene el valor 1, y una expresión que es falsa tiene
el valor 0."""

a = 5 == 5
print (a)
b = 5 == 6
print (b)

"""Aunque probablemente estas operaciones le resulten familiares, los simbolos en
Python son diferentes de los matemáticos. Un error habitual es utilizar un signo
igual sencillo (=) en lugar del doble (==). Recuerde que = es un operador de
asignación y == es un operador de comparación. Además, no existen =< ni =>."""

x = 5
print (x and 1)
y = 0 
print (y and 1)

def imprimeN (x):
    if x %2 == 0:
        print (f"{x} es par")
    
    else:
        print (f"{x} es impar")
imprimeN(17)
imprimeN(x + 1) 
 
print("/////////////////////////////////////////////////")

J = int(input("numero: "))
M = int(input("numero: "))

if J == M:
    print ("Son iguales")
else:
    print ("Son distintos")


def funcionA():
    print("Has elegido la opción A")

def funcionB():
    print("Has elegido la opción B")

def funcionC():
    print("Has elegido la opción C")

eleccion = input("Elige una opción (A, B o C): ")

if eleccion == 'A':
    funcionA()
elif eleccion == 'B':
    funcionB()
elif eleccion == 'C':
    funcionC()
else:
    print("Elección no válida.")
    


     


