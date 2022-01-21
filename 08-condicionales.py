#revisar si una condicion es mayor a 
from platform import python_branch


balance=0
if balance>0:
    print('puedes pagar')
else:
    print('no tiene saldo')

likes=200
if likes==200:
    print('excelente')

#if con texto
lenguaje='python'
if lenguaje!='python':
    print ('excelente decision')

    #evaluar boolean
usuario_autenticado=True
if usuario_autenticado:
    print('acceso al sistema')
else:
    print('debes iniciar sesion')

#evaluar un elemento de una lista
lenguajes=['python', 'Kotlin', 'java','javascrpt', 'PHP']
if 'PHP' in lenguajes:
    print('si existe')
else:
    print('no esta en la lista')


#if anidados
usuario_autenticado=True
usuario_admin=False

if usuario_autenticado:
    if usuario_admin:
        print('acceso total')
    else:
        print('acceso al sistema')
else:
    print('debes iniciar sesion')