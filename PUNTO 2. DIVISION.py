print("bienvenido al sistema")
numerador = float(input("Introduce el numerador: "))
divisor = float(input("Introduce el divisor: "))

if divisor == 0:
    print("Error: no se es posible dividir cero.")
else:
    resultado = numerador / divisor
    print(f"el resultado de la division es: {resultado}")
