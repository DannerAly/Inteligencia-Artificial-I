import random

def generarPeso(estatura):
    if estatura > 1:
        estaturaAjust = estatura * 100 - 100
        peso = random.randint(int(estaturaAjust - 10), int(estaturaAjust + 10))
    else:
        peso = random.randint(8, 12)
    return peso

n = 100
datos = [] 

for i in range(n):
    estatura = round(random.uniform(1.5, 2.0),2)
    peso = generarPeso(estatura)
    datos.append((estatura, peso))

estaturas = [x[0] for x in datos]
pesos = [x[1] for x in datos]

print(datos)

errorMenor = 1000
for a in range(-100, 101):
    for b in range(-100, 101):
        
        errorTotal = 0
        for i in range(len(estaturas)):
            Y = a * estaturas[i] + b
            errorAbs = abs(pesos[i] - Y)
            errorTotal += errorAbs

        if errorTotal < errorMenor:
            errorMenor = errorTotal
            mejorA = a
            mejorB = b

print(f"El menor error absoluto total es: {errorMenor}")
print(f"Mejor valor de a: {mejorA}")
print(f"Mejor valor de b: {mejorB}")