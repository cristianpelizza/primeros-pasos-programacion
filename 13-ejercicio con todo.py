playlist={} #diccionario vacio
playlist ['canciones'] = [] #lista vacia de canciones

#funcion principal
def app():
    #agregar playlist
    agregar_playlist=True
    while agregar_playlist:
        nombre_playlist=input ('como deseas nombrar la playlist?\r\n')
        if nombre_playlist:
            playlist['nombre']=nombre_playlist
        
            #ya tenemos un nombre descativar el True
            agregar_playlist=False
            #mandar llamar la funcion para agregar canciones
            agregar_canciones()

def agregar_canciones():
    #bandera para agregar canciones
    agregar_cancion=True
    
    while agregar_cancion:
        #preguntar al usuario que cancion desean agregar
        nombre_playlist=playlist['nombre']
        pregunta=f'\r\nagrega canciones para la playlist{nombre_playlist}:\r\n'
        pregunta+='escribe "X" para dejar de agregar canciones\r\n'

        cancion=input(pregunta)
        
        if cancion=="X":
            #dejar de agregar canciones
            agregar_cancion=False

            #mostrar resumen de la playlist
            mostrar_resumen()
        else:
            #agregar las canciones a la playlist
            playlist['canciones'].append(cancion)

def mostrar_resumen():
    nombre_playlist=playlist['nombre']
    print(f'playlist:{nombre_playlist}\r\n')
    print('canciones:\r\n')
    for cancion in playlist['canciones']:
        print(cancion)
    

        

            
        
        
    
app()
