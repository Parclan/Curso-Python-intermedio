# Elecciones

import os 
os.system ("clear")

def functionA ():
    print ("Usted eligio a Jose")


def functionB ():
    print ("Usted eligio a Carlos")


def functionC ():
    print ("Usted eligio a Oscar")

print ("Las letras tienen que ser mayusculas")    
elegir = input("Elige A, B ,C: ")
    
if elegir == 'A':
    functionA()

elif elegir == 'B':
    functionB ()
    
elif elegir == 'C':
    functionC ()

else:
    print ("No dio una respuesta")
    
print("//////////////////////////////////////////////////////////////////////")

x = int(input("Digite un numero: "))

if x >= 0:
    print (f"{x} es un numero positivo")

elif 0 >= x:
    print (f"{x} es un numero negativo")

else:
    print("Please digit one number")