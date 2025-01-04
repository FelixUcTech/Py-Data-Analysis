# Python Para Ciencia de Datos
- [NumPy](#numpy-menú)
    - [Algunas funcionalidades de numpy](#algunas-funcionalidades-de-numpy-menú)
    - [Algebra líneal](#algebra-líneal-menú)
    - [Indexación y Slicing](#indexación-y-slicing-menú)
- [Pandas](#pandas-menú)
- [Matplotlib](#matplotlib-menú)

## Introducción
Dentro de la sheet de colab podemos validar si están instalados los paquetes(bibliotecas de software)
```py
# Validar si están instaladas las bibliotecas
try:
    import numpy
    print("NumPy está instalado. Versión:", numpy.__version__)
except ImportError:
    print("NumPy no está instalado.")

try:
    import matplotlib
    print("Matplotlib está instalado. Versión:", matplotlib.__version__)
except ImportError:
    print("Matplotlib no está instalado.")

try:
    import pandas
    print("Pandas está instalado. Versión:", pandas.__version__)
except ImportError:
    print("Pandas no está instalado.")
```
Las versiones qué nos aparecieron después de ejecutarlos son:

- NumPy está instalado. Versión: 1.26.4
- Matplotlib está instalado. Versión: 3.8.0
- Pandas está instalado. Versión: 2.2.2

**Importante redefinir los nombres para trabajar con abreviaciones**
```py
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
```

## NumPy [(Menú)](#python-para-ciencia-de-datos)
### Intro
NumPy nos permite realizar operaciones matemáticas y estadísitcas de alto rendimiento
### Algunas funcionalidades de numpy [(Menú)](#python-para-ciencia-de-datos)

**Suma de total de elementos de un array**
```py
array = np.array([[1,2,3],[4,5,6]])
sum = np.sum(array)
print("Total: ", sum)
```
**Media**  
```py
Media =  np.mean(np.array([[1,2,3],[4,5,6]]))
print("Media del array:", Media)
```

**Desviación estandar**
```py
std = np.std(np.array([[1,2,3],[4,5,6]]))
print("Desviación standar:", std)
```
### Algebra líneal [(Menú)](#python-para-ciencia-de-datos)

El álgebra líneal opera entre matrices que nos pemiten hacer calculos de manera eficiente cuando hay matrices de nxn aplicando correctamente cada concepto del algebra líneal. En la universidad 
### Indexación y Slicing [(Menú)](#python-para-ciencia-de-datos)
Estos dos conceptos nos permiten, sleeccionar y manipular subconjuntos de datos sin necesidad de copiar grandes volúmenes de información, podría ser como una ruta de consulta continua, no necesitamos todo lo qué está en el directorio de la ruta amarilla, solo cierta información y cada ver que ejecutamos una consulta o relazamos algún procesamiento con los datos, nos vamos directo a la información que requerimos sin necesidad de qué el procesador lea el resto de información, relacionandolo a la ingeniería de datos, cada milisegundo en una consulta de millones de datos en un servidor distribuido podría definir la eficiencia de nuestra aplicación o producto.

La indexación y el slicing en Python son conceptos relacionados, pero no son exactamente lo mismo. Indexación se refiere a acceder a un solo elemento de una secuencia (como una lista, tupla o array) usando su posición o índice, mientras que slicing permite obtener una sub-secuencia de la secuencia original, especificando un rango de índices (inicio, fin y paso). La indexación devuelve un único valor, mientras que el slicing devuelve una nueva secuencia (lista, tupla o array) con los elementos seleccionados en el rango indicado. Ambos son fundamentales para manipular datos en estructuras como listas, cadenas y arrays.

**Ejemplo**
NumPy está diseñado para trabajar con arreglos multidimensionales homogéneos, donde cada fila (o dimensión) debe tener la misma cantidad de elementos.

```py
import numpy as np
#Si realmente necesitas listas de diferentes longitudes, usa un array de tipo objeto
matriz = np.array([[1,2,3],[32,32,32],[1,1,1,1],[7,7,7,7,7]], dtype = object)
#Se busca lo qué queremos dentro de la matriz de prueba
print("Primeras dos matrices:", matriz[0:2])#como los límites de una función [toca - no lo toca se aproxima)
```

**Otro ejemplo**
```py
# Array NumPy con dtype=object
import numpy as np
matriz = np.array([[1, 2, 3], [32, 32, 32], [1, 1, 1, 1], [7, 7, 7, 7, 7]], dtype=object)

# Usando un bucle para obtener el primer elemento de cada sublista
primeros_elementos = [sublista[0] for sublista in matriz]
print(primeros_elementos)  # Salida: [1, 32, 1, 7]
```

**Indexacción buleana**

Este tipo de filtro o direccionamiento es por medio de una condición lógica qué cumpla la sentencia. Este tipo de indexación nos devuelve el mismo array pero en terminos lógicos qué cumplan la condición.

```py
import numpy as np
matriz = np.array([[1, 2, 3], [32, 32, 32], [1, 1, 1], [7, 7, 7]])
bool_index = matriz <= 6
print(bool_index)
```
### Broadcasting
Nos permite operar array de diferentes dimensiones normalizandolos en relación al array más grande, se deben cumplir ciertas condiciones, para aplicar estás funciones, en resumen es una operación que se puede replicar en el array más grande pero siempre y cuando la semantica del código lo permita.

**Algunos ejemplos**

```py
import numpy as np
porescalar = np.array([100,200,300]) * np.array([.9])
print("Descuento:", porescalar)
```

```py
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
concatenar = np.concatenate((b,a))
print("Resultado: ", concatenar)
```

Son una infinidad de operaciones qué se pueden hacer en Numpy entre matrices aplicando el concepto de broadcating, qué es un concepto utilizado también en comunicaicones de radio, qué es una señal qué se comunica de una fuente a multiples, como la televisión, pues resumiendo, si puedes aplicar el concepto en algebra líneal lo puedes aplicar en Numpy en operación de matrices, cada operación en algabra líneal puede tener sus limitantes, y es ahí donde el código las puede solventar, esjemplo la multiplicación por dos escalares.

```py
import numpy as np

# Option 1: If you want to multiply each element of the first array by each element of the second array,
# you can reshape one of the arrays to introduce a new dimension of size 1.
# This will allow broadcasting to work.

porescalar = np.array([100, 200, 300])[:, np.newaxis] * np.array([.9, 0.8])  
print("Descuento (Option 1):", porescalar)

# Output:
# Descuento (Option 1): [[ 90.  80.]
#                        [180. 160.]
#                        [270. 240.]]


# Option 2: If you intended to multiply corresponding elements of the two arrays,
# you need to ensure they have the same shape.
# In this case, you might need to adjust your data or the operation you want to perform.

# Example: If you want to apply discounts of 0.9 and 0.8 to the first two elements of the first array:

porescalar = np.array([100, 200, 300])[:2] * np.array([.9, 0.8]) 
print("Descuento (Option 2):", porescalar)

# Output:
# Descuento (Option 2): [ 90. 160.]
```

El ejemplo anterior no es tan directo en código pero se puede solventar si fuera una necesidad.

**Unir diferentes filas en una misma matriz**

```py
stacked_vertical = np.vstack((a,b,a,b))
print("Vertical: ", stacked_vertical)

#Este es equivalente en resultado a la concatenación
#Es importante  saber cual tiene mejor rendimiento si nos lleran a pedir otimizar la operación
stacked_horizontal = np.hstack((a,b,a,b))
print("Vertical: ", stacked_horizontal)
```

**Dividir un array largo en un valor dado**

```py
array_largo = np.arange(1,131)
split_matriz =  np.split(array_largo,10)#Debe ser un multiplo para qué te genere la tabla
print("Tabla del 13: ", split_matriz)
```
### Copias y vistas
**Copia**
Cuando haces una copia de una estructura de datos (como una lista o un array de NumPy), Python crea una nueva instancia en memoria con los mismos valores, pero independiente del objeto original. Las modificaciones en la copia no afectan al objeto original.

```py
import numpy as np
original = np.array([1, 2, 3])
copia = original.copy()

copia[0] = 99
print("Original:", original)  # [1, 2, 3]
print("Copia:", copia)        # [99, 2, 3]
```
**Vista**
Una vista en cambio, es una referencia al mismo bloque de memoria que el objeto original. Esto significa que cualquier cambio realizado en la vista también afecta al objeto original, ya que ambas comparten la misma memoria.

```py
import numpy as np
original = np.array([1, 2, 3])
vista = original[1:]  # Crear una vista del array

vista[0] = 99
print("Original:", original)  # [1, 99, 3]
print("Vista:", vista)        # [99, 3]
```
**¿Cómo saber si es una copia o una vista?**
Puedes usar el método base de un array de NumPy para verificar si un objeto es una vista de otro. Si el atributo base es None, entonces el objeto es una copia. Si tiene una referencia (no None), entonces es una vista.

```py
import numpy as np
original = np.array([1, 2, 3])
copia = original.copy()
vista = original[1:]

print(copia.base)  # None, porque es una copia
print(vista.base)  # <numpy.ndarray object>, porque es una vista
```
### Darle reshaped y transpuesta 

import numpy as np
```py
import numpy as np
# Crear un array 2x3
matriz = np.array([[1, 2, 3], [4, 5, 6]])

# Obtener la transposición
transpuesta = matriz.T

print("Matriz original:")
print(matriz)
print("\nTranspuesta:")
print(transpuesta)
```

Para el siguiente caso podemos organizar cualquier matriz de fXe a lxi siempre y cuando la dimensionalidad a la que se va a cambiar sea equivalente en numeros de elementos, ejemplo una de 3x3 no se podría convertir en 4x2, dado qué un elemento quedaría bailando, pero sí una de 3x3 podría convertirse en una de 1x9 y 9x1, esto porque no hay otro multiplo par 9.

```py
import numpy as np

# Crear un array 1D
array_unidimensional = np.array([1, 2, 3, 4, 5, 6])

# Reshape para convertirlo en un array 2D de forma (2, 3)
reshapeado = array_unidimensional.reshape(2, 3)

print("Array original:")
print(array_unidimensional)
print("\nArray reshapeado (2x3):")
print(reshapeado)
```
**Flattening & Reverse**
El flattening está estrechamente relacionado con el machine learning, especialmente en modelos que requieren convertir datos complejos en una representación más simple y procesable. Por ejemplo, en redes neuronales, las imágenes (que suelen ser arrays multidimensionales) se aplanan en un vector unidimensional antes de pasarlas a las capas densas para facilitar el cálculo de pesos y sesgos. Este proceso transforma datos estructurados (como matrices o tensores) en una forma que los algoritmos pueden manejar más fácilmente, lo que es crucial para entrenar modelos de clasificación, regresión o reconocimiento de patrones. Sin embargo, el uso de flattening debe ser contextual, ya que en algunos casos puede implicar pérdida de relaciones espaciales importantes, por lo que se complementa con técnicas que preserven dicha información, como en redes convolucionales.

```py
# Crear un array 2D
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Revertir las filas
revertir_filas = array_2d[::-1]

# Revertir las columnas
revertir_columnas = array_2d[:, ::-1]

print("Array original:")
print(array_2d)
print("\nArray con filas revertidas:")
print(revertir_filas)
print("\nArray con columnas revertidas:")
print(revertir_columnas)

```
```py
import numpy as np

# Crear un array 2D
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Aplanar el array
array_aplanado = array_2d.flatten()

print("Array original:")
print(array_2d)
print("\nArray aplanado:")
print(array_aplanado)

```
### Resumen de código
**Elementales**
```py
import numpy as np

array1 = np.array([10, 20, 30, 40])
array2 = np.array([1, 2, 3, 4])

suma = array1 + array2
resta = array1 - array2
multiplicacion = array1 * array2
division = array1 / array2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
```

**Cálculos estadísticos en Arrays**
```py
pythonCopiar código
import numpy as np

datos = np.array([23, 76, 35, 67, 89, 45, 68, 79, 35])

media = np.mean(datos)
mediana = np.median(datos)
varianza = np.var(datos)
desviacion = np.std(datos)

print("Media:", media)
print("Mediana:", mediana)
print("Varianza:", varianza)
print("Desviación estándar:", desviacion
```

**Operaciones Matriciales**
```py
import numpy as np

matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])

suma_matrices = matriz1 + matriz2
resta_matrices = matriz1 - matriz2
producto_matrices = np.dot(matriz1, matriz2)
inversa_matriz1 = np.linalg.inv(matriz1)

print("Suma de matrices:\n", suma_matrices)
print("Resta de matrices:\n", resta_matrices)
print("Producto de matrices:\n", producto_matrices)
print("Inversa de la matriz 1:\n", inversa_matriz1)
```

**Resolución de un Sistema de Ecuaciones Lineales**
```py
import numpy as np

A = np.array([[2, 3], [1, 2]])
b = np.array([8, 5])

x = np.linalg.solve(A, b)
print("Solución del sistema de ecuaciones:", x)
```
**Simulación de Datos**
```py
import numpy as np

datos_simulados = np.random.normal(0, 1, 1000)
media_simulada = np.mean(datos_simulados)
desviacion_simulada = np.std(datos_simulados)

print("Media de los datos simulados:", media_simulada)
print("Desviación estándar de los datos simulados:", desviacion_simulada)
```

## Pandas [(Menú)](#python-para-ciencia-de-datos)
### intro
https://pandas.pydata.org/docs/user_guide/

Pandas está construido sobre NumPy, facilitando la manipulación y el análisis de datos, es ideal para trabajar con datos tabulares como los qué se encuentran en hojas de cálculos, o bases de datos relacionales. Una excelente bibliográfica qué me ayudo mucho en la universidad pero si aún no has llegado ahí puedes abordarla con simples **buenas bases de aritmetica y algebra** es **Álgebra líneal una introducción moderna por David Poole de la editorial CENGAGE Learning**.

Relacionado a esto:
-  NumPy proporciona herramientas para resolver sistemas de ecuaciones lineales.
- Aprendizaje Automático: Los algoritmos de regresión lineal, redes neuronales y otros modelos dependen en gran medida de las operaciones matriciales.

Las dos estructuras principales que ofrece pandas son las **Series y los Dataframes**
Una representa  una tabla la cual es dataframes y la otra representa cada columna, la cues es la serie.

**IMPORTANTE PARA PONER EN PRÁCTICA PANDAS** [Algunos Data Frames](https://www.kaggle.com/)

```py
import pandas as pd

# Crear un DataFrame (tabla)
data = {
    "Nombre": ["Ana", "Luis", "María"],
    "Edad": [25, 30, 22],
    "Ciudad": ["Madrid", "Barcelona", "Sevilla"]
}

df = pd.DataFrame(data)

# Obtener una Serie (columna) del DataFrame
serie_edades = df["Edad"]

print("DataFrame completo:")
print(df)

print("\nSerie 'Edad':")
print(serie_edades)

# Verificar los tipos
print("\nTipo del DataFrame:", type(df))
print("Tipo de la Serie:", type(serie_edades))

```
### loc [(Menú)](#python-para-ciencia-de-datos)

Para extraer datos con la función de pandas, loc, podemos hacerlo de la siguiente manera.

```py
consulta = data.loc[:,["Columna1","Columna27"]]
print(consulta)
```
La función loc en pandas devuelve una vista o una copia, dependiendo del contexto. Esto significa que el comportamiento puede variar según cómo se utilice. A continuación, te explico los casos relevantes:

Cuando devuelve una vista
- Si accedes a columnas o filas específicas y luego modificas esa selección, es probable que los cambios se reflejen en el DataFrame original, ya que estás trabajando con una vista.
- Por ejemplo, si accedes con loc para modificar un valor directamente, afecta al DataFrame original.

```py
import pandas as pd

# Crear DataFrame
data = pd.DataFrame({
    "Columna1": [1, 2, 3],
    "Columna27": [4, 5, 6]
})

# Usar loc para obtener una vista
consulta = data.loc[:, ["Columna1", "Columna27"]]

# Modificar el valor
consulta.iloc[0, 0] = 100

print("DataFrame original:")
print(data)
```

Cuando devuelve una copia
Si utilizas funciones o métodos que explícitamente indican que trabajan con copias (por ejemplo, añadiendo .copy()), la operación genera una nueva instancia en memoria. Esto asegura que cualquier cambio en la selección no afecte al DataFrame original.

```py
# Crear una copia explícita
consulta_copia = data.loc[:, ["Columna1", "Columna27"]].copy()

# Modificar el valor
consulta_copia.iloc[0, 0] = 200

print("DataFrame original:")
print(data)

print("\nDataFrame copia:")
print(consulta_copia)
```
### Datos Faltantes
**¿Cómo identificar los datos faltantes?**

https://pandas.pydata.org/docs/user_guide/missing_data.html

Se utilizan unas funciones para determinar los datos faltantes por columna, esto con los siguientes 2 métodos.

```py
import pandas as pd
df = pd.read_csv('/bangladesh_divisions_dataset.csv')
datos_faltantes =  df.isna().sum()
print("Datos faltantes por columna\n", datos_faltantes)
```

.isna() determina los favoles faltantes mediente la escritura de True en la casilla donde haya falta, y con sum(), por columna hace el conteo de los trues, que se hayan encontrado en el dataframe. **Cuando faltan datos, hay dos opciones eliminar la las filas o columnas correspondientes a los datos faltantes o agregar la información faltante**, es importante hacer esto aunque sea obvio porque implicar grandes cambios en el desarollo de nuestro análisis.

Caso uno 1.1 eliminar filas donde haya datos faltantes, con la función **.dropna()**. Para este primer caso perdemos algunas filas y pero mantenemos las columnas.
```py
import pandas as pd

DatosLimpios = df.dropna()
# Puede escribirse dropna(axis = 0), es equivalente a no poner nada.
print("Sin filas con valores faltantes\n", DatosLimpios)
```

Caso dos 1.2 Ahora eliminar las columnas donde haya datos faltantes esto no es recomendable si no es esctrictamente necesario porque puede ser más factible hacer el analisis si solo falta un dato a qué se elimine toda la info, aliminamos las columnas donde hubieran datos faltantes pero mantenemos el total de filas.

```py
import pandas as pd

DatosLimpios = df.dropna(axis=1)
print("Sin columnas con valores faltantes\n", DatosLimpios)
```

2.1 Rellenar donde haya datos faltantes

```py
tabla_rellenada = df.fillna("Datos no disponible")

print("Rellenado con 'Datos no disponible'\n", tabla_rellenada)

# Filtrar filas que contienen 'Datos no disponible' en cualquier columna
filas_con_datos_no_disponible = tabla_rellenada[
    tabla_rellenada.isin(["Datos no disponible"]).any(axis=1)
]

print("Filas con 'Datos no disponible':\n", filas_con_datos_no_disponible)
```
Si volvemos apreguntar si hay datos no dispoibles pero a tabla_rellenada, encontraremos que no hay valores vacios.
### Creación y Manipulación de Columnas en Padaas


## Matplotlib [(Menú)](#python-para-ciencia-de-datos)

Nos permite visualizar los datos de manera efectiva, 