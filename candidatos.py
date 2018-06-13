candidatos=[]
partidos=[]
municipios=[]
n=int(input())

for i in range(n):
    nombre = (input("Nombre del Postulante:"))
    par = (input("Partido del Postulante:"))
    muni = (input("Municipio del Postulante:"))

    candidatos.append(nombre)
    partidos.append(par)
    municipios.append(muni)

print(candidatos)
print(partidos)
print(municipios)
