#creando un diccionario simple
from operator import methodcaller


cancion={
    'artista' : 'metallica', #llave y valor
    'cancion' : 'enter sandman',
    'lanzamiento' : 1992,
    'likes' : 3000
}
#acceder a los elementos del diccionario
print(cancion['artista'])
print(cancion['lanzamiento'])

#mezclar con string
artista=cancion['artista']
print(f'estoy escuchando a {artista}')

print(cancion)

#agregar nuevos valores
cancion['playlist']= 'heavy metal'
print(cancion)

#reemplazar valor existente
cancion['cancion']= 'drugs'
print(cancion)

#eliminar un valor
del cancion['lanzamiento']
print(cancion)