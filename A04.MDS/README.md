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

## Manipulación inicial de Valores Faltantes [Menú](#missing-data-strategies)

## Busqueda de relaciones de Valores Faltantes [Menú](#missing-data-strategies)

## Tratamiento de Valores Faltantes [Menú](#missing-data-strategies)

