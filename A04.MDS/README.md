# Missing-Data-Strategies
- [Introducción](#introducción-menú)
    - [Operaciones con valores faltantes](#operaciones-con-valores-faltantes-menú)
    - [Conociendo datasets para manejo de datos faltantes](#conociendo-datasets-para-manejo-de-datos-faltantes-menú)
- [Manipulación inicial de Valores Faltantes](#manipulación-inicial-de-valores-faltantes-menú)
- [Busqueda de relaciones de Valores Faltantes](#busqueda-de-relaciones-de-valores-faltantes-menú)
- [Tratamiento de Valores Faltantes](#tratamiento-de-valores-faltantes-menú)

## Introducción [Menú](#missing-data-strategies)
### Operaciones con valores faltantes [Menú](#missing-data-strategies)
Los datos faltantes puede determinar resultados erroneos en cualquier análisis planteado. Por lo cual aprender a tratar los datos faltantes o determinar si son necesarios o no, es importante en cada análisis de datos.

**¿Qué pasa con la siguiente operación?**

![VF1](/A04.MDS/A04.MDS-Imagenes/VF1.png)

**Para el caso donde no sabemos ¿Qué procede?**

![VF1](/A04.MDS/A04.MDS-Imagenes/VF2.png)

- Primer caso: Otro valor faltante
- Segundo caso: Un warning, no opera como debería
- Tercer caso: Un error de copilación

**Diferentes algoritmo diferentes resultado:**

![VF1](/A04.MDS/A04.MDS-Imagenes/VF3.png)

![VF1](/A04.MDS/A04.MDS-Imagenes/VF4.png)

Con la información anterior se entiende implicitamente que dependiendo el entorno, lenguaje, librería, edición, etc del sofware donde estemos desarrollando será la forma en que el mismo interprete qué es un valor faltante y qué no, para ello nos apoyaremos del [DeepNote](https://deepnote.com/workspace/platzi-escuela-datos-83832097-f136-43ff-b38d-abaa022e8ec7/project/datos-faltantes-694a3d08-7f18-421d-9e2f-c2820a79680e/notebook/553972dde60446379c4205c75670d7ad), para evaluar el tipo de dato no reconocido para diferentes herramientas de manipulación de datos.

**Con Python**
```py
print(
    None or True,          # Evalúa el operador lógico `or`. Si el primer valor (None) es falso, retorna el segundo valor (True).
    None or False,         # Evalúa el operador lógico `or`. Si el primer valor (None) es falso, retorna el segundo valor (False).
    None == None,          # Compara si `None` es igual a `None`. Esto siempre es verdadero.
    None is None,          # Compara si `None` es el mismo objeto (identidad). Siempre es verdadero, ya que `None` es único.
    # None + True,         # Esto causaría un error porque `None` no es un número y no se puede sumar a `True` (que es igual a 1).
    # None / False,        # Esto causaría un error porque `False` equivale a 0, y dividir por cero no está permitido.
    type(None),            # Devuelve el tipo del objeto `None`, que es `<class 'NoneType'>`.
    sep="\n"               # Imprime cada valor en una nueva línea.
)
```
**Con NumPY**
```py
print(
    np.nan or True,      # Evalúa el operador lógico `or`. En Python, `np.nan` no se evalúa como un valor booleano explícito False, por lo que se considera True en contextos booleanos. Por lo tanto, devuelve `np.nan` y no el segundo valor (`True`).
    np.nan == np.nan,    # Compara si `np.nan` es igual a `np.nan`. Por definición, en NumPy y en IEEE 754, `nan` no es igual a ningún valor, ni siquiera a otro `nan`. Retorna `False`.
    np.nan is np.nan,    # Verifica si `np.nan` es el mismo objeto en memoria que otro `np.nan`. Como todos los `np.nan` se refieren al mismo objeto en NumPy, esto retorna `True`.
    np.nan / 2,          # Realiza una operación matemática con `np.nan`. Cualquier operación con `nan` resulta en `nan`. Por lo tanto, retorna `nan`.
    type(np.nan),        # Devuelve el tipo de `np.nan`. Es un valor especial del tipo flotante (`<class 'float'>`).
    np.isnan(np.nan),    # Verifica si `np.nan` es un `nan`. La función `np.isnan` retorna `True` si el valor es un `nan`.
    sep="\n"             # Imprime cada valor en una nueva línea para mayor claridad.
)
```
**Con Pandas**
```py
# Crear un DataFrame desde un diccionario utilizando diferentes tipos de valores faltantes
test_missing_df = pd.DataFrame.from_dict(
    data=dict(
        x=[0, 1, np.nan, np.nan, None],  # La columna 'x' contiene valores numéricos, NaN (de NumPy) y None (de Python)
        y=[0, 1, pd.NA, np.nan, None]    # La columna 'y' contiene valores numéricos, NA (de pandas), NaN y None
    )
)

# Muestra el DataFrame con valores faltantes
print("DataFrame con valores faltantes:")
print(test_missing_df)

# Verificar valores faltantes en todo el DataFrame utilizando `isna()`
# Retorna un DataFrame booleano donde `True` indica valores faltantes (NaN, NA, None)
print("\n¿Hay valores faltantes en el DataFrame? (usando .isna()):")
print(test_missing_df.isna())

# Verificar valores faltantes en todo el DataFrame utilizando `isnull()`
# `isnull()` es equivalente a `isna()` en pandas.
print("\n¿Hay valores faltantes en el DataFrame? (usando .isnull()):")
print(test_missing_df.isnull())

# Verificar valores faltantes solo en la columna 'x' utilizando `.isna()`
# Retorna una Serie booleana donde `True` indica valores faltantes.
print("\n¿Hay valores faltantes en la columna 'x'? (usando .isna()):")
print(test_missing_df.x.isna())

# Crear una Serie con un valor numérico y un valor faltante (NaN)
print("\nSerie con un valor numérico y un valor faltante:")
print(pd.Series([1, np.nan]))
```
### Conociendo datasets para manejo de datos faltantes [Menú](#missing-data-strategies)

**Nota:** Normalmente es buena práctica cargar las librerías antes de ejecutar funciones en deepnotes o en jupyternotebooks.

**Importar librerías**
```py
import janitor
import matplotlib.pyplot as plt
import missingno
import numpy as np
import pandas as pd
import pyreadr
import seaborn as sns
import session_info
import upsetplo
```
**Cargar los conjuntos de datos de deepnote**
```py
pima_indians_diabetes_url = "https://nrvis.com/data/mldata/pima-indians-diabetes.csv"
```
**Dentro de un ambiente de JupyterNotebooks para ejecutar comandos de terminal, se utiliza el signo de exclamación al inicio !**
```sh
# Descargar un archivo desde una URL y guardarlo con un nombre específico en el directorio ./data.
# -O: Especifica el nombre y la ubicación donde se guardará el archivo.
# {pima_indians_diabetes_url}: Representa una variable que contiene la URL del archivo a descargar.
# -q: Activa el modo silencioso, evitando que se muestren mensajes de progreso.
!wget -O ./data/pima-indians-diabetes.csv {pima_indians_diabetes_url} -q
```
**Pandas directamente te permite cargar los archivos desde una url, pero es una buena práctica cargar los archivos en local**
```py
diabetes_df = pd.read_csv(
    filepath_or_buffer="./data/pima-indians-diabetes.csv", # or pima_indians_diabetes_url
    sep=",",
    names=[
        "pregnancies",
        "glucose",
        "blood_pressure",
        "skin_thickness",
        "insulin",
        "bmi",
        "diabetes_pedigree_function",
        "age",
        "outcome",
    ]
)
```
**El código descarga datasets en formato .rda desde una URL base, los guarda localmente, los convierte en DataFrames usando pyreadr, y los organiza en un diccionario. Luego, registra los DataFrames como variables locales, examina sus dimensiones, estructura y detecta valores faltantes en uno de ellos.**
```py
# Definir la URL base donde se encuentran los archivos de datos
base_url = "https://github.com/njtierney/naniar/raw/master/data/"

# Lista de nombres de los datasets que queremos descargar
datasets_names = ("oceanbuoys", "pedestrian", "riskfactors")

# Extensión de los archivos de los datasets
extension = ".rda"

# Crear un diccionario vacío para almacenar los DataFrames después de leerlos
datasets_dfs = {}

# Iterar sobre cada nombre de dataset
for dataset_name in datasets_names:
    # Construir el nombre completo del archivo
    dataset_file = f"{dataset_name}{extension}"
    
    # Definir la ruta local donde se guardará el archivo
    dataset_output_file = f"./data/{dataset_file}"
    
    # Construir la URL completa del archivo a descargar
    dataset_url = f"{base_url}{dataset_file}"
    
    # Descargar el archivo desde la URL y guardarlo localmente
    !wget -q -O {dataset_output_file} {dataset_url}
    
    # Leer el archivo .rda descargado usando pyreadr y obtener el DataFrame correspondiente
    datasets_dfs[f"{dataset_name}_df"] = pyreadr.read_r(dataset_output_file).get(dataset_name)

# Ver las claves (nombres) del diccionario que contiene los DataFrames
datasets_dfs.keys()

# Actualizar las variables locales con las claves y valores del diccionario datasets_dfs
locals().update(**datasets_dfs)

# Limpiar las variables no necesarias
del datasets_dfs

# Obtener información sobre las dimensiones de los DataFrames
oceanbuoys_df.shape, pedestrian_df.shape, riskfactors_df.shape, diabetes_df.shape

# Mostrar información básica sobre el DataFrame `riskfactors_df`
riskfactors_df.info()

# Verificar valores faltantes en el DataFrame `riskfactors_df`
riskfactors_df.isna()
```

**Documentación**
- [kaggle-Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- [naniar](https://github.com/njtierney/naniar)
- [R](https://cran.r-project.org/web/packages/naniar/vignettes/getting-started-w-naniar.html)
### 


## Manipulación inicial de Valores Faltantes [Menú](#missing-data-strategies)

## Busqueda de relaciones de Valores Faltantes [Menú](#missing-data-strategies)

## Tratamiento de Valores Faltantes [Menú](#missing-data-strategies)

