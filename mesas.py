import random
def generador_edad_votantes (mesas):
    votantes={}
    lis=list(mesas.values())
    m=0
    for i in lis:
        edades=[]
        m=m+1
        for j in range (i):
            x=random.randint(18,90)
            edades.append(x)
        votantes.update({'Mesa n°'+str(m):edades})
    return votantes
MESAS={}
n=int(input("Ingrese el numero de mesas disponibles:"))
for i in range(n):
    nv=int(input("Numero de votantes mesa n°"+str(i+1)+":"))
    MESAS.update({'Mesa n°'+str(i+1):nv})
edades= generador_edad_votantes(MESAS)
print("Mesas y cantidad de votantes:",MESAS)
print("Mesas y la edad de votantes:",edades)
