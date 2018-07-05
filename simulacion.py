import mesas2
import candidatos
import random
import time

def voto(personas):
    for i in personas:
        for e in personas[i]:
            escoger()
            tiempo(e)

def escoger():
    llaves=[]
    for i in postulantes:
        key=i
        llaves.append(key)
    x=random.randint(0,len(llaves)-1)
    p=postulantes[llaves[x]][2]
    postulantes[llaves[x]][2]=p+1

def tiempo(e):
    if e>=18 and e<=35:
        t=0
        a.append(e)
    elif e>=36 and e<=55:
        t=0
        b.append(e)
    else:
        t=0
        c.append(e)
    time.sleep(t)

votantes=mesas2.mesas
postulantes=candidatos.candidatos

a=[]
b=[]
c=[]
pre=[]

for i in votantes:
    print(i,":",votantes[i])
    print(len(votantes[i]))


voto(votantes)

print(postulantes)

votosemitidos = len(a) + len(b) + len(c)
jovenes = (len(a) / votosemitidos) * 100
mediaedad = (len(b) / votosemitidos) * 100
avanzados = (len(c) / votosemitidos) * 100
preferenciales = (int(len(votantes['Mesa Preferencial'])) / votosemitidos) * 100

print("Porcentaje de votantes entre 18 y 35 años:",jovenes,"%")
print("Porcentaje de votantes entre 36 y 55 años:",mediaedad,"%")
print("Porcentaje de votantes mayores a 55 años:",avanzados,"%")
print("Porcentaje de votantes preferenciales:",preferenciales,"%")