#iniciar un diccionario vacio
from re import A


jugador={}
print(jugador)

#se une un jugador
jugador['nombre']='juan'
jugador['puntaje']=0
print(jugador)

#incrementando el puntaje
jugador['puntaje']=100
print(jugador)

jugador['puntaje']=200
print(jugador)

#acceder a un valor
print(jugador.get('consola', 'no existe ese valor'))

#iterar en el diccionario
for llave,valor in jugador.items():
    print(llave)
    print(valor)

#eliminar jugador y puntaje
del jugador['nombre']
del jugador['puntaje']
print(jugador)
