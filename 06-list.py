lenguajes=['python','kotlin','java','javascript']

print(lenguajes)

#los list comienzan en la posicion 0
print(lenguajes[0]) #python

#ordenar los elementos
lenguajes.sort()
print(lenguajes)

#acceder a un elemento dentro de un texto
aprendiendo=f'estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

#modificando valores de un arreglo(list)
lenguajes[2]='PNP'
print(lenguajes)

#agregar elementos a un arreglo (list)
lenguajes.append('ruby')
print(lenguajes)

#eliminar de un arreglo (list)
del lenguajes[1]
print(lenguajes)

#eliminar el ultimo elemento de un arreglo (list)
lenguajes.pop()
print(lenguajes)

#eliminar con pop una posicion en especifico
lenguajes.pop(0)
print(lenguajes)

#eliminar por nombre
lenguajes.remove('PNP')
print(lenguajes)

