import mesas2
import candidatos
import random

def voto(personas):
    duracion=0
    for i in personas['Mesa Preferencial']:
        escoger()
    for i in personas:
        print("Esta mesa voto",i)
        for e in personas[i]:
            escoger()
            t=tiempo(e)
            duracion=duracion+t
        if duracion>=80:
            return True
    return True

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
        t=2
        a.append(e)
    elif e>=36 and e<=55:
        t=4
        b.append(e)
    else:
        t=6
        c.append(e)
    return t

def estadistcas():
    votosemitidos = len(a) + len(b) + len(c) + len(votantes['Mesa Preferencial'])
    jovenes = (len(a) / votosemitidos) * 100
    mediaedad = (len(b) / votosemitidos) * 100
    avanzados = (len(c) / votosemitidos) * 100
    preferenciales = (int(len(votantes['Mesa Preferencial'])) / votosemitidos) * 100
    print(postulantes)
    print("Porcentaje de votantes entre 18 y 35 años:", jovenes, "%")
    print("Porcentaje de votantes entre 36 y 55 años:", mediaedad, "%")
    print("Porcentaje de votantes mayores a 55 años:", avanzados, "%")
    print("Porcentaje de votantes preferenciales:", preferenciales, "%")

votantes=mesas2.mesas
postulantes=candidatos.candidatos

a=[]
b=[]
c=[]
pre=[]

for i in votantes:
    print(i,":",votantes[i])
    print(len(votantes[i]))


duracion=voto(votantes)

if duracion==True:
    estadistcas()


print(duracion)