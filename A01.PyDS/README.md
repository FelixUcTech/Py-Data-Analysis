# Python Para Ciencia de Datos
- [NumPy](#numpy-menú)
    - [Algunas funcionalidades de numpy](#algunas-funcionalidades-de-numpy-menú)
    - [Algebra líneal](#algebra-líneal-menú)
    - [Indexación y Slicing](#indexación-y-slicing-menú)
    - [Broadcasting](#broadcasting-menú)
    - [Copias y vistas](#copias-y-vistas-menú)
    - [Darle reshaped y transpuesta](#darle-reshaped-y-transpuesta-menú)
    - [Resumen de código](#resumen-de-código-menú)
- [Pandas](#pandas-menú)
    - [Intro Pandas](#intro-pandas)
    - [Loc](#loc-menú)
    - [Creación y Manipulación de Columnas en Pandas](#creación-y-manipulación-de-columnas-en-pandas-menú)
    - [Agrupaciones](#agrupaciones-menú)
    - [Filtrado de Datos](#filtrado-de-datos-menú)
    - [Pivot y Reshape en Pandas](#reestructuración-de-datos-pivot-y-reshape-en-pandas-menú)
    - [Fusión de da DataFrames](#fusión-de-da-dataframes-menú)
    - [Series Temporales](#series-temporales-menú)
- [Matplotlib](#matplotlib-menú)
    - [Intro Matplotlib](#intro-matplotlib-menú)
    - [Personalización de Gráficos](#personalización-de-gráficos-menú)
    - [Gráficos de Barras y Diagramas de Pastel](#gráficos-de-barras-y-diagramas-de-pastel-menú)
    - [Histograma y Boxplot](#histograma-y-boxplot-menú)
    - [Series de tiempo y fechas](#series-de-tiempo-y-fechas-menú)
    - [Layouts Avanzados](#layouts-avanzados-menú)
- [Proyecto personal](#proyecto-personal-menú)
    

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
### Intro Numpy 
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
### Broadcasting [(Menú)](#python-para-ciencia-de-datos)
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
### Copias y vistas [(Menú)](#python-para-ciencia-de-datos)
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
### Darle reshaped y transpuesta [(Menú)](#python-para-ciencia-de-datos)

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
### Resumen de código [(Menú)](#python-para-ciencia-de-datos)
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
### Intro Pandas
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
### Datos Faltantes [(Menú)](#python-para-ciencia-de-datos)
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
### Creación y Manipulación de Columnas en Pandas [(Menú)](#python-para-ciencia-de-datos)

**Creación de una columan nueva en función de operaciones aritmeticas**
```py 
import pandas as pd

df_walmart = pd.read_csv("/Walmart_Sales.csv")

df_walmart['Multiplicacion'] = ((df_walmart['Fuel_Price'])/(df_walmart['CPI']))

print(df_walmart)
```
**Nueva columna basada en condicionales**

```py 
import pandas as pd

df_walmart = pd.read_csv("/Walmart_Sales.csv")

df_walmart['Multiplicacion'] = ((df_walmart['Fuel_Price'])/(df_walmart['CPI']))

df_walmart['Mayor a la media'] = ((df_walmart['Multiplicacion'])>(df_walmart['Multiplicacion'].mean()))

print(df_walmart)
```

**Cambiar el tipo de variable de una columna**
```py 
import pandas as pd

df_walmart = pd.read_csv("/Walmart_Sales.csv")

print(df_walmart.info())

df_walmart['Date'] = pd.to_datetime(df_walmart['Date'], format='%d-%m-%Y')

print(df_walmart.info())
```

**Aplicar una función labdam en la columan**
```py
import pandas as pd

df_walmart = pd.read_csv("/Walmart_Sales.csv")

# Convertir la columna 'Date' al formato datetime
df_walmart['Date'] = pd.to_datetime(df_walmart['Date'], format='%d-%m-%Y')

# Crear nuevas columnas para el año y mes utilizando lambda
df_walmart['Year'] = df_walmart['Date'].apply(lambda x: x.year)
df_walmart['Month'] = df_walmart['Date'].apply(lambda x: x.month)

# Mostrar las primeras filas con las nuevas columnas
print(df_walmart[['Date', 'Year', 'Month']].head())
```
**Transformaciones con datos categóricos**

```py
import pandas as pd

# Crear un DataFrame de ejemplo
df = pd.read_csv("/Walmart_Sales.csv")

# Definir la función para categorizar
def categorize_column(df, column_name, new_column_name='Category'):
    """
    Categoriza los valores de una columna en 10 divisiones simétricas basadas en su rango.
    
    Args:
        df (pd.DataFrame): El DataFrame que contiene la columna a categorizar.
        column_name (str): El nombre de la columna a categorizar.
        new_column_name (str): El nombre de la nueva columna con las categorías.
        
    Returns:
        pd.DataFrame: El DataFrame original con una nueva columna de categorías.
    """
    min_value = df[column_name].min()
    max_value = df[column_name].max()
    interval_size = (max_value - min_value) / 10
    
    # Función lambda para asignar categorías
    def categorize_value(value):
        for i in range(10):
            if value <= min_value + (i + 1) * interval_size:
                return f"Category {i + 1}"
        return f"Category 10"  # Para el último intervalo
    
    # Crear una nueva columna con las categorías
    df[new_column_name] = df[column_name].apply(categorize_value)
    return df

# Aplicar la función a una columna específica
df = categorize_column(df, 'Temperature', new_column_name='Category_Temperature')

# Mostrar el DataFrame resultante
print(df)
```
### Agrupaciones [(Menú)](#python-para-ciencia-de-datos)
Las agrupaciones son similares a SQL o Postgres, dependen de una columna para el resultado relacionado a otra.

```py
import pandas as pd
df = pd.read_csv("/content/drive/MyDrive/Curso de Python para Ciencia de Datos/Walmart_Sales.csv")
# df.info()

# Configurar pandas para mostrar números completos
pd.options.display.float_format = '{:.2f}'.format


# El agrupamiento de la cantidad de ventas por tienda qué haya en la base de datos
# df["Store"].value_counts()

# Suma de las ventas por tienda
grupo_de_ventas =  df.groupby("Store")["Weekly_Sales"].sum()
print(grupo_de_ventas)
```
Utilizando consultas simultaneas medinate .agg, en pandas es extremadamente flexible y permite aplicar múltiples funciones de agregación a un grupo o conjunto de columnas. Con .agg, puedes realizar operaciones como suma, promedio, conteo, y más, además de combinar varias funciones en una sola llamada.}

```py
import pandas as pd
df = pd.read_csv("/content/drive/MyDrive/Curso de Python para Ciencia de Datos/Walmart_Sales.csv")

grupo = df.groupby("Store").agg({
    "Weekly_Sales": ['sum', 'mean'],
    "Temperature": ['max', 'min']
})

print(grupo)
```

Obteniendo agrupaciones dentro de las agrupaciones, y utilizando varias operaciones para esos subconjuntos.

```py
import pandas as pd
df = pd.read_csv("/content/drive/MyDrive/Curso de Python para Ciencia de Datos/Walmart_Sales.csv")

grupo = df.groupby(["Store", "Fuel_Price"]).agg({
    "Weekly_Sales": ['sum', 'mean'],
    "Temperature": ['max', 'min']}
)

print(grupo)
```
### Filtrado de Datos [(Menú)](#python-para-ciencia-de-datos)
Filtrar información nos permite centrar nuestra atención en lo que realmente importa para nuestro cliente o para nuestra actividad, al igual qué el filtrado inicial es super importante porque reduce la cantidad de recursos qué solicitamos, ejemplo en MongoDB se utiliza el filtrado de información $match antes o como primera capa para que los datos que se procesen sean menores.

Suponiendo que tengo que realizar un análisis único de una tienda en particular, genero un subconjunto de datos de mi dataframe original.

```py
import pandas as pd
df = pd.read_csv("/content/drive/MyDrive/Curso de Python para Ciencia de Datos/Walmart_Sales.csv")

# Filtrado de Datos para la tienda 27
df_tienda_27 = df[df["Store"] == 27]

print("Filtrado de Datos para la tienda 27")
print(df_tienda_27)
```

También podríamos agregar más de un filtro en una misma sentencia.
```py
import pandas as pd
df = pd.read_csv("/content/drive/MyDrive/Curso de Python para Ciencia de Datos/Walmart_Sales.csv")

# Filtrado de Datos para la tienda 27
df_tienda_27 = df[(df["Store"] == 27) & (df["Weekly_Sales"] > 1000)]

print("Filtrado de Datos para la tienda 27")
print(df_tienda_27)
```
### Reestructuración de datos: Pivot y Reshape en Pandas [(Menú)](#python-para-ciencia-de-datos)
Una pivot table es una herramienta para resumir y reorganizar columnas de un DataFrame de pandas, que además permite crear cálculos estadísticos (suma, conteos, promedios, etc.).

Básicamente transforma los valores de determinadas filas o columnas en indices de un nuevo DataFrame, la intersección de éstos es el valor resultante.

La nueva organización de los datos nos ayuda a encontrar patrones que pudieran estar ocultos en los datos crudos.

Función:

pivot_table(): Puede implementarse directo del DataFrame o a partir de la librería en si misma "pd.pivot_table()" con la diferencia de que ésta última recibe el DF como parámetro.
**Parámetros:**
- data: Cuando se utiliza la función directamente de pandas.
- values: Nombre de la columna o columnas (lista) que rellenarán la tabla a partir de la función de agregación.
- index: Nombre de la columna donde se tomarán los valores para crear los indices del DataFrame resultante.
- columns: Nombre de la columna donde se tomarán los valores las nuevas columnas del DataFrame resultante.
- aggfunc: Función de agregación a aplicar.

```py
import pandas as pd
df = pd.read_csv("/content/drive/MyDrive/Curso de Python para Ciencia de Datos/Walmart_Sales.csv")

# Crear una tabla pivote con el promedio de ventas semanales por tienda y fecha
tabla_pivote = df.pivot(index='Date', columns='Store', values='Weekly_Sales')
print(tabla_pivote)
```
### Fusión de da DataFrames [(Menú)](#python-para-ciencia-de-datos)
Lo mecanísmo para hacer una funsión de datos, en pandas son similares a la forma de hacer los joins en sql, por lo qué dejare algunos ejemplos.
```py
import pandas as pd

# DataFrame 1
df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie']
})
print("DataFrame 1:")
print(df1)

# DataFrame 2
df2 = pd.DataFrame({
    'id': [3, 4, 5],
    'score': [85, 90, 95]
})
print("\nDataFrame 2:")
print(df2)

# DataFrame 3
df3 = pd.DataFrame({
    'name': ['Alice', 'David', 'Eve'],
    'age': [24, 30, 28]
})
print("\nDataFrame 3:")
print(df3)


merged_df = pd.merge(df1, df2, on='id', how='inner')
print("\nMerge (Inner Join) on 'id':")
print(merged_df)


concatenated_df = pd.concat([df1, df2], ignore_index=True)
print("\nConcatenated DataFrame (Rows):")
print(concatenated_df)


inner_joined_df = pd.merge(df1, df3, on='name', how='inner')
print("\nInner Join on 'name':")
print(inner_joined_df)
```
### Series Temporales [(Menú)](#python-para-ciencia-de-datos)
El manejo de series temporales en **Pandas** es crucial para trabajar con datos relacionados con el tiempo, como precios de acciones, datos meteorológicos o eventos registrados por tiempo. Pandas ofrece herramientas poderosas para trabajar con fechas y tiempos de manera eficiente.

**Aspectos principales de series temporales en Pandas**

1. **Fechas como índice (`DatetimeIndex`)**  
   Es común usar fechas como índice para facilitar la manipulación y análisis.

2. **Conversión de cadenas a fechas (`pd.to_datetime`)**  
   Pandas permite convertir cadenas a objetos de fecha para trabajar con ellos.

3. **Generación de rangos de fechas (`pd.date_range`)**  
   Crear secuencias de fechas con una frecuencia específica.

4. **Resampleo**  
   Agrupar datos por frecuencia (diaria, semanal, mensual, etc.).

5. **Seleccionar datos por rango de fechas**  
   Filtrar datos en intervalos temporales.

**Ejemplo práctico**

```python
import pandas as pd
import numpy as np

# Generar un rango de fechas
dates = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')

# Crear un DataFrame con datos aleatorios
data = pd.DataFrame({
    'date': dates,
    'value': np.random.randint(10, 100, len(dates))
})

# Establecer la columna 'date' como índice
data.set_index('date', inplace=True)
print("DataFrame con índice de fechas:")
print(data)

# Filtrar datos por rango de fechas
filtered_data = data['2023-01-03':'2023-01-07']
print("\nDatos filtrados entre '2023-01-03' y '2023-01-07':")
print(filtered_data)

# Resamplear datos (frecuencia semanal)
weekly_data = data.resample('W').mean()
print("\nDatos resampleados (promedio semanal):")
print(weekly_data)

# Agregar una nueva columna con el mes
data['month'] = data.index.month
print("\nDataFrame con columna adicional del mes:")
print(data)
```
## Matplotlib [(Menú)](#python-para-ciencia-de-datos)
### Intro Matplotlib [(Menú)](#python-para-ciencia-de-datos)
Nos permite visualizar los datos de manera efectiva, esta biblioteca fue creada por John Hunter, en 2003,
Es una estandar para la creación de gráficos en varias diciplinas, desde gráficos de ciencias elementales hasta finanzas.

[Link de Referencia: MATPLOTLIB](https://matplotlib.org/stable/install/index.html)

**Para instalar la librería**

*En entornos como googlecolab estás librerías ya están instaladas*
```sh
pip install matplotlib 
```
**Importación de modulos principales**
```py
import numpy as np
import matplotlib.pyplot as plt
```

- **Gráfico de líneas:** Es útil para una varible en relación al tiempo. Es especialmente útil para identificar patrones, o estacionalidad en relación a una tendencia.

*Ejemplo básico:*
```py
mes = np.array(["Enero","Febrero","Marzo","Abril"])
ventas = np.array([25,27,62,21])

# Configurar el tamaño de gráfico
#Configurar las dimensiones
plt.figure(figsize=(8,6))

# Crear el gráfico
# Determinando las dimensiones debemos definir el tipo de gráfico
# De acuerdo a un plano cartesiano
# plt.plot(x,y) equivalente a los dos arrays definidos
plt.plot(mes,ventas, marker='o', color='blue')

#Caracterísiticas del gráfico
plt.title('Ventas mensaules de un producto')
plt.xlabel('Meses')
plt.ylabel('Ventas en billones de unidades')
```
![EjmploMPL](/A01.PyDS/A01.PyDS-Imagenes/EjemploMPL.png)

- **Gráfico de dispersión:** Este gráfico es principalmente útil para relacionar dos varibles y su relación, cómo varibales independientes, ejemplo temperatura y la presión en una línea de producción y ver la tendencia de producción, el flujo, la calidad quimíca del resultado etc etc.

```py
#Horas de Estudio
HE = np.array([1,2,3,4,5,6,7,8,9,9])
#Calificación
C = np.array([10,15,25,34,66,44,57,67,77,90])

# Crear el gráfico
# 
plt.scatter(HE,C,color='blue')

#Caracterísiticas del gráfico
plt.title('Hora de estudio contra Nota')
plt.xlabel('Horas de Estudio')
plt.ylabel('Calificación')
```
![EjmploMPL](/A01.PyDS/A01.PyDS-Imagenes/EjemploMPL2.png)

**Nota importante:** Una forma de resumir un punto importante, para cada gráfico ya sea plt.plot() o plt.scatter(), los array que se utilicen seben mantener el mismo tamaño, es decir la misma cantidad de elementos.
### Personalización de Gráficos [(Menú)](#python-para-ciencia-de-datos)
La personalización de gráficos nos ayuda a qué nuestra información sea más clara, llamativa, informativa y atractiva. Un ejemplo de lo qué podemos personalizar es:

- Titulos
- Etiquetas
- Leyendas
- Estilos de línea
- Marcadores
- Etc

**Ejemplo de gráfico de dispersión**
```py
import numpy as np
import matplotlib.pyplot as plt
#Horas de Estudio
HE = np.array([2,3,4,5,6,7,8])
#Calificación
Estudiante001 = np.array([10,15,25,44,66,74,97])
Estudiante002 = np.array([11,13,30,60,46,74,87])

# Gráfico de dispersión de dos estudiantes
plt.scatter(HE, Estudiante001, marker='o', color='red', linestyle='-', label='Estudiante 1')
plt.scatter(HE, Estudiante002, marker='s', color="blue", linestyle="--", label='Estudiante 1')

#Caracterísiticas del gráfico
plt.title('Hora de estudio contra Nota de dos estudiantes')
plt.xlabel('Horas de Estudio')
plt.ylabel('Calificación')
```
![EjmploMPL](/A01.PyDS/A01.PyDS-Imagenes/EjemploMPL3.png)

**Ejemplo de gráfico de líneas mismos valores**
```py
import numpy as np
import matplotlib.pyplot as plt
#Horas de Estudio
HE = np.array([2,3,4,5,6,7,8])
#Calificación
Estudiante001 = np.array([10,15,25,44,66,74,97])
Estudiante002 = np.array([11,13,30,60,46,74,87])

# Gráfico de dispersión de dos estudiantes
plt.plot(HE, Estudiante001, marker='o', color='red', linestyle='-', linewidth = 2, label='Estudiante 1')
plt.plot(HE, Estudiante002, marker='s', color="blue", linestyle="--", linewidth = 2, label='Estudiante 1')

#Caracterísiticas del gráfico
plt.title('Hora de estudio contra Nota de dos estudiantes')
plt.xlabel('Horas de Estudio')
plt.ylabel('Calificación')
```
![EjmploMPL](/A01.PyDS/A01.PyDS-Imagenes/EjemploMPL4.png)
### Gráficos de Barras y Diagramas de Pastel [(Menú)](#python-para-ciencia-de-datos)
Los gráficos de barra y de pastel se utilizan para representar datos categóricos de manera vizual y compresible

**Crear un gráfico de barra**
```py
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))

# Datos de ejemplo
cat = ["PA","PB","PC"]
ventas = [10,20,30]

# Crear el gráfico de barras
plt.bar(cat, ventas, color="skyblue", label="Ventas")

# Caracterísiticas del gráfico
plt.title("Ventas por Categoría mensual")
plt.xlabel("Categoría")
plt.ylabel("Ventas")
```
![Gráfico de barra](/A01.PyDS/A01.PyDS-Imagenes/EjemploMPL5.png)

**Hay ciertas personalizaciones para cada gráfico**
```py
import matplotlib.pyplot as plt

plt.figure(figsize=(12,7.5))

# Datos de ejemplo
cat = ["PA","PB","PC"]
ventas = [10,20,30]

# Crear el gráfico de barras
plt.bar(cat, ventas, color="skyblue", label="Ventas")

#Anotación para destacar un punto en específico
plt.annotate("Máximo de ventas", xy=("PC",30.5), arrowprops= dict(facecolor="black", shrink=0.25), xytext=(1,25))

# Caracterísiticas del gráfico
plt.title("Ventas por Categoría mensual")
plt.xlabel("Categoría")
plt.ylabel("Ventas")

#plt.legend()

plt.show()
```
![Gráfico de barra](/A01.PyDS/A01.PyDS-Imagenes/EjemploMPL6.png)

**Gráfico horizontal**
```py
import matplotlib.pyplot as plt

plt.figure(figsize=(12,7.5))

# Datos de ejemplo
cat = ["PA","PB","PC"]
ventas = [10,20,30]

# Crear el gráfico de barras
plt.barh(cat, ventas, color="skyblue", label="Ventas")

# Caracterísiticas del gráfico
plt.title("Ventas por Categoría mensual")
plt.xlabel("Categoría")
plt.ylabel("Ventas")

#plt.legend()

plt.show()
```
![Gráfico de barra](/A01.PyDS/A01.PyDS-Imagenes/EjemploMPL7.png)

Es recomendable usar diagramas de pastel cuando se tienen pocas categorías con diferencias claves en al proporción.

```py
# prompt: crea una gráfica de pastel 

import matplotlib.pyplot as plt

plt.figure(figsize=(12,10))

# Datos de ejemplo para el gráfico de pastel
Productos = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

# Crear el gráfico de pastel
plt.pie(sizes, labels=Productos, autopct='%2.2f%%', startangle=110)

# Agregar un título al gráfico
plt.title('Gráfico de Pastel de Ejemplo')

#Asegurar qué sea un círculo
plt.axis('equal')

# Mostrar el gráfico
plt.show()      
```
![Diagrama de Pastel](/A01.PyDS/A01.PyDS-Imagenes/EjemploMPL8.png)
### Histograma y Boxplot [(Menú)](#python-para-ciencia-de-datos)
Son las herramientas gráficas para ver la distribución estadística de un conjunto de datos, es una herramienta que permite analizar la variabilidad para identificar posibles anomalias. 

**Generar números randon de acuerdo a una desviación estadística dada**

```py
import numpy as np
import matplotlib.pyplot as plt

datos = np.random.normal(170, 10, 200)
print(datos)
```

**Algunas funcionalidades de los histogramas de plt**
```py
import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo (reemplaza con tus datos)
datos = np.random.normal(170, 10, 200)

# Crear el histograma
plt.hist(datos, 
         bins=20,         # Número de bins (intervalos)
         range=(140, 200), # Rango de valores a mostrar
         density=False,    # Normalizar el histograma (área total = 1)
         weights=None,     # Pesos para cada valor
         cumulative=False, # Histograma acumulativo
         bottom=None,      # Valor de desplazamiento vertical
         histtype='bar',   # Tipo de histograma ('bar', 'barstacked', 'step', 'stepfilled')
         align='mid',      # Alineación de las barras ('left', 'mid', 'right')
         orientation='vertical', # Orientación del histograma ('vertical', 'horizontal')
         rwidth=0.9,       # Ancho relativo de las barras (0-1)
         log=False,        # Escala logarítmica en el eje y
         color="salmon", # Usar colores suaves para cada barra
         label='Datos',     # Etiqueta de la leyenda
         alpha=0.9         # Transparencia de las barras
         )

# Personalizar el gráfico
plt.title('Histograma de Datos', fontsize=16)  # Título del gráfico
plt.xlabel('Valores', fontsize=12)            # Etiqueta del eje x
plt.ylabel('Frecuencia', fontsize=12)          # Etiqueta del eje y
plt.grid(True, linestyle='--', alpha=0.5)      # Agregar una cuadrícula
plt.legend(loc='upper right')                  # Mostrar la leyenda
plt.xticks(np.arange(140, 201, 10))            # Personalizar los ticks del eje x
plt.yticks(np.arange(0, 60, 5))                # Personalizar los ticks del eje y

# Mostrar el gráfico
plt.show()
```
![Histograma](/A01.PyDS/A01.PyDS-Imagenes/EjemploMPL11.png)

**Boxplot**

Boxplot o diagramas de caja son gráficos que resumen la información de los histogramas, ¿Qué es un Boxplot?
Un boxplot, o diagrama de caja, es una herramienta visual utilizada en el análisis exploratorio de datos para resumir la distribución de un conjunto de datos. Este gráfico representa la mediana, los cuartiles y los posibles valores atípicos, proporcionando una visión rápida de la dispersión y la asimetría de los datos.

Componentes de un Boxplot:

- Box (Caja): Representa el rango intercuartil (IQR), que incluye el 50% central de los datos. Los bordes de la caja indican el primer cuartil (Q1) y el tercer cuartil (Q3).
- Median (Mediana): Indica el valor central de los datos, dividiendo el conjunto en dos partes iguales.
- Whiskers (Bigotes): Extienden desde los cuartiles hasta los valores mínimos y máximos dentro de 1.5 veces el IQR. Ayudan a identificar la extensión de los datos sin incluir los valores atípicos.
- Outliers (Valores Atípicos): Representan los valores que se encuentran fuera del rango de los bigotes.

El boxplot es especialmente útil para comparar la distribución de los datos entre diferentes grupos o categorías y para identificar rápidamente anomalías o valores extremos en un conjunto de datos.

El boxplot es una herramienta poderosa para el análisis exploratorio de datos, permitiendo a los analistas visualizar rápidamente la distribución de los datos y detectar valores atípicos. Su capacidad para resumir la información clave de un conjunto de datos en un formato visual compacto lo hace ideal para comparar distribuciones entre diferentes grupos o categorías.

Al integrar boxplots en el análisis de datos, se puede obtener una comprensión más profunda de las características subyacentes de los datos, facilitando la toma de decisiones informadas y la identificación de patrones significativos.

[Boxplots documentación](https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html)

```py
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Polygon

# Fixing random state for reproducibility
np.random.seed(19680801)

# fake up some data
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))

fig, axs = plt.subplots(2, 3)

# basic plot
axs[0, 0].boxplot(data)
axs[0, 0].set_title('basic plot')

# notched plot
axs[0, 1].boxplot(data, notch=True)
axs[0, 1].set_title('notched plot')

# change outlier point symbols
axs[0, 2].boxplot(data, sym='gD')
axs[0, 2].set_title('change outlier\npoint symbols')

# don't show outlier points
axs[1, 0].boxplot(data, sym='')
axs[1, 0].set_title("don't show\noutlier points")

# horizontal boxes
axs[1, 1].boxplot(data, sym='rs', orientation='horizontal')
axs[1, 1].set_title('horizontal boxes')

# change whisker length
axs[1, 2].boxplot(data, sym='rs', orientation='horizontal', whis=0.75)
axs[1, 2].set_title('change whisker length')

fig.subplots_adjust(left=0.08, right=0.98, bottom=0.05, top=0.9,
                    hspace=0.4, wspace=0.3)

# fake up some more data
spread = np.random.rand(50) * 100
center = np.ones(25) * 40
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
d2 = np.concatenate((spread, center, flier_high, flier_low))
# Making a 2-D array only works if all the columns are the
# same length.  If they are not, then use a list instead.
# This is actually more efficient because boxplot converts
# a 2-D array into a list of vectors internally anyway.
data = [data, d2, d2[::2]]

# Multiple box plots on one Axes
fig, ax = plt.subplots()
ax.boxplot(data)

plt.show()
```

![Gráfico de barra](/A01.PyDS/A01.PyDS-Imagenes/EjemploMPL9.png)
![Gráfico de barra](/A01.PyDS/A01.PyDS-Imagenes/EjemploMPL10.png)

Para generar valores random que puedan ser reproducibles para diversos modelos, se utilizar un comando que nos permite establecer reproducibilidad en valores generados de manera aleatoria.

```py
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(27)

# Datos de ejemplo para tres grupos de edades
edades_grupo1 = np.random.normal(25, 6, 50)  # Grupo 1: Media 25, desviación estándar 6
edades_grupo2 = np.random.normal(35, 7, 60)  # Grupo 2: Media 35, desviación estándar 7
edades_grupo3 = np.random.normal(45, 12, 70)  # Grupo 3: Media 45, desviación estándar 12

datos = [edades_grupo1, edades_grupo2, edades_grupo3]

# Crear el boxplot
plt.figure(figsize=(10, 6))  # Ajustar el tamaño de la figura
plt.boxplot(datos, 
            notch=True,       # Mostrar muescas en las cajas
            sym='x',          # Símbolo para los valores atípicos
            vert=True,        # Orientación vertical (True) u horizontal (False)
            whis=1.5,         # Longitud de las líneas de bigote (factor de la IQR)
            patch_artist=True, # Rellenar las cajas con color
            showmeans=True,    # Mostrar la media con un símbolo
            labels=['Grupo 1 (20-29)', 'Grupo 2 (30-39)', 'Grupo 3 (40-49)'], #Etiquetas personalizadas   
```
![BoxPlot](/A01.PyDS/A01.PyDS-Imagenes/EjemploMPL12.png)
### Series de tiempo y fechas [(Menú)](#python-para-ciencia-de-datos)

Representación de cambios de una variables en el tiempo.

```py
import pandas as pd                 # Manejo de datos en formato DataFrame.
import numpy as np                  # Operaciones numéricas.
import matplotlib.pyplot as plt     # Creación de gráficos.
from matplotlib.dates import DateFormatter  # Formateo de fechas.

# Crear un rango de fechas mensual de 12 meses comenzando en enero de 2023.
fechas = pd.date_range(start='2023-01-01', periods=100, freq='M')

# Generar 12 valores aleatorios entre 1000 y 5000 para representar ventas.
ventas = np.random.randint(1000, 5000, size=100)

# Crear un DataFrame con las fechas y las ventas.
data = pd.DataFrame({'Fecha': fechas, 'Ventas': ventas})

# Configurar la figura y su tamaño.
plt.figure(figsize=(12, 6))  # Establece las dimensiones del gráfico (ancho x alto en pulgadas).

# Crear un gráfico de línea con opciones personalizables.
plt.plot(
    data['Fecha'],            # Eje X: las fechas.
    data['Ventas'],           # Eje Y: las ventas.
    marker='o',               # Marcador en cada punto ('o' para círculo, otros: 's', '^', 'd', etc.).
    linestyle='-',            # Estilo de la línea ('-' para continua, '--' para discontinua, etc.).
    linewidth=2,              # Grosor de la línea.
    color='green',             # Color de la línea (puedes usar nombres o códigos hexadecimales como '#FF5733').
    markerfacecolor='red',    # Color de relleno de los marcadores.
    markeredgecolor='black',  # Color del borde de los marcadores.
    markersize=8,             # Tamaño de los marcadores.
    label='Ventas Mensuales', # Etiqueta para la leyenda.
    alpha=0.8                 # Transparencia de la línea (1 es opaco, 0 es completamente transparente).
)

# Configurar el título del gráfico con estilo adicional.
plt.title(
    'Análisis de Ventas Mensuales',  # Texto del título.
    fontsize=16,                     # Tamaño de fuente.
    fontweight='bold',               # Grosor de la fuente ('normal', 'bold', etc.).
    color='darkblue'                 # Color del texto.
)

# Etiqueta del eje X con personalización.
plt.xlabel(
    'Fecha',               # Texto de la etiqueta.
    fontsize=12,           # Tamaño de fuente.
    fontstyle='italic',    # Estilo de la fuente ('normal', 'italic', etc.).
    color='darkgreen'      # Color del texto.
)

# Etiqueta del eje Y con personalización.
plt.ylabel(
    'Ventas',              # Texto de la etiqueta.
    fontsize=12,           # Tamaño de fuente.
    fontstyle='italic',    # Estilo de la fuente.
    color='darkgreen'      # Color del texto.
)

# Personalizar las marcas (ticks) del eje X.
plt.xticks(
    rotation=45,           # Rotación de las etiquetas.
    fontsize=10,           # Tamaño de fuente.
    color='gray'           # Color de las etiquetas.
)

# Personalizar las marcas (ticks) del eje Y.
plt.yticks(
    fontsize=10,           # Tamaño de fuente.
    color='gray'           # Color de las etiquetas.
)

# Agregar una cuadrícula al gráfico.
plt.grid(
    True,                  # Mostrar la cuadrícula.
    linestyle='--',        # Estilo de la línea de la cuadrícula ('-', '--', etc.).
    linewidth=0.5,         # Grosor de las líneas de la cuadrícula.
    alpha=0.7              # Transparencia de la cuadrícula.
)

# Mostrar una leyenda en el gráfico.
plt.legend(
    loc='upper left',      # Posición de la leyenda ('best', 'upper right', 'lower left', etc.).
    fontsize=10,           # Tamaño de fuente de la leyenda.
    frameon=True,          # Mostrar un marco alrededor de la leyenda.
    shadow=True,           # Agregar sombra al marco.
    facecolor='lightyellow', # Color de fondo del marco.
    edgecolor='black'      # Color del borde del marco.
)

# Ajustar los márgenes alrededor del gráfico.
plt.tight_layout()

# Mostrar el gráfico final.
plt.show()

```

![MPL13](/A01.PyDS/A01.PyDS-Imagenes/EjemploMPL13.png)

**Ventas acumuladas**

```py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Establecer semilla para reproducibilidad
np.random.seed(42)

# Crear un rango de fechas mensual de 12 meses comenzando en enero de 2023.
fechas = pd.date_range(start='2023-01-01', periods=12, freq='M')

# Generar 12 valores aleatorios entre 1000 y 5000 para representar ventas mensuales.
ventas_mensuales = np.random.randint(1000, 5000, size=12)

# Calcular la suma acumulada de las ventas.
ventas_acumuladas = np.cumsum(ventas_mensuales)

# Crear un DataFrame con las fechas, ventas mensuales y ventas acumuladas.
data = pd.DataFrame({
    'Fecha': fechas,
    'Ventas Mensuales': ventas_mensuales,
    'Ventas Acumuladas': ventas_acumuladas
})

# Configurar la figura y su tamaño.
plt.figure(figsize=(12, 6))

# Crear un gráfico de línea para las ventas acumuladas con personalización.
plt.plot(
    data['Fecha'],               # Eje X: fechas.
    data['Ventas Acumuladas'],   # Eje Y: ventas acumuladas.
    marker='o',                  # Marcador en cada punto ('o' para círculo).
    linestyle='-',               # Estilo de la línea.
    linewidth=2,                 # Grosor de la línea.
    color='teal',                # Color de la línea.
    markerfacecolor='orange',    # Color de relleno de los marcadores.
    markeredgecolor='black',     # Color del borde de los marcadores.
    markersize=8,                # Tamaño de los marcadores.
    label='Ventas Acumuladas',   # Etiqueta para la leyenda.
    alpha=0.8                    # Transparencia de la línea.
)

# Configurar el título del gráfico.
plt.title(
    'Suma Acumulada de Ventas Mensuales',  # Texto del título.
    fontsize=16,                          # Tamaño de fuente.
    fontweight='bold',                    # Grosor de la fuente.
    color='darkblue'                      # Color del texto.
)

# Etiqueta del eje X.
plt.xlabel(
    'Fecha',              # Texto de la etiqueta.
    fontsize=12,          # Tamaño de fuente.
    fontstyle='italic',   # Estilo de la fuente.
    color='darkgreen'     # Color del texto.
)

# Etiqueta del eje Y.
plt.ylabel(
    'Ventas Acumuladas',  # Texto de la etiqueta.
    fontsize=12,          # Tamaño de fuente.
    fontstyle='italic',   # Estilo de la fuente.
    color='darkgreen'     # Color del texto.
)

# Rotar las etiquetas del eje X.
plt.xticks(
    rotation=45,          # Rotación de las etiquetas.
    fontsize=10,          # Tamaño de fuente.
    color='gray'          # Color de las etiquetas.
)

# Personalizar las marcas (ticks) del eje Y.
plt.yticks(
    fontsize=10,          # Tamaño de fuente.
    color='gray'          # Color de las etiquetas.
)

# Agregar una cuadrícula al gráfico.
plt.grid(
    True,                 # Mostrar la cuadrícula.
    linestyle='--',       # Estilo de la línea de la cuadrícula.
    linewidth=0.5,        # Grosor de las líneas de la cuadrícula.
    alpha=0.7             # Transparencia de la cuadrícula.
)

# Mostrar una leyenda en el gráfico.
plt.legend(
    loc='upper left',     # Posición de la leyenda.
    fontsize=10,          # Tamaño de fuente de la leyenda.
    frameon=True,         # Mostrar un marco alrededor de la leyenda.
    shadow=True,          # Agregar sombra al marco.
    facecolor='lightyellow',  # Color de fondo del marco.
    edgecolor='black'     # Color del borde del marco.
)

# Ajustar los márgenes alrededor del gráfico.
plt.tight_layout()

# Mostrar el gráfico final.
plt.show()
```
![MPL14](/A01.PyDS/A01.PyDS-Imagenes/EjemploMPL14.png)
### Layouts Avanzados [(Menú)](#python-para-ciencia-de-datos)
GridSpec es una clase de Matplotlib que permite personalizar y organizar diseños complejos de subgráficos en una cuadrícula flexible. Proporciona control detallado sobre la posición y el tamaño relativo de cada subgráfico dentro de la figura, definiendo filas, columnas y espacios intermedios. Es especialmente útil cuando se necesitan configuraciones no uniformes o cuando se deben ajustar subgráficos a diferentes proporciones o tamaños específicos.

```py
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np

# Crear datos para los gráficos
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)
data = np.random.randn(1000)

# Configurar el layout con GridSpec
fig = plt.figure(figsize=(12, 8))  # Tamaño de la figura
gs = GridSpec(3, 3, figure=fig)    # Crear una cuadrícula de 3x3

# Gráfico 1: Línea (ocupa la primera fila completa)
ax1 = fig.add_subplot(gs[0, :])  # Primera fila, todas las columnas
ax1.plot(x, y, label='Seno', color='blue')
ax1.plot(x, z, label='Coseno', color='red', linestyle='--')
ax1.set_title('Gráfico de Líneas')
ax1.legend()
ax1.grid(True)

# Gráfico 2: Dispersión (scatter) (en la segunda fila, primera columna)
ax2 = fig.add_subplot(gs[1, 0])  # Segunda fila, primera columna
ax2.scatter(x, y, c='green', alpha=0.7, edgecolor='black')
ax2.set_title('Gráfico de Dispersión')
ax2.set_xlabel('Eje X')
ax2.set_ylabel('Eje Y')

# Gráfico 3: Histograma (en la segunda fila, segunda columna)
ax3 = fig.add_subplot(gs[1, 1])  # Segunda fila, segunda columna
ax3.hist(data, bins=20, color='purple', alpha=0.7)
ax3.set_title('Histograma')
ax3.set_xlabel('Valores')
ax3.set_ylabel('Frecuencia')

# Gráfico 4: Barras (en la segunda fila, tercera columna)
categorias = ['A', 'B', 'C', 'D']
valores = [5, 7, 3, 8]
ax4 = fig.add_subplot(gs[1, 2])  # Segunda fila, tercera columna
ax4.bar(categorias, valores, color='orange', alpha=0.9)
ax4.set_title('Gráfico de Barras')
ax4.set_xlabel('Categorías')
ax4.set_ylabel('Valores')

# Gráfico 5: Mapa de calor (en la tercera fila, ocupa toda la fila)
matriz = np.random.rand(10, 10)
ax5 = fig.add_subplot(gs[2, :])  # Tercera fila, todas las columnas
heatmap = ax5.imshow(matriz, cmap='coolwarm', aspect='auto')
ax5.set_title('Mapa de Calor')
fig.colorbar(heatmap, ax=ax5, orientation='horizontal', pad=0.2)

# Ajustar el espacio entre subgráficos
plt.tight_layout()

# Mostrar la figura final
plt.show()
```
![MTL15](/A01.PyDS/A01.PyDS-Imagenes/EjemploMPL15.png)
## Proyecto personal [Menú](#python-para-ciencia-de-datos)



```py
```

```py
```

```py
```
