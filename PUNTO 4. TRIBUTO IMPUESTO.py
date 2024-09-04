print("Bienvenido al sistema")
print("Contesta las siguientes preguntas para determinar tu impuesto a Declarar")

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
ingreso_mensual = float(input("Introduce tu ingreso mensual: "))

if edad > 18 and ingreso_mensual >= 3000000:
    print("Erika, te corresponde declarar para este periodo.")

else: 
    print("Erika, No te corresponde Declarar en este periodo. ")

