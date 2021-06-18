# Problema 2.

parcial1 = float(input("Ingrese la nota del primer parcial: "))
parcial2 = float(input("Ingrese la nota del segundo parcial: "))
taller = float(input("Ingrese la nota del taller: "))
proyecto = float(input("Ingrese la nota del proyecto: "))
notafinal = float(parcial1 * 0.25)+(parcial2 * 0.25)+(taller*0.2)+(proyecto*0.3)

print("Tu nota final es: %s" % notafinal)