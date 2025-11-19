suma_stock = []
catalogo = {
    'BK001': ['El Quijote', 'Miguel de Cervantes', 'físico', 1200, 'Editorial Planeta', 'español'],
    'BK002': ['1984', 'George Orwell', 'digital', 328, 'Penguin', 'inglés'],
    'BK003': ['Rayuela', 'Julio Cortázar', 'físico', 600, 'Sudamericana', 'español'],
    'BK004': ['Sapiens', 'Yuval Noah Harari', 'digital', 450, 'Debate', 'inglés'],
    }

inventario = {
    'BK001': [15990, 3],
    'BK002': [8990, 0],
    'BK003': [18990, 7],
    'BK004': [12500, 5],
    }

def stock_editorial(editorial):
    
    for catalogo[0] in catalogo[5] == editorial:
        suma_stock = suma_stock + 1
        print(suma_stock)
    else:
        print("Esa editorial no esta regitrada.")

def buscar_por_precio(p_min, p_max):

    if inventario[0] in inventario[0] >= p_min and p_max:
        print(catalogo[0] in catalogo[0])
        print(catalogo[0])
    else:
        print("No hay libros disponibles en ese rango de precios.")

def actualizar_precio(codigo, nuevo_precio):
    codigo = input("Ingrese código del libro: ")

    if codigo == inventario[0]:
        precio = inventario[0] in inventario[0]
        precio == nuevo_precio 
        print("Precio actualizado!!")
    else:
        print("El libro no existe!!")

        while True:
            act = input("¿Desea actualizar otro precio? (s-n): ").lower()
            if act == 's':
                continue
            elif act == 'n':
                break

