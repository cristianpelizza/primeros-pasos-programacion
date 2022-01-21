#operadores and y or
usuario_logueado=True
usuario_admin=False

if usuario_logueado or usuario_admin:
    print('administrador')
elif usuario_logueado:
    print('acceso al sistema')
else:
    print('debes iniciar sesion')