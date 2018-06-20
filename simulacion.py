import mesas2
import candidatos
import random
lista=[]
edades=mesas2.edades
votantes=mesas2.hormiguero(edades)
postulantes=candidatos.candidatos

print(votantes)
print(postulantes)

def escogervoto(votantes):
    counter=len(votantes)-1
    while counter>0:
        for i in votantes:
            key='Mesa n°'+str(counter)
            votan=votantes[key]
        print(voto(votan,postulantes))
        counter=counter-1
    keypref = 'Mesa Preferencial'
    votanpref = votantes[keypref]
    print(votanpref)

def voto(votan, postulantes):
    votos=[]
    for i in votan:
        votos.append(random.randint(1,len(postulantes)))
    return conteovotos(votos,postulantes)

def conteovotos(votos,postulantes):
    for i in votos:
        voto=postulantes[i+1]
        registrovotos(voto,postulantes)

def registrovotos(voto,postulantes):
    for i in range(len(postulantes)):
        lista.append(postulantes[0])
        lista.append(voto)


escogervoto(votantes)
print(votantes)
print(postulantes)
print(lista)