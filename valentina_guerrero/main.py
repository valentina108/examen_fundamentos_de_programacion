import funciones as fn

while True:
    print("MENÚ PRINCIPAL")
    print("1. Stock por editorial.")
    print("2. Buscar libros por precio.")
    print("3. Actualizar precio de libro.")
    print("4. Salir.")

    try:
        opc = int(input("Ingrese una opción (1-4): "))
    except ValueError:
        print("Debe ingresar una opción valida.")
        
    if opc == 1:
        editorial = input("Ingrese el nombre de la editorial: ").lower()
        fn.stock_editorial(editorial)
    elif opc == 2:
        try:
            p_min = int(input("Ingrese precio mínimo: "))
        except ValueError:
            print("Ingrese un numero entero.")

        p_max = int(input("Ingrese precio máximo: "))
        fn.buscar_por_precio(p_min,p_max)
    elif opc == 3:
        fn.actualizar_precio(codigo,nuevo_precio)
        codigo = input("Ingrese código del libro: ")
        nuevo_precio = int(input("Ingrese nuevo precio: "))
        
    elif opc == 4:
        print("Programa finalizado.")
        break
    else:
        print("Debe seleccionar una opción válida!!")