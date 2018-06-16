import random
def edades(n):
    edades = []
    for i in range(n):
        x = random.randint(18, 90)
        edades.append(x)
    return edades

def hormiguero(lista):
    mesas = {'Mesa n°1':[],'Mesa n°2':[],'Mesa n°3':[],'Mesa n°4':[],'Mesa n°5':[],'Mesa n°6':[],'Mesa Preferencial':[]}
    counter=len(lista)//8
    while counter>0:
        manco=random.randint(0,len(lista))
        key = 'Mesa Preferencial'
        mesas.setdefault(key, [])
        mesas[key].append(lista[manco])
        counter=counter-1
        del lista[manco]

    for i in lista:
        x=random.randint(1,6)
        key='Mesa n°'+str(x)
        mesas.setdefault(key,[ ])
        mesas[key].append(i)
    return mesas

votantes=int(input("Numero de votantes:"))

edades=edades(votantes)

print(hormiguero(edades))