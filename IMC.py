print("===BIENVENIDO A CALCULAR TU IMC===")
print("INGRESA TUS DATOS PORFAVOR")

altura = float(input("INGRESA TU ALTURA:"))
peso = float(input("INGRESA TU PESO:"))

print("haciendo calculos....")

IMC = peso / (altura ** 2)
print(IMC)

if IMC >= 40:
    print("Tienes obesidad III")
elif IMC >= 35:
    print("Tienes obesidad II")
elif IMC >= 30:
    print("Tienes obesidad tipo I")
elif IMC >= 25:
    print("Estas en sobrepeso")
elif IMC >= 22:
    print("Estas en tu peso correcto")
elif IMC >= 18.5:
    print("Tienes bajo peso")
else:
    print("ESTAS EN DESNUTRICION")
