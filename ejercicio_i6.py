import os
os.system("cls")

import math


#imprime numeros de logaritmo
"""def imprimeLogaritmo(x):
    if x >= 0:
        print(math.log(x))
    else:
        print("Solo numeros positivos")
    return
imprimeLogaritmo(10)"""



#imprime un conteo exacto
"""def cuenta_atras(n):
    if n == 0:
        print("Despegando")
        
    else:
        print ("Fallido")
cuenta_atras(1-2)"""

#imprime oraciones en cantidad
def nLinea (n):
    if n > 0:
        print("hola")
        nLinea(n - 1)
nLinea(100)
    
