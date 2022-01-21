nombre = input('cual es tu nombre: \r\n')

print (f'hola {nombre}')

#leer datos que seran numeros
edad=input ('cual es su edad? \r\n')
edad=int(edad)
if edad >=18:
    print('ya puedes votar')
else:
    print('aun no puedes votar')

#mezclarlo con operadores
numero=input('agrega un numero y te dire si es par o impar \r\n')
numero=int(numero)

if numero %2==0:
    print (f' el numero {numero} es par')
else:
    print(f'el numero {numero} es impar')
