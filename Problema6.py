class Producto:
    def __init__(self, nombre, precio, anio_fabricacion):
        self.nombre = nombre        
        self.precio = precio        
        self.anio_fabricacion = anio_fabricacion  

    def mostrar_informacion(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Año: {self.anio_fabricacion}"

class Catalogo:
    def __init__(self):
        self.productos = []  
    
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el catálogo.")
        else:
            for producto in self.productos:  
                print(producto.mostrar_informacion())
    
    def filtrar_por_anio(self, anio):
        productos_filtrados = [producto for producto in self.productos if producto.anio_fabricacion == anio]
        if productos_filtrados:
            print(f"Productos del año {anio}:")
            for producto in productos_filtrados:
                print(producto.mostrar_informacion())
        else:
            print(f"No hay productos del año {anio}.")

    def filtrar_por_precio(self, precio_min, precio_max):
        productos_filtrados = [producto for producto in self.productos if precio_min <= producto.precio <= precio_max]
        if productos_filtrados:
            print(f"Productos con precio entre ${precio_min} y ${precio_max}:")
            for producto in productos_filtrados:
                print(producto.mostrar_informacion())
        else:
            print(f"No hay productos en el rango de precio ${precio_min} - ${precio_max}.")

catalogo_elementos = Catalogo()

producto1 = Producto("Camara fotografica", 1700, 2021)
producto2 = Producto("Teclado", 60, 2023)
producto3 = Producto("Mouse", 50, 2024)

catalogo_elementos.agregar_producto(producto1)
catalogo_elementos.agregar_producto(producto2)
catalogo_elementos.agregar_producto(producto3)

print("Lista de productos en el catálogo:")
catalogo_elementos.mostrar_productos()


print("\nFiltrar productos del año 2024:")
catalogo_elementos.filtrar_por_anio(2024)


print("\nFiltrar productos con precios entre 40 y 100:")
catalogo_elementos.filtrar_por_precio(40, 100)


