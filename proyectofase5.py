# =========================================
# Nombre del estudiante: Yuliet Vanessa Jimenez Moreno
# Grupo: 213022_937
# Programa: Ingenieria Electronica
# Codigo fuente: Autoria propia
# =========================================

# MATRIZ DEL MENU
menu = [
    ["Hamburguesa", "Comida Rapida", 25000],
    ["Pizza", "Comida Rapida", 40000],
    ["Ensalada Cesar", "Saludable", 18000],
    ["Sushi", "Japonesa", 55000],
    ["Pasta Alfredo", "Italiana", 32000],
    ["Jugo Natural", "Bebida", 12000]
]


# =========================================
# FUNCION
# =========================================

def calcular_precio_final(categoria, precio_base,
                          categoria_objetivo,
                          umbral_precio):

    if categoria == categoria_objetivo and precio_base > umbral_precio:

        descuento = precio_base * 0.15
        precio_final = precio_base - descuento

    else:
        precio_final = precio_base

    return precio_final


# =========================================
# CICLO PRINCIPAL
# =========================================

continuar = "1"

while continuar == "1":

    # =====================================
    # TABLA DE BIENVENIDA
    # =====================================

    print("""
╔══════════════════════════════════════════════════════════════╗
║                  BIENVENIDOS AL PROGRAMA                     ║
╠══════════════════════════════════════════════════════════════╣
║               SISTEMA DE MENU Y PROMOCIONES                  ║
╚══════════════════════════════════════════════════════════════╝
    """)

    # =====================================
    # MOSTRAR CATEGORIAS
    # =====================================

    print("\nCategorias disponibles:")
    print("1. Comida Rapida")
    print("2. Saludable")
    print("3. Japonesa")
    print("4. Italiana")
    print("5. Bebida")


    # =====================================
    # ELEGIR CATEGORIA
    # =====================================

    while True:

        opcion = input(
            "\nSeleccione una categoria (1-5): "
        )

        if opcion == "1":
            categoria_objetivo = "Comida Rapida"
            break

        elif opcion == "2":
            categoria_objetivo = "Saludable"
            break

        elif opcion == "3":
            categoria_objetivo = "Japonesa"
            break

        elif opcion == "4":
            categoria_objetivo = "Italiana"
            break

        elif opcion == "5":
            categoria_objetivo = "Bebida"
            break

        else:
            print("Error: Opcion no valida, intente nuevamente")


    # =====================================
    # PEDIR PRECIO MINIMO
    # =====================================

    while True:

        try:
            umbral_precio = int(
                input("Ingrese el precio minimo: ")
            )

            if umbral_precio > 0:
                break

            else:
                print("El numero debe ser mayor que 0")

        except ValueError:
            print("Error: Debe ingresar un numero valido")


    # =====================================
    # TABLA FINAL
    # =====================================

    print("""
╔════════════════════════════════════════════════════════════════════════════════════╗
║                           RESULTADO FINAL                                         ║
╠════╦════════════════════╦════════════════════╦════════════════════╦═══════════════╣
║ No ║ Producto           ║ Precio Base        ║ Precio Final       ║ Promocion     ║
╠════╬════════════════════╬════════════════════╬════════════════════╬═══════════════╣
    """)

    for i in range(len(menu)):

        nombre = menu[i][0]
        categoria = menu[i][1]
        precio_base = menu[i][2]

        precio_final = calcular_precio_final(
            categoria,
            precio_base,
            categoria_objetivo,
            umbral_precio
        )

        if precio_final != precio_base:
            promocion = "15% OFF"
        else:
            promocion = "No aplica"

        print(
            f"║ {i+1:<2} "
            f"║ {nombre:18} "
            f"║ ${precio_base:<18} "
            f"║ ${precio_final:<18.0f} "
            f"║ {promocion:13}║"
        )

    print("╚════╩════════════════════╩════════════════════╩════════════════════╩═══════════════╝")


    # =====================================
    # PREGUNTAR SI DESEA CONTINUAR
    # =====================================

    while True:

        continuar = input(
            "\nDesea realizar otra consulta?\n"
            "1. Si\n"
            "2. No\n"
            "Seleccione una opcion: "
        )

        if continuar == "1" or continuar == "2":
            break

        else:
            print("Error: Debe ingresar 1 o 2")


# =========================================
# TABLA DE DESPEDIDA
# =========================================

print("""
╔══════════════════════════════════════════════════════════════╗
║                    FIN DEL PROGRAMA                          ║
╠══════════════════════════════════════════════════════════════╣
║                   MUCHAS GRACIAS                             ║
║                   HASTA PRONTO                               ║
╚══════════════════════════════════════════════════════════════╝
""")
