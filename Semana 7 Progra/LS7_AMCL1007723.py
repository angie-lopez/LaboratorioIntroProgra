

CODIGO = True

while CODIGO: 
    print("Ejercicio 1: Operaciones Aritméticas")
    a = int(input("Ingrese el primer número: "))
    c = int(input("Ingrese el segundo número: "))

    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Módulo")
    print("6. Exponenciación")
    print("7. Cociente")
    print("8. Salir")

    opcion = input("Elija una opción (1-8): ")

    if opcion == '1':
        resultado = a + c
        print(a, "+", c,  "=", resultado)
    elif opcion == '2':
        resultado = a - c
        print(a, "-", yc,  "=", resultado)
    elif opcion == '3':
        resultado = a * c
        print(x, "*", y,  "=", resultado)
    elif opcion == '4':
        if y == 0:
            print("No se puede dividir por cero.")
        else:
            resultado = a / c
            print(a, "/", c,  "=", resultado)
    elif opcion == '5':
        resultado = xa % c
        print(a, "%", c,  "=", resultado)
    elif opcion == '6':
        resultado = a ** c
        print(a, "**", c,  "=", resultado)
    elif opcion == '7':
        resultado = a // c
        print(a, "//", c,  "=", resultado)
    elif opcion == '8':
        print("¡Hasta luego!")
        CODIGO = False 
    else:
        print("Opción no válida. Por favor, elija una opción válida (1-8).")
