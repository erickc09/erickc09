  
from ..efficiency.functionTime import count_elapsed_time

@count_elapsed_time
def lineabusqueda(list, target):
    for i in range(0, len(list)):
        if target == list[i]:
            return i
    return None

@count_elapsed_time
def busquedabin(arreglo, x):
    bajabus = 0
    subebus = len(arreglo)-1
    index = -1

    while bajabus < subebus:
        puntointermedio = int((bajabus+subebus)/2)
        if x==arreglo[puntointermedio]:
            index = puntointermedio
            break
        else:
            if x < arreglo[puntointermedio]:
                subebus = puntointermedio-1
            else:
                bajabus = puntointermedio+1
    if bajabus == subebus and arreglo[bajabus]==x:
        index = bajabus
    return index

def recursividadbinaria(arreglo, x, lB, uB):
    puntointermedio = int((lB+uB)/2)

    if lB == uB:
        if x==arreglo[puntointermedio]:
            return puntointermedio
        else:
            return -1
    else:
        if x==arreglo[puntointermedio]:
            return puntointermedio
        else:
            if x < arreglo[puntointermedio]:
                return recursividadbinaria(arreglo, x , lB, puntointermedio)
            else:
                return recursividadbinaria(arreglo, x, puntointermedio+1, uB)

def buscarinterpolo(arreglo, x):
    apoyo = ((len(arreglo)-1)/(arreglo[len(arreglo)-1]-arreglo[0])*x)-arreglo[0]
    if x > arreglo[len(arreglo)-1] :
        return -1
    elif len(arreglo) == 1 and arreglo[0] != x :
        return -1
    elif x > arreglo[int(apoyo)] :
        buscarinterpolo(arreglo[int(apoyo):],x)
    elif x < arreglo[int(apoyo)] :
        buscarinterpolo(arreglo[:int(apoyo)],x)
    else :
        return int(apoyo)