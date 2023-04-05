#Realice un programa que muestre un menú con las siguientes opciones: 1) Sumar 2) Restar 3) Multiplicar 4) Dividir 5) Salir. El usuario debe seleccionar una opción, y a continuación, el programa debe solicitar el ingreso de dos números enteros y debe realizar la operación correspondiente a la opción seleccionada. La ejecución debe realizarse una y otra vez, hasta que el usuario seleccione la opción #5.


print("Menú principal: \n \n 1) Sumar \n 2) Restar \n 3) Multiplicar \n 4) Dividir \n 5) Salir \n")
seleccion = int(input("Seleccione una opcion: "))


while seleccion != 0:
  if seleccion != 0 and seleccion <= 4:
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro numero: "))
  if seleccion == 1:
    resultado = num1 + num2
    print(f"El resultado es {resultado}")
    seleccion = int(input("\n Seleccione otra opción: "))
  elif seleccion == 2:
    resultado = num1 - num2
    print(f"El resultado es {resultado}")
    seleccion = int(input("\n Seleccione otra opción: "))
  elif seleccion == 3:
    resultado = num1 * num2
    print(f"El resultado es {resultado}")
    seleccion = int(input("\n Seleccione otra opción: "))
  elif seleccion == 4:
    resultado = num1 / num2
    print(f"El resultado es {resultado}")
    seleccion = int(input("\n Seleccione otra opción: "))
  elif seleccion == 5:
    print("Saliendo del sistema")
    break