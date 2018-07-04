import mesas2
import candidatos
import random
import time

edades=mesas2.edades
votantes=mesas2.hormiguero(edades)
postulantes=candidatos.candidatos

#def escogervoto(votantes):
#    counter=len(votantes)-1
#    while counter>0:
#        for i in votantes:
#            key='Mesa n°'+str(counter)
#            votan=votantes[key]
#        print(voto(votan,postulantes))
#        counter=counter-1
#    keypref = 'Mesa Preferencial'
#    votanpref = votantes[keypref]
#    print(votanpref)

#def voto(votan, postulantes):
#    votos=[]
    #for i in votan:
       # votos.append(random.randint(1,len(postulantes)))
   # return conteovotos(votos,postulantes)

#def conteovotos(votos,postulantes):
    #for i in votos:
       # voto=postulantes[i+1]
        #registrovotos(voto,postulantes)

#def registrovotos(voto,postulantes):
    #for i in range(len(postulantes)):
        #lista.append(postulantes[0])
        #lista.append(voto)

def voto(votantes):
    for i in votantes:
        key=i
        for e in votantes[i]:
            escoger()
            tiempo(e)
    for e in votantes['Mesa Preferencial']:
        escoger()
        tiempo(e)

def escoger():
    llaves=[]
    for i in postulantes:
        key=i
        llaves.append(key)
    p=0
    x=random.randint(0,len(llaves)-1)
    p=postulantes[llaves[x]][2]
    postulantes[llaves[x]][2]=p+1

def tiempo(e):
    if e>=18 and e<=35:
        t=0
    elif e>=36 and e<=55:
        t=0
    else:
        t=0
    time.sleep(t)

for i in votantes:
    key=i
    print(i,":",votantes[i])

voto(votantes)
print(postulantes)