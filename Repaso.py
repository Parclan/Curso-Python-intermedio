import os 
os.system ("cls")

def functionA ():
    print("Usted es hincha del junior")
    
def functionB ():
    print("Usted es hincha del Fc Barcelona")
    
def functionC ():
    print("Usted es hincha del Real Madrid")
    

eleccion = input("Elige A, B, C: ")

if eleccion == 'A':
    functionA()
    
elif eleccion == 'B':
    functionB()
    
elif eleccion == 'C':
    functionC()

else:
    print("Usted no eligio ninguna letra")