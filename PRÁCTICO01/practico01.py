import random
import matplotlib.pyplot as plt


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


sumXY = 0
for i in range(n):
    sumXY += estaturas[i] * pesos[i]

sumX = sum(estaturas)
sumY = sum(pesos)
sumX2 = sum([x**2 for x in estaturas])

a = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX**2)
b = (sumY - a * sumX) / n

print('a =', a)
print('b =', b)


pesoIdeal = [a * x + b for x in estaturas]

plt.plot(estaturas, pesoIdeal, color='red', label='Línea de regresión')

formula = 'Regresion Lineal: ' f'y = {a:.2f}x + {b:.2f}'
plt.text(min(estaturas), max(pesos), formula, fontsize=12, color='red')

plt.scatter(estaturas, pesos, color='blue')
plt.title('Estatura vs Peso')
plt.xlabel('Estatura (m)')
plt.ylabel('Peso (kg)')
plt.grid(True)
plt.show()
