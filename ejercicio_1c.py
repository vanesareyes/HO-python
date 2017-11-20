#Factorizar n
import math 
n = 600851475143
#def factorizar(n):
    #almaceno resultados de la factorizacion en una lista
l = []
num1 = n

print num1
#mientras sea par el 2 es un factor
while num1 % 2 == 0:
    l.append(2)
    num1 /= 2
#ahora impares empezando por el 3
cuenta = 3
raiz = int(math.sqrt(num1))
while cuenta <= raiz and num1 > 1:
    if num1 % cuenta == 0:
        l.append(cuenta)
        num1 /= cuenta
    else:
        cuenta += 2
if num1 > 1:
    l.append(num1)
#return l

print l

res=max(l)
print res

