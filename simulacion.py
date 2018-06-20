import mesas2
import candidatos

edades=mesas2.edades
votantes=mesas2.hormiguero(edades)
postulantes=candidatos.candidatos

def escogervoto(votantes):
    counter=len(votantes)-1
    while counter>0:
        for i in votantes:
            key='Mesa n°'+str(counter)
            votan=votantes[key]
        print(votan)
        counter=counter-1
    keypref = 'Mesa Preferencial'
    votanpref = votantes[keypref]
    print(votanpref)

escogervoto(votantes)
print(votantes)
print(postulantes)