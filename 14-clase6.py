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
        self.precio=precio


#crear una clase hijo de restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, alberca):
        super().__init__(nombre, categoria, precio)
        self.alberca=alberca

    #reescribir un metodo (debe llamarse igual)
    def mostrar_informacion(self):
        print(f'Nombre:{self.nombre}, Categoria:{self.categoria}, Precio: {self.precio}, Alberca:{self.alberca}')
    

    #agregar un metodo que solo exista en hotel
    def get_alberca(self):
        return self.alberca

hotel=Hotel('hotel POO', '5 estrellas', 200, 'alberca_si')
hotel.mostrar_informacion()
alberca=hotel.get_alberca()
print(alberca)
