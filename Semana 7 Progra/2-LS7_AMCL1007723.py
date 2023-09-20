CODIGO = True
while CODIGO: 
    print("Ejercicio 3: Jerarquia de operaciones")
    p = int(input("Ingrese el primer número: "))
    r = int(input("Ingrese el segundo número: "))
    k = int(input("Ingrese el tercer numero: "))

    print("1. p*r+k")
    print("2. p*(r+k)")
    print("3. p/r+k")
    print("4. 3p+2r/k**2")
    print("5. Cuadratica")
    print("6. Salir")

    opcion = input("Elija la ecuacion que desea: ")

    if opcion=="1":
        operacion1= (p*r)+k
        print("resultado de: ", p, "*", r, "+", k, "=", operacion1)
    elif opcion=="2":
        operacion2= p *(r+k)
        print("resultado de: ", p, "*", "(", r, "+", k, ")", "=", operacion2)
    elif opcion=="3":
        operacion3= p/(r+k)
        print("resultado de: ", p, "/", "(", r, "+", k, ")", "=", operacion3)
    elif opcion=="4":
        operacion4= ((3*p)+(2*r))/k**2
        print("resultado de: ""(3 ", p, ")", "+", "(", "2 ", r, ")", "/", k," 2", "=", operacion4) 
    elif opcion=="5": 
        discriminante = (r ** 2) - (4 * p * k) 
        x1 = (-r+(discriminante)**0.5)/(2*p) 
        x2 = (-r-(discriminante)**0.5)/(2*p)
        if p==0: 
            print("p no puede ser 0") 
        elif discriminante <= 0:
            print("el discriminante no puede ser 0 o menor que 0")
        else:
            print("x1= ", x1)
            print("x2=", x2)
    elif opcion =="6":
        print("¡hasta luego!")
        CODIGO = False
    else: 
        print("Opción no válida. Por favor, elija una opción válida (1-6).")
