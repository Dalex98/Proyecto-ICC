import mesas2
import candidatos
import random

edades=mesas2.edades
votantes=mesas2.hormiguero(edades)
postulantes=candidatos.candidatos


def escogervoto(votantes):
    counter=len(votantes)-1
    while counter>0:
        for i in votantes:
            key='Mesa n°'+str(counter)
            votan=votantes[key]
        print(conteovoto(votan,postulantes))
        counter=counter-1
    keypref = 'Mesa Preferencial'
    votanpref = votantes[keypref]
    print(votanpref)

def conteovoto(votan, postulantes):
    votos=[]
    for i in votan:
        votos.append(random.randint(1,len(postulantes)))
    return votos
escogervoto(votantes)
print(votantes)
print(postulantes)