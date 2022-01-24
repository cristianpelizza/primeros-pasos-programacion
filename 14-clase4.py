class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre=nombre #atributo
        self.categoria=categoria
        self.precio=precio
    
    def mostrar_informacion(self):
        print(f'Nombre:{self.nombre}, Categoria:{self.categoria}, Precio: {self.precio}')

    #getters y setters - get:obtiene un valor y set:agrega o modifica un valor
    def get_precio(self):
        return self.__precio
    
    def set_precio(self,precio):
        self.__precio=precio

#instanciar la clase
restaurant=Restaurant('pizzeria mexico', 'comida italiana', 50)
#restaurant.__precio=80 #no sera posible modificarlo con private __
restaurant.mostrar_informacion()
restaurant.set_precio(80)
precio=restaurant.get_precio()
print(precio)


restaurant2=Restaurant('hamburguesas Python', 'comida casual', 20)
restaurant2.mostrar_informacion()
restaurant2.set_precio(40)
restaurant2.get_precio()


