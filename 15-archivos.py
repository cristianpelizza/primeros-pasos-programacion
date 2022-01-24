def app():
    #crear el archivo
    archivo=open('archivo.txt', 'w') #w es permiso de escritura y si no existe lo creará

    #generar numeros en archivo
    for i in range(0,20):
        archivo.write('esta es la linea'+str(i)+"\r\n")

app()
