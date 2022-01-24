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


#crear una clase hijo de restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio)

hotel=Hotel('hotel POO', '5 estrellas', 200)
hotel.mostrar_informacion()
