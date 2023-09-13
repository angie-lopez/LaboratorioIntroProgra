print("ejercicio 2")
d=input("ingrese el numero de dia: ")
dnum=int(d)

print(type(dnum))
print("Dia: ")


if dnum < 0 or dnum> 7:
    print("Error: El numero a ingresar debe de estar contenido de 1 a 7")
elif dnum == 1: 
    print("lunes")
elif dnum == 2:
    print("martes")
elif dnum == 3:
    print("miercoles")
elif dnum == 4: 
    print("jueves")
elif dnum == 5: 
    print("viernes")
elif dnum == 6: 
    print("sabado")
elif dnum == 7: 
    print("domingo")
