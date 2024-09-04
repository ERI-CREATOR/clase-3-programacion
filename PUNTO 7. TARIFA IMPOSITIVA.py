print("Bienvenido al sistema de calculo impositivo")
print("definiremos el porcentaje y tarifa a declarar ")

renta = float(input("introduce tu renta anual:"))

if renta < 1000000:
    tarifa_impositiva = "5%"
elif 1000000 <= renta <= 2000000:
    tarifa_impositiva = "15%"
elif 2000000 < renta <= 3500000:
    tarifa_impositiva = "20%"
elif 3500000 < renta <= 6000000:
    tarifa_impositiva = "30%"
else: 
    tarifa_impositiva = "45%"
print("la tarifa impositiva que te corresponde es:", tarifa_impositiva)
