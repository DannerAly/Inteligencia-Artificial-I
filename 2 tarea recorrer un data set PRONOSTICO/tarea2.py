import pandas as pd  # type: ignore

# Leer el archivo CSV
archivo_dataset = pd.read_csv("pesosyestaturas.csv")
print(archivo_dataset)


promedio_peso_Y = archivo_dataset["Peso"].mean()
promedio_estatura_X = archivo_dataset["Estatura"].mean()

# sumatoria(x*y de todas las columnas)
sumatoria_producto = (archivo_dataset["Peso"] * archivo_dataset["Estatura"]).sum()

sumatoria_estatura_cuadrado = (archivo_dataset["Estatura"] ** 2).sum()

b= (sumatoria_producto - 10 * promedio_estatura_X * promedio_peso_Y) / (sumatoria_estatura_cuadrado - 10 * (promedio_estatura_X)**2) 
a = promedio_peso_Y - b * promedio_estatura_X

print ("El valor de a es: ", a)
print ("El valor de b es: ", b)

def predecirPeso(x):
    return a + b * x

estatura = int(input("Ingresa un número entero: "))
print("Predicción de peso para la estatura ingresada:", predecirPeso(estatura))



