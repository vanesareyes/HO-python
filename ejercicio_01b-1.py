'''Ejercicio 1b)'''

fib=[]
for i,k in enumerate(range (1,32)):
    print( "i,k:",i,k)# k es el numero de la serie de fib y el i es el indice de la serie
    if k <= 2:
	    fib.append(i)
    if k>2:
        fib.append(fib[i-1]+fib[i-2])
		
print fib    
#r=max(fib)
#print r

fibimp=[]
for i in fib:
    if i %2 != 0:
        fibimp.append (i)
   # else: fibimp.append (0)

print fibimp

d=set(fibimp)
e=sum(d)
print e

