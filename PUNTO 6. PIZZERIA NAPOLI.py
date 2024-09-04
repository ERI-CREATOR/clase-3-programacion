print("Bienvenido a la pizzería Bella Napoli")

pedido = int(input("¿Quieres una pizza vegetariana?: 1. sí 2. no "))

if pedido == 1:
    print("Elegiste la pizza vegetariana")
    ingredientes1 = input("La pizza lleva incluida mozzarella y tomate. Elige un solo ingrediente: P.pimiento, T.tofu ")
    
    if ingredientes1 == "P":
        print("Los ingredientes de la pizza vegetariana son: mozzarella, tomate y pimiento")
    elif ingredientes1 == "T":
        print("Los ingredientes de la pizza vegetariana son: mozzarella, tomate y tofu")
    else:
        print("Ingrediente no válido. Selecciona 'P' para pimiento o 'T' para tofu.")
else:
    print("Elegiste la pizza no vegetariana")
    ingredientes2 = input("La pizza lleva incluida mozzarella y tomate. Elige un solo ingrediente: PE.peperoni, J.jamón, S.salmon ")
    
    if ingredientes2 == "PE":
        print("Los ingredientes de la pizza no vegetariana son: mozzarella, tomate y peperoni")
    elif ingredientes2 == "J":
        print("Los ingredientes de la pizza no vegetariana son: mozzarella, tomate y jamón")
    elif ingredientes2 == "S":
        print("Los ingredientes de la pizza no vegetariana son: mozzarella, tomate y salmón")
    else:
        print("Ingrediente no válido. Selecciona 'PE' para peperoni, 'J' para jamón o 'S' para salmón.")