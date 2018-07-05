candidatos={}
postulantes=int(input("Numero de candidatos:"))
for i in range(postulantes):
    info = []
    nombre = (input("Nombre del Postulante:"))
    par = (input("Partido del Postulante:"))
    muni = (input("Municipio del Postulante:"))
    puntos=0
    info.append(par)
    info.append(muni)
    info.append(puntos)
    candidatos.update({nombre:info})
candidatos
#print(candidatos)