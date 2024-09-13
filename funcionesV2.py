print("funciones version 2")
print("frida apodaca")
# zona de listas tuplas conjuntos y diccionario 
celulares=["samsung a52","iphone 12","china"]

# este es una tupla
cancionWTE=("seasson","bonfire","annie.","peach eyes")
print(cancionWTE)

# este es un conjunto
straykids={"lee know","han","suengmin","bangchan","felix","hyunjin","I.N","changbin"}
print(straykids)
print("lista de los integrantes de stray kids")
print(straykids)
    
# este es un diccionario
deporte={"volleyball","soccer","box"}
thisadict = {
    "volleyball": "cancha con red",
    "soccer": "cancha con porteria",
    "box": "ring"
}

# zona de funciones
def verlista(telefonos):
    for uncelular in telefonos:
        print(uncelular)

def vertuplas(canciones):
    for wte in canciones:
        print(wte)
            
def verset(grupoSKZ):
    for grupo in grupoSKZ:
        print(grupo)
                    
def verdiccionario(deportes):
    for undeporte in deportes:
        print(undeporte)

#llamadas a funciones
print("imprime celulares de una lista")
verlista(celulares)

print("imprime las canciones de wave to earth en una lista")
vertuplas(cancionWTE)

print("los integrantes de stray kids son")
verset(straykids)

print("donde se practican estos deportes")
verdiccionario(deporte)