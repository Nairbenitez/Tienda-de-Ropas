from typing import List

# Clase base para productos
class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int, talla: str = ""):
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad
        self._talla = talla

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def precio(self) -> float:
        return self._precio

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @property
    def talla(self) -> str:
        return self._talla

    def mostrar_info(self) -> str:
        return f"{self._nombre:<20} | ₲{self._precio:>10,.0f} | Stock:{self._cantidad:>3} | Talla: {self._talla:<4}"

    def reducir_stock(self) -> None:
        if self._cantidad > 0:
            self._cantidad -= 1  # Reducir el stock en 1

# Clase para ropa de hombres
class RopaHombre(Producto):
    def __init__(self, nombre: str, precio: float, cantidad: int, talla: str):
        super().__init__(nombre, precio, cantidad, talla)
        self._genero = "Hombre"

    def mostrar_info(self) -> str:
        return f"{super().mostrar_info()} | {self._genero}"

# Clase para ropa de mujeres
class RopaMujer(Producto):
    def __init__(self, nombre: str, precio: float, cantidad: int, talla: str):
        super().__init__(nombre, precio, cantidad, talla)
        self._genero = "Mujer"  # Mover esta línea de indentación

    def mostrar_info(self) -> str:
        return f"{super().mostrar_info()} | {self._genero}"

# Clase para categorías de productos
class Categoria:
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._productos: List[Producto] = []

    @property
    def nombre(self) -> str:
        return self._nombre

    def agregar_producto(self, producto: Producto) -> None:
        self._productos.append(producto)

    def mostrar_productos(self) -> None:
        if self._productos:
            for producto in self._productos:
                print(producto.mostrar_info())

# Clase para el inventario
class Inventario:
    def __init__(self):
        self._categorias: List[Categoria] = []

    def agregar_categoria(self, categoria: Categoria) -> None:
        self._categorias.append(categoria)

    def mostrar_productos(self) -> None:
        print("\n=== TIENDA DE NAIR ===\n")
        for categoria in self._categorias:
            categoria.mostrar_productos()

    def procesar_compra(self, nombre_producto: str, genero: str) -> None:
        for categoria in self._categorias:
            for producto in categoria._productos:
                # Verificar si el producto coincide y si el género es correcto
                if (producto.nombre.lower() == nombre_producto.lower() and 
                    ((isinstance(producto, RopaHombre) and genero.lower() == "hombre") or 
                     (isinstance(producto, RopaMujer) and genero.lower() == "mujer"))):
                    
                    if producto.cantidad > 0:
                        producto.reducir_stock()
                        print("\n" + "=" * 70)
                        print("Compra realizada con éxito:")
                        print("-" * 70)
                        print(producto.mostrar_info())
                        print("=" * 70)
                        return  # Salir después de realizar la compra
                    else:
                        print("\nProducto fuera de stock.")
                        return
        print("\nProducto no encontrado.")

def main():
    # Crear inventario
    inventario = Inventario()
    
    # Crear categorías
    categoria_camisas = Categoria("CAMISAS")
    categoria_pantalones = Categoria("PANTALONES")
    categoria_calzado = Categoria("CALZADO")
    
    # Productos para hombres
    camisas_hombre = [
        RopaHombre("Camisa Roja", 95000, 10, "M"),
        RopaHombre("Camisa Casual negra", 70000, 15, "L"),
        RopaHombre("Camisa Deportiva gris", 90000, 20, "XL"),
    ]
    pantalones_hombre = [
        RopaHombre("Pantalón Jean", 95000, 12, "32"),
        RopaHombre("Pantalón Vestir", 120000, 8, "34"),
        RopaHombre("Pantalón Casual", 75000, 15, "36"),
    ]
    calzado_hombre = [
        RopaHombre("Zapatos Formales beige", 150000, 10, "42"),
        RopaHombre("Zapatillas naranjas", 180000, 15, "43"),
        RopaHombre("Sandalias verdelimon", 45000, 20, "41"),
    ]
    
    # Productos para mujeres
    camisas_mujer = [
        RopaMujer("Blusa Formal", 75000, 12, "S"),
        RopaMujer("Blusa Casual", 60000, 18, "M"),
        RopaMujer("Top Fashion", 50000, 25, "L"),
    ]
    pantalones_mujer = [
        RopaMujer("Pantalón Jean", 85000, 15, "28"),
        RopaMujer("Pantalón Vestir", 110000, 10, "30"),
        RopaMujer("Leggins", 65000, 20, "32"),
    ]
    calzado_mujer = [
        RopaMujer("Zapatos Tacón", 160000, 8, "37"),
        RopaMujer("Zapatillas", 170000, 12, "38"),
        RopaMujer("Sandalias", 55000, 18, "36"),
    ]
    
    # Agregar productos a categorías
    for producto in camisas_hombre + camisas_mujer:
        categoria_camisas.agregar_producto(producto)
    for producto in pantalones_hombre + pantalones_mujer:
        categoria_pantalones.agregar_producto(producto)
    for producto in calzado_hombre + calzado_mujer:
        categoria_calzado.agregar_producto(producto)
    
    # Agregar categorías al inventario
    inventario.agregar_categoria(categoria_camisas)
    inventario.agregar_categoria(categoria_pantalones)
    inventario.agregar_categoria(categoria_calzado)
    
    while True:
        inventario.mostrar_productos()
        print("\nOpciones:")
        print("=" * 70)
        print("1. Comprar producto")
        print("2. Salir")
        print("=" * 70)
        opcion = input("\nSeleccione una opción (1-2): ").strip()
        if opcion == "2":
            print("\n¡Gracias por su visita!")
            print("=" * 70)
            break
        elif opcion == "1":
            nombre = input("Ingrese el nombre del producto: ").strip()
            genero = input("Ingrese el género (Hombre/Mujer): ").strip()
            inventario.procesar_compra(nombre, genero)
            input("\nPresione Enter para continuar...")
        else:
            print("\nOpción no válida.")
            input("Presione Enter para continuar...")

# Ejecutar el programa
if __name__ == "__main__":
    main()