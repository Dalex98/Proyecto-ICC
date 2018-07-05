import random
def edades(votantes):
    edades = []
    menores=round(votantes*0.9)
    viejitos=votantes-menores
    for i in range(menores):
        x = random.randint(18, 64)
        edades.append(x)
    for i in range(viejitos):
        x = random.randint(65, 90)
        edades.append(x)
    return edades
def hormiguero(lista):
    mesas = {'Mesa n°1':[],'Mesa n°2':[],'Mesa n°3':[],'Mesa n°4':[],'Mesa n°5':[],'Mesa n°6':[],'Mesa Preferencial':[]}
    counter=round(len(lista)*0.03)
    while counter>0:
        manco=random.randint(0,len(lista))
        key = 'Mesa Preferencial'
        mesas.setdefault(key, [])
        mesas[key].append(lista[manco])
        counter=counter-1
        del lista[manco]
    for i in lista:
        if i>=65:
            key = 'Mesa Preferencial'
            mesas.setdefault(key, [])
            mesas[key].append(i)
        else:
            x=random.randint(1,6)
            key='Mesa n°'+str(x)
            mesas.setdefault(key,[])
            mesas[key].append(i)
    return mesas
votantes=int(input("Numero de votantes:"))
mesas=hormiguero(edades(votantes))
#for i in mesas:
#   print(i,":",mesas[i])
#   print(len(mesas[i]))