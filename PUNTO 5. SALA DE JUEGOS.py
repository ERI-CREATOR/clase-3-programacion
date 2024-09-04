print("Bienvenido al sistema")
edad = int(input("Introduce la edad del cliente: "))
if edad < 4:
    precio = 0
    print("Puedes ingresar gratis")
elif 4 <= edad <= 18:
    precio = 5000
    print("El valor de la entrada correspondiente es 5000")
else:
    precio = 10000

print("El valor de la entrada correspondiente es 10000")