Peso = input("Cuál es su peso en kilogramos?")
Estatura = input("Cuál es su estatura en metros?")

imc = round(float(Peso)/ float(Estatura)**2, 2)

print("Su indice de masa corporal es", imc)