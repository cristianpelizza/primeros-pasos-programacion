class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre=nombre #atributo
        self.categoria=categoria
        self.__precio #default: Public, Protected, Private
    
    def mostrar_informacion(self):
        print(f'Nombre:{self.nombre}, Categoria:{self.categoria}, Precio: {self.__precio}')

#instanciar la clase
restaurant=Restaurant('pizzeria mexico', 'comida italiana', 50)


restaurant.__precio=80
restaurant.mostrar_informacion()

restaurant2=Restaurant('hamburguesas Python', 'comida casual', 20)

restaurant2.__precio=40
restaurant2.mostrar_informacion()


