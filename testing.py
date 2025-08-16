class Producto:
    def __init__(self, nombre, precio, descuento=0):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento

    def precio_final(self):
        return self.precio * (1 - self.descuento / 100)

    def mostrar_info(self):
        print(f"\n📦 Producto: {self.nombre}")
        print(f"  Precio original: ${self.precio:,.2f}")
        print(f"  Descuento: {self.descuento}%")
        print(f"  Precio final con descuento: ${self.precio_final():,.2f}")
        print("-" * 40)


class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_producto(self, nombre_producto):
        for producto in self.productos:
            if producto.nombre.lower() == nombre_producto.lower():
                return producto
        return None

    def mostrar_productos(self):
        print("\n📋 Lista de productos:")
        for producto in self.productos:
            print(f"- {producto.nombre}")


def mostrar_menu():
    print("\n🔹 Menú:")
    print("1. Ver lista de productos")
    print("2. Buscar precio de un producto")
    print("3. Salir")


def main():
    tienda = Tienda("Mi Chuzo")

    
    tienda.agregar_producto(Producto("Camisa", 100000, 10))
    tienda.agregar_producto(Producto("Pantalon", 180000, 20))
    tienda.agregar_producto(Producto("Zapatos", 550000, 15))
    tienda.agregar_producto(Producto("Sombrero", 220000, 0))

    print(f"🛒 Bienvenido a {tienda.nombre}")

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            tienda.mostrar_productos()

        elif opcion == '2':
            nombre = input("🔍 Ingresa el nombre del producto: ")
            producto = tienda.buscar_producto(nombre)
            if producto:
                producto.mostrar_info()
            else:
                print("❌ Producto no encontrado.")

        elif opcion == '3':
            print("👋 Gracias por visitar la tienda. ¡Hasta luego!")
            break

        else:
            print("⚠️ Opción inválida. Intenta de nuevo.")



if __name__ == "__main__":
    main()
