COP = float(input("Ingrese el valor en pesos colombianos: "))
cambio = input("¿A que moneda desea convertirlo (USD, EUR, JPY): ")

if cambio == "USD":
    cambio = (COP * 0.00027)

if cambio == "EUR":
    cambio = (COP * 0.00023)

if cambio == "JPY":
    cambio = (COP * 0.030)

print(cambio)
