candidatos={}

Numcandidatos=int(input("Numero de candidatos:"))

for i in range(Numcandidatos):
    info = []
    nombre = (input("Nombre del Postulante:"))
    par = (input("Partido del Postulante:"))
    muni = (input("Municipio del Postulante:"))
    info.append(par)
    info.append(muni)
    candidatos.update({nombre:info})

print(candidatos)
