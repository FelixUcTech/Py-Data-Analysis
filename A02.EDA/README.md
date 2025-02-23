# Análisis Exploratorio de Datos
- [Herrami](Herramientas y Tecnologías Utilizadas)
- [Preliminares](#preliminares-menú)
    - [Intro](#intro-menú)
    - [¿Qué razones tenemos para comenzar un análisis exploratorio de datos?](#qué-razones-tenemos-para-comenzar-un-análisis-exploratorio-de-datos)
    - [Tipos de análisis de datos](#tipos-de-análisis-de-datos-menú)
    - [Tipos de datos y análisis de variables](#tipos-de-datos-y-análisis-de-variables-menú)
    - [Herramientas en el análisis exploratorio de datos](#herramientas-en-el-análisis-exploratorio-de-datos-menú)
    - [Conjunto de Datos](#conjunto-de-datos-menú)
    - [Recolección de datos](#recolección-de-datos-limpieza-y-validación--menú)
    - [Validación](#validación-menú)
- [Análisis Univariado](#análisis-univariado-menú)
    - [Variable Categórica: Conteos y proporciones](#variable-categórica-conteos-y-proporciones-menú)
    - [Medidas de tendencia central](#medidas-de-tendencia-central-menú)
    - [Medidas de dispersión](#medidas-de-dispersión-menú)
    - [Estadística descriptiva aplicada: distribuciones](#estadística-descriptiva-aplicada-distribuciones-menú)
    - [Teorema del límite central](#teorema-del-límite-central-menú)
- [Análisis Bivariado](#análisis-univariado-menú)
    - [Establecer relaciones](#establecer-relaciones-menú)
    - [Gráficos de violín y boxplots](#gráficos-de-violín-y-boxplots-menú)
    - [Matrices de correlación](#matrices-de-correlación-menú)
    - [Análisis de regresión simple](#análisis-de-regresión-simple-menú)
- [Análisis multivariado](#análisis-multivariado-menú)
    - [Regresión multiple](#regresión-multiple-menú)
    - [Regresión logística](#regresión-logística-menú)
    - [¿Qué hacer cuando tenemos muchas varibles?](#qué-hacer-cuando-tenemos-muchas-varibles-menú)

## Herramientas y Tecnologías Utilizadas [Menú](#análisis-exploratorio-de-datos)

### **Bibliotecas de Python**
- Seaborn
- Pandas
- EmpiricalDist

### **Entornos de Desarrollo**
- Deepnote
- Visual Studio Code

### **Herramientas de Terminal y Sistemas**
- Terminal de Ubuntu




## Preliminares [Menú](#análisis-exploratorio-de-datos)
### Intro [Menú](#análisis-exploratorio-de-datos)

¿Qué es el análisis exploratorio de datos? o como sus siglas en ingles nos permiten abreviar, EDA (Exploratory Data Analysis).

![EDA](/A02.EDA/A02.EDA-Imagenes/EDA.png)
### ¿Qué razones tenemos para comenzar un análisis exploratorio de datos?

![EDA?](/A02.EDA/A02.EDA-Imagenes/ComoHacerUnEDA.png)

**Motivos**
- Organizar y entender las varibles, identificar:
    - Tipos de varibles
    - Categorías que pertenencen
    - El tipo de análisis que se puede realizar con ellas
- Entender las relaciones
    - Relaciones Varibles - Varibles
    - Relaciones Varible - Gráfico
- Encontrar patrones ocultos
    - Es descrubir cosas que probablemente nadie sabe y qué podrían aportar valor en un futuro.
- Escoger el modelo correcto para la necesidad correcta
    - Hacer un análisis te permite encontrar el modelo correcto para la necesidad correcta.
- Ayudarte a tomar decisiones informadadas

**¿Cuales son los pasos para realizar un análisis exploratorio de datos?**

![5P](/A02.EDA/A02.EDA-Imagenes/5pasos.png)

1. Hazte toda clase de preguntas relacionado al factor creativo que pudiera ayudar a entender mejor el proyecto.
2. Ve observando qué necesitas y qué no tienes claro de como usarlo, y podrás ir acotando el trabajo de tus datos.
3. Categorizar las varibles, determinar el alcance del análisis que puedes hacer con la información qué tienes.
4. ¿Tengo toda la información? ¿Qué podría tratar el estado de mi dataset después de los pasos ya realizados?¿Tengo valores atípicos?¿Cuál es la distribución de los datos?
5. Establecer las relaciones entre los conjuntos de datos, qué pasa si un relación definida es efectada o no por las otras varibles de mi conjunto de datos. ¿Qué significa qué las observaciones se agrupen?¿qué significa el patrón que se observa?

**ESTO PUEDE LLEGAR A SER UN CICLO INFITO**

![5P](/A02.EDA/A02.EDA-Imagenes/5pasos-2.png)

**PERO COMO ANÁLISTA ESTO DEBE TERMINAR EN ALGÚN MOMENTO PARA ENTREGAR VALOR AL CLIENTE**

![5P](/A02.EDA/A02.EDA-Imagenes/5pasos-3.png)

### Tipos de análisis de datos [Menú](#análisis-exploratorio-de-datos)
Sin importar qué tus datos sean muy pequeños o muy bastos, los tipos de análitica que puedes hacer son las siguientes:

![TDA1](/A02.EDA/A02.EDA-Imagenes/TiposDA1.png)

**Ejmplo:**

![TDA1](/A02.EDA/A02.EDA-Imagenes/TiposDA2.png)

Estás estapas no son independientes una de la otra, es más, son dependientes una de la otra, cada etapa depende de qué la anterior se haya hecho correctamente para poder pasar a la siguiente.

![TDA1](/A02.EDA/A02.EDA-Imagenes/TiposDA3.png)
### Tipos de datos y análisis de variables [Menú](#análisis-exploratorio-de-datos)
**¿Qué tipo de datos y cómo clasificarlos?**

![Tipo De Datos](/A02.EDA/A02.EDA-Imagenes/TipoDeDatos.png)

**¿Qué tipo de análisis puedes realizar sobre tus datos?**

![Tipo De Analisis](/A02.EDA/A02.EDA-Imagenes/tipodeanalisis.png)

Por lo general tenemos a encontrar en el campo laboral, análisis multivariado, pero dentro de análisis complejos donde todas las varibles se relacionan es bueno realizar análisis univaridos, parapasar al bivariado, y entender como las varibles van aportando a cada determinada etapa del procesamiento de la información. Y así llegar a un análisis exploratorio de datos que cumpla y pueda dar una respuesta congruente con los datos.
### Herramientas en el análisis exploratorio de datos [Menú](#análisis-exploratorio-de-datos)
**Ejemplos**

![Tools](/A02.EDA/A02.EDA-Imagenes/tools.png)

Al final la herramienta no es tan importante como los resultados que entregues con ella. Multiples herramientas están diseñadas para lenguajes o funciones particulaes, nuestra necesidad presede a la herramienta, por lo qué es importante buscar las herramientas que mejor se adapten a nuestras necesidades, y de ser posible probar más de una.

**Algunos ejemplos de herramientas son**
- [anaconda](https://www.anaconda.com/)
- [sagemaker](https://aws.amazon.com/es/pm/sagemaker/)
- [deepnote](https://deepnote.com/)
- [colab](https://colab.research.google.com/)
- [jupyter](https://jupyter.org/)

**Material de estudio**
- [Deepnote](https://deepnote.com/workspace/FelixUcTech-e21cfe80-6202-41cd-a589-37a0039faa08/project/Curso-EDA-Communication-Duplicate-f6a288f2-b3d9-4fdc-8529-57c8c878547e/notebook/f8020947d6874e2495d776bb9b2926e9)
### Conjunto de Datos [Menú](#análisis-exploratorio-de-datos)

![Preliminar-imagen](/A02.EDA/A02.EDA-Imagenes/Pre-001.png)

Cuando utilizamos datos qué alguien más ya recolecto la estrategía principal es buscar integrarlo al flujo de trabajo principal.

- [palmerpenguins](https://allisonhorst.github.io/palmerpenguins/)
- [Palmer Station](https://pallter.marine.rutgers.edu/)
- [Datos](https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv)

- [Entorno de Práctica](https://deepnote.com/app/felixuctech/Curso-EDA-Communication-Duplicate-f6a288f2-b3d9-4fdc-8529-57c8c878547e?utm_content=f6a288f2-b3d9-4fdc-8529-57c8c878547e)

Normalmente como se muestra en el material de estudio, se debe definir qué son los datos crudos y que son los datos procesados, un punto importante es el procesamiento de datos que puede ser responsabildiad del ingeniero de datos o a su vez del analista por la calidad de la fuente que tenga, pero trabajando con datos procesados se plantea un analisis exploratorio desde el momento que se define así a la base de datos.
### Recolección de datos, limpieza y validación  [Menú](#análisis-exploratorio-de-datos)

![Preliminar-imagen](/A02.EDA/A02.EDA-Imagenes/Pre-002.png)

Entre más alejado el nivel de datos, el efoque de la adquisición de los datos puede que no sea 100% el requerido para nuestro análisis. Es decir, directamente no está asociado directamente a un problema de negocio en particular.

**¿Qué es la validación de datos?**

![Preliminar-imagen](/A02.EDA/A02.EDA-Imagenes/Pre-003.png)

**¿Qué se debe validar para asegurar consistencia?**

![Preliminar-imagen](/A02.EDA/A02.EDA-Imagenes/Pre-004.png)
### Validación [Menú](#análisis-exploratorio-de-datos)
En la validación se trata de responder ciertas preguntas para poder introducirse a la base de datos que se nos presenta, dicha información y comandos con código se presenta en [Deepnote](https://deepnote.com/workspace/FelixUcTech-e21cfe80-6202-41cd-a589-37a0039faa08/project/Curso-EDA-Communication-Duplicate-f6a288f2-b3d9-4fdc-8529-57c8c878547e/notebook/f8020947d6874e2495d776bb9b2926e9), es importante responder con código las siguientes preguntas. 

- ¿Qué tipo de dato son las variables del conjunto de datos?
- ¿Cuántas variables de cada tipo de dato tenemos en el conjunto de datos?
- ¿Cuántas variables y observaciones tenemos en el conjunto de datos?
- ¿Existen valores nulos explícitos en el conjunto de datos?
- De tener observaciones con valores nulos, ¿cuántas tenemos por cada variable?
- ¿Cuántos valores nulos tenemos en total en el conjunto de datos?
- ¿Cuál es la proporción de valores nulos por cada variable?
- ¿Cómo podemos visualizar los valores nulos en todo el conjunto de datos?
- ¿Cuántas observaciones y conteos perderíamos si eliminamos los datos faltantes?

**Otros ejemplos**

- ¿Cuál es la distribución estadística de las variables numéricas (media, mediana, desviación estándar, etc.)?
- ¿Cuáles son los valores únicos y sus conteos para las variables categóricas?
- ¿Existen valores duplicados en el conjunto de datos? De ser así, ¿cuántos?
- ¿Cuál es la correlación entre las variables numéricas del conjunto de datos?
- ¿Qué variables tienen outliers y cómo se distribuyen?
- ¿Cómo se agrupan las observaciones según una o varias variables categóricas?
- ¿Existen patrones de valores faltantes que sean dependientes de otras variables?
- ¿Cómo se distribuyen las observaciones en las variables categóricas más relevantes?
- ¿Cuántas observaciones cumplen con ciertas condiciones específicas (e.g., valores mayores a un umbral)?
- ¿Cuál es la relación entre dos variables específicas, visualizada mediante gráficos como scatterplots o boxplots?

## Análisis Univariado [Menú](#análisis-exploratorio-de-datos)
### Variable Categórica: Conteos y proporciones [Menú](#análisis-exploratorio-de-datos)
Una varible categórica es el ejemplo de la frecuencia en un campo definido.

![AU](/A02.EDA/A02.EDA-Imagenes/AU001.png)

Dentro de esta cetegorización nosotros podemos enriquecer toda está información mediante determinar características para cada una que nos ayuden a entender la información de manera más intuitiva.

![AU](/A02.EDA/A02.EDA-Imagenes/AU002.png)

Una vez categorizada la información podemos obtener ciertas proporciones que nos pueden ser de utilidad ya sea para entender el conjunto de datos o darnos cuenta de las necesidades que tenemos en nuestro set de datos.

![AU](/A02.EDA/A02.EDA-Imagenes/AU003.png)

**Analizando data**

El método ***.describe(include='all')*** es parte de la biblioteca **Pandas**, que se utiliza para analizar y manipular datos en Python.

**¿Qué hace este método?** processed_penguins_df.describe(): Muestra estadísticas descriptivas de las columnas numéricas de un DataFrame. Estas estadísticas incluyen la media, mediana, desviación estándar, valores mínimos y máximos, y percentiles.

include='all': Instruye a Pandas para que muestre estadísticas descriptivas de todas las columnas del DataFrame, incluyendo las categóricas. Para las columnas categóricas, proporciona:

- El número de valores únicos (unique).
- El valor más frecuente (top).
- La frecuencia del valor más frecuente (freq).

 Filas que aparecen en la tabla
count

1. count
    - ¿Qué significa?: Número de valores no nulos en cada columna.
    - ¿Por qué es importante?: Te muestra si faltan datos (es decir, si el total es menor al número total de filas).

2. unique (solo para variables categóricas)
    - ¿Qué significa?: Cantidad de valores únicos en una columna.
    - ¿Por qué es importante?: Sirve para identificar cuántas categorías distintas hay en las variables categóricas.

3. top (solo para variables categóricas)
    - ¿Qué significa?: Valor más frecuente en la columna.
    - ¿Por qué es importante?: Ayuda a encontrar patrones o valores dominantes en los datos.

4. freq (solo para variables categóricas)
    - ¿Qué significa?: Frecuencia (conteo) del valor más frecuente.
    - ¿Por qué es importante?: Te indica cuántas veces aparece la categoría más común.

5. mean (solo para variables numéricas)
    - ¿Qué significa?: Promedio de los valores numéricos.
    - ¿Por qué es importante?: Es una medida central que resume los datos.

6. std (solo para variables numéricas)
    - ¿Qué significa?: Desviación estándar de los valores.
    - ¿Por qué es importante?: Indica cuánto varían los datos respecto a la media.

7. min (solo para variables numéricas)
    - ¿Qué significa?: Valor más pequeño en la columna.
    ¿Por qué es importante?: Te muestra los extremos inferiores de los datos.

8. 25% (primer cuartil)
    - ¿Qué significa?: Valor debajo del cual está el 25% de los datos.
    - ¿Por qué es importante?: Sirve para identificar los datos más bajos en el conjunto.

9. 50% (mediana o segundo cuartil)
    - ¿Qué significa?: Valor central que divide los datos en dos partes iguales.
    - ¿Por qué es importante?: No es afectada por valores atípicos, a diferencia de la media.

10. 75% (tercer cuartil)
    - ¿Qué significa?: Valor debajo del cual está el 75% de los datos.
    - ¿Por qué es importante?: Identifica los valores altos en el conjunto.

11. max (solo para variables numéricas)
    - ¿Qué significa?: Valor más grande en la columna.
    - ¿Por qué es importante?: Muestra los extremos superiores de los datos.


Si solo quisieramos de nuestro DataSet revisar mediante .describe() solamente las varibles númericas lo podemos hacer mediante el método de pandas.

```py
#Varibles númericas
processes_penguins_df.describe(include=[np.number])

#Varibles categóricas
processes_penguins_df.describe(include=object)
```

En pandas es importante definir los objetos a categorías, cuando así lo queremos ya que pandas nos permite hacer cosas diferentes con categorías, la forma de definirlas es la siguiente. 

```py

#Definiendo categorías
proccessed_penguins_df
.astype({
    'species': 'category',
    'island': 'category',
    'sex': 'category',
})
.describe(include='category') #Ya no se podría ejecutar .describe(include=object), correctamente

#Después de ejecutar la siguiente sentencia si se busca nuevamente objeto no se encuentra dado que se definieron los objetos como categorías.

```
La API de Pandas es la interfaz que proporciona la biblioteca Pandas en Python para interactuar con estructuras de datos (como DataFrames y Series) y realizar operaciones como análisis, manipulación y visualización. Es una forma organizada de acceder a los métodos y funciones que ofrece Pandas para trabajar con datos.

El siguiente código utiliza la API de Pandas para realizar un análisis y una visualización:

```python
processed_penguins_df
    .species
    .value_counts()
    .plot(
        kind='bar',
        # color=penguin_color.values()
    )
```

**API (Application Programming Interface)**  
Una API es un conjunto de reglas, definiciones y herramientas que permite que diferentes programas o sistemas se comuniquen entre sí. Es una interfaz que actúa como un intermediario, permitiendo que una aplicación utilice las funciones o datos de otra aplicación sin necesidad de entender su implementación interna.

En términos simples, una API es como un "menú de un restaurante" que te muestra las opciones disponibles (funciones o servicios) y te indica cómo solicitar lo que necesitas, sin tener que saber cómo se prepara la comida en la cocina (la lógica interna del sistema).

**Tipos comunes de APIs:**
- APIs de software: Permiten la interacción entre diferentes programas. Por ejemplo, la API de Pandas en Python para manipular datos.
- APIs web: Usadas para interactuar con servicios en línea a través de la red. Por ejemplo, la API de Twitter para obtener datos de publicaciones.
- APIs de hardware: Permiten que el software controle dispositivos de hardware.  

**Ejemplo en Pandas:**  
En Pandas, la API proporciona métodos y funciones como `.value_counts()`, `.plot()` y `.groupby()` para interactuar con estructuras de datos como DataFrames y Series. Estas funciones son la "interfaz" que permite a los usuarios manipular datos fácilmente, sin preocuparse por los detalles internos de cómo Pandas realiza esas operaciones.
### Medidas de tendencia central [Menú](#análisis-exploratorio-de-datos)
**¿Cúales son?**

![AU](/A02.EDA/A02.EDA-Imagenes/AU004.png)

**Media**  
Promedio aritmético de un conjunto de datos: la suma de todos los valores dividida entre el número total de valores.

```py
#Utilizando pandas
processes_penguins_df.bill_depth_mm.mean()

#Utilizando numpy
np.mean(processes_penguins_df.bill_depth_mm)
```

```py
#Obtener la media de todos los datos númericos
processes_penguins_df.mean()
```
Enteoria ambos casos deben ser el mismo resultado dado que pandas está construido por encima de numpy

**Mediana**  
El valor central en un conjunto de datos ordenado. Si hay un número par de valores, es el promedio de los dos centrales.

```py
#Obtener la mediana de todos los datos númericos
processes_penguins_df.median()
```

**Moda**  
El valor o valores que aparecen con mayor frecuencia en un conjunto de datos.

En la ejecución siguiente, igual aplica para varibles categoricas no solo las númericas como los casos anteriores.
```py
#Obtener la moda de todos los datos númericos
processes_penguins_df.mode()
```

**Media ponderada**  
Promedio que asigna diferentes pesos a los valores:  

$$
\text{Media ponderada} = \frac{\sum (x_i \cdot w_i)}{\sum w_i}
$$  

donde \(x_i\) son los valores y \(w_i\) sus pesos.

**Media armónica**  
Promedio utilizado para tasas o proporciones:  
$$
\text{Media armónica} = \frac{n}{\sum \frac{1}{x_i}}
$$ 
donde \(n\) es el número de valores y \(x_i\) son los valores.

**Media geométrica**  
Promedio que multiplica los valores y toma la raíz \(n\)-ésima:  
$$
\text{Media geométrica} = \sqrt[n]{x_1 \cdot x_2 \cdot \dots \cdot x_n}
$$

Es útil para datos que crecen multiplicativamente, como tasas de interés.
### Medidas de dispersión [Menú](#análisis-exploratorio-de-datos)
**Rango**  
El rango es la diferencia entre el valor máximo y el valor mínimo en un conjunto de datos.  
**Fórmula:**  
$$
\text{Rango} = \text{Valor máximo} - \text{Valor mínimo}
$$

**Rango intercuartílico (IQR)**  
El rango intercuartílico mide la dispersión de un conjunto de datos entre el primer cuartil (Q1) y el tercer cuartil (Q3).  
**Fórmula:**  
$$
\text{IQR} = Q3 - Q1
$$  
Donde:
- \(Q1\) es el primer cuartil (25% de los datos),
- \(Q3\) es el tercer cuartil (75% de los datos).

**Desviación estándar**  
La desviación estándar mide la dispersión o la variabilidad de los datos respecto a su media.  
**Fórmula:**  
$$
\sigma = \sqrt{\frac{\sum (x_i - \mu)^2}{n}}
$$  
Donde:
- \(x_i\) son los valores individuales,
- \(\mu\) es la media del conjunto de datos,
- \(n\) es el número total de datos.


![AU](/A02.EDA/A02.EDA-Imagenes/AU005.png)

![AU](/A02.EDA/A02.EDA-Imagenes/AU006.png)

![AU](/A02.EDA/A02.EDA-Imagenes/AU007.png)

![AU](/A02.EDA/A02.EDA-Imagenes/AU008.png)

**Rango**
El rango no tiene mucho sentido que se aplique para varibles categóricas, dado que su función en principalmente en matemáticas lo cual es en su mayoría númerico o algebráico.

```py
#Límite superior, límite máximo
processed_penguins_df.max(numeric_only=True)
#Límite inferior, límite mínimo
processed_penguins_df.min(numeric_only=True)
```

La diferencia del rango LS  - LI
```py
#¿Cuál es la diferencia del rango?
processed_penguins_df.max(numeric_only=True) - processed_penguins_df.min(numeric_only=True)
```

**Desviación estandar**
```py
#Desviación estandar
processed_penguins_df.std()
```

**Rango Intercuartílico; ¿Para qué sirve el rango intercuartílico (IQR)?**

El rango intercuartílico (IQR) es útil porque mide la dispersión de los datos **centrales** (50% de los valores) y **reduce el impacto de los valores atípicos** (outliers). A diferencia del rango general, el IQR no considera los valores extremos, lo que lo hace una medida más robusta para analizar la variabilidad en los datos.
 Usos principales:
1. **Identificar valores atípicos (outliers):**  
   Se pueden detectar outliers considerando los valores que caen fuera de los límites:
   $$
   \text{Límite inferior} = Q1 - 1.5 \cdot \text{IQR}
   $$
   $$
   \text{Límite superior} = Q3 + 1.5 \cdot \text{IQR}
   $$  
   Los datos fuera de este rango se consideran atípicos.

2. **Comparar dispersión entre conjuntos de datos:**  
   El IQR permite evaluar la variabilidad de los datos centrales en diferentes distribuciones sin que los valores extremos distorsionen la comparación.

3. **Análisis de datos asimétricos:**  
   Como el IQR no depende de supuestos de normalidad, es adecuado para datos que no siguen una distribución normal.

4. **Medición de estabilidad o consistencia:**  
   Si el IQR es pequeño, indica que los datos centrales son más consistentes y están menos dispersos.

En resumen, el IQR es una herramienta clave para explorar la **variabilidad central de los datos** de forma confiable, especialmente en presencia de valores extremos.

**Criterio matemático del rango intercuartílico para detectar y excluir valores atípicos**

El rango intercuartílico (IQR) utiliza un **criterio basado en los límites superior e inferior** que se calculan añadiendo o restando un múltiplo del IQR a los cuartiles \( Q1 \) (primer cuartil) y \( Q3 \) (tercer cuartil). El criterio más común para identificar valores atípicos es el de **1.5 veces el IQR**. Los valores que caen fuera de estos límites se consideran atípicos.
 Fórmulas para los límites:
1. **Límite inferior:**
   $$
   \text{Límite inferior} = Q1 - 1.5 \cdot \text{IQR}
   $$

2. **Límite superior:**
   $$
   \text{Límite superior} = Q3 + 1.5 \cdot \text{IQR}
   $$
 Interpretación:
- Los valores que están **por debajo del límite inferior** o **por encima del límite superior** se consideran **valores atípicos** o **outliers**.
- Este criterio asegura que los datos dentro de los límites contienen aproximadamente el **99.3% de los valores** si los datos siguen una distribución normal, ya que \( \pm 1.5 \cdot \text{IQR} \) abarca la mayor parte de los datos centrales.

Razón detrás de este criterio:
El factor 1.5 está diseñado para ser lo suficientemente amplio como para incluir la mayoría de los datos típicos, pero al mismo tiempo lo suficientemente estricto como para detectar valores que se desvíen considerablemente del rango central. Este enfoque es robusto porque no depende de la media ni de la desviación estándar, que pueden ser influenciadas por valores extremos.

Si un análisis requiere mayor sensibilidad, el factor puede ajustarse, por ejemplo, usando:

$$
3.0 \cdot \text{IQR}
$$

para detectar valores extremadamente atípicos.

**Cálculando el rango intercuartílico**
```py
#Lo cálcula para todos los valores númericos de dataframe
print(processed_penguins_df.quantile(0.75))

print(processed_penguins_df.quantile(0.75)-processed_penguins_df.quantile(0.25))
```

**Todos los cuartiles**
```py
(
    processed_penguins_df
    .quantile(q=[0.75.0.5,0.25])
    .transpose() #Mostrar cuartiles en las columnas de la tabla
    .rename_axis('Varibles')#Columna 1
    .reset_index()
    .assign(
        iqr=lambda df: df[0.75] - df[0.25]
    )
)
```

**¿Cómo visualizar la distribución de una varible?**
```py
# Asumimos que 'processed_penguins_df' es el DataFrame con los datos procesados.

# Crear una figura con 3 subgráficas (1 fila, 3 columnas)
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Especificar las especies
species = processed_penguins_df['species'].unique()

# Para cada especie, graficar un histograma separado
for i, sp in enumerate(species):
    # Filtrar los datos para cada especie
    species_data = processed_penguins_df[processed_penguins_df['species'] == sp]
    
    # Graficar el histograma
    sns.histplot(
        data=species_data,
        x='flipper_length_mm',
        kde=True,  # Para agregar una curva KDE si lo deseas
        ax=axes[i],
        color=sns.color_palette("Set1")[i],  # Colores diferentes para cada especie
        #bins=35
    )

    # Añadir líneas de referencia
    axes[i].axvline(
        x=species_data['flipper_length_mm'].mean(),
        color='red',
        linestyle='dashed',
        linewidth=2,
        label='Mean'
    )
    axes[i].axvline(
        x=species_data['flipper_length_mm'].median(),
        color='blue',
        linestyle='dashed',
        linewidth=2,
        label='Median'
    )
    axes[i].axvline(
        x=species_data['flipper_length_mm'].mode().values[0],
        color='black',
        linestyle='dashed',
        linewidth=4,
        label='Mode'
    )
    axes[i].axvline(
        x=species_data['flipper_length_mm'].quantile(0.25),
        color='yellow',
        linestyle='dashed',
        linewidth=2,
        label='25th Percentile'
    )
    axes[i].axvline(
        x=species_data['flipper_length_mm'].quantile(0.75),
        color='yellow',
        linestyle='dashed',
        linewidth=2,
        label='75th Percentile'
    )
    
    # Títulos y etiquetas
    axes[i].set_title(f"Species: {sp}")
    axes[i].set_xlabel('Flipper Length (mm)')
    axes[i].set_ylabel('Frequency')
    axes[i].legend()

# Ajustar el espacio entre subgráficas
plt.tight_layout()
plt.show()
```

![AU](/A02.EDA/A02.EDA-Imagenes/AU009.png)

![AU](/A02.EDA/A02.EDA-Imagenes/AU010.png)

![AU](/A02.EDA/A02.EDA-Imagenes/AU011.png)
### Estadística descriptiva aplicada: distribuciones [Menú](#análisis-exploratorio-de-datos)
**Función de probabilidad de masa (PMF)**  
Es una función que asigna una probabilidad a cada valor posible de una variable discreta. La probabilidad de que la variable tome un valor específico es dada por esta función:  
$$ P(X = x) = p(x) $$

**Función de distribución acumulada (CDF)**  
Es una función que describe la probabilidad de que una variable aleatoria tome un valor menor o igual a un valor específico. Se calcula sumando las probabilidades de todos los valores anteriores de la variable aleatoria:  
$$ F(x) = P(X \leq x) = \sum_{i=-\infty}^{x} P(X = i) $$

**Función de probabilidad de densidad (PDF)**  
Es una función que describe la probabilidad de que una variable aleatoria continua tome un valor dentro de un rango específico. La probabilidad exacta de que la variable tome un valor específico es cero, pero el área bajo la curva de la función en un intervalo da la probabilidad de que la variable esté en ese intervalo:  
$$ P(a \leq X \leq b) = \int_{a}^{b} f(x) \, dx $$ 
### Funciones de densidad de probabilidad
Dentro de un conjunto de datos qué tenemos, podemos ver mediante la función **Kdeplot** de **seaborn**, una forma continua de una representación de la probabilidad de existencia de un dato en específico en relación al conjunto de datos dado. Algo importante que resaltar es que cada función de cada librería, tiene muchos parámetros que nos pueden ayudar a optener el resultado más próximo a nuestra necesidad, ejemplo es un una constante dentro del método de kdplot, dentro del método se tiene **bw_method** esta constante nos ayuda a que la función se pueda aproxima mejor a la probabilidad de nuestro conjunto de datos.


```py
sns.kdeplot(
    data=processed_penguind_df,
    x="Tamaño de la aleta en mm"
    bw_method=0.1
)
```
### Teorema del límite central [Menú](#análisis-exploratorio-de-datos)
El Teorema del Límite Central establece que, dada una muestra suficientemente grande de variables aleatorias independientes e idénticamente distribuidas, su media muestral seguirá una distribución aproximadamente normal, independientemente de la distribución original de los datos. 

Formalmente, si X₁, X₂, ..., Xₙ son variables aleatorias independientes con media μ y varianza finita σ², entonces la distribución de la media muestral:

$$(X̄ - μ) / (σ / √n)$$

se aproxima a una distribución normal estándar (media 0 y varianza 1) cuando n → ∞. 

Este resultado es fundamental en estadística porque permite aplicar métodos inferenciales basados en la normalidad, incluso cuando la distribución original de los datos no es normal.

**Un ejemplo gráfico de la ley de los grandes números** Un dado con una densidad homogenea en todas las caras de su forma. 

![AU](/A02.EDA/A02.EDA-Imagenes/AU012.png)

![AU](/A02.EDA/A02.EDA-Imagenes/AU013.png)

![AU](/A02.EDA/A02.EDA-Imagenes/AU014.png)

![AU](/A02.EDA/A02.EDA-Imagenes/AU015.png)

![AU](/A02.EDA/A02.EDA-Imagenes/AU016.png)

[Teorema del ímite central](https://www.youtube.com/watch?v=s6w-Z9SyAlA&ab_channel=CodigoMaquina), mejor ejemplificación.

## Análisis Bivariado [Menú](#análisis-exploratorio-de-datos)
### Establecer relaciones [Menú](#análisis-exploratorio-de-datos)
Una representación de dos varibles puede llegar a ser muy interesante en función de número de datos, para ello es importante saber como representarlo.

![AB](/A02.EDA/A02.EDA-Imagenes/AB001.png)

![AB](/A02.EDA/A02.EDA-Imagenes/AB002.png)

![AB](/A02.EDA/A02.EDA-Imagenes/AB003.png)

![AB](/A02.EDA/A02.EDA-Imagenes/AB004.png)

![AB](/A02.EDA/A02.EDA-Imagenes/AB005.png)

Ejemplo de formas de representación de dos varibles, en este caso son dos varibles con una tercer varible categorica para una obervación más intuitiva.

```py
sns.jointplot(  data=processed_penguins_df,
                x='bill_length_mm',
                y='bill_depth_mm',
                palette=penguin_color,
                hue='species'
            )
```

![AB](/A02.EDA/A02.EDA-Imagenes/AB006.png)
### Gráficos de violín y boxplots [Menú](#análisis-exploratorio-de-datos)
```py
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))

sex_colour = {'Male': '#ADD8E6', 'Female': '#FFC0CB'}  # Azul claro y rosa claro


sns.violinplot(
    data=processed_penguins_df,
    x='island',
    y='body_mass_g',
    ax=ax1
)

sns.swarmplot(
    data=processed_penguins_df,
    x='island',
    y='body_mass_g',
    hue='sex',
    palette=sex_colour,
    ax=ax1
)

ax1.set_title('Violin Plot and Swarm Plot')

sns.boxplot(
    data=processed_penguins_df,
    x='island',
    y='body_mass_g',
    hue='sex',
    palette=sex_colour,
    ax=ax2
)

ax2.set_title('Box Plot')

# Ajustar el diseño de la figura
plt.tight_layout()

plt.show()

```

![AB](/A02.EDA/A02.EDA-Imagenes/AB008.png)

```py
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))

sex_colour = {'Male': '#ADD8E6', 'Female': '#FFC0CB'}  # Azul claro y rosa claro


sns.violinplot(
    data=processed_penguins_df,
    x='island',
    y='body_mass_g',
    ax=ax1
)

sns.swarmplot(
    data=processed_penguins_df,
    x='island',
    y='body_mass_g',
    hue='sex',
    palette=sex_colour,
    ax=ax1
)

ax1.set_title('Violin Plot and Swarm Plot')

sns.boxplot(
    data=processed_penguins_df,
    x='island',
    y='body_mass_g',
    hue='sex',
    palette=sex_colour,
    ax=ax2
)

ax2.set_title('Box Plot')

# Ajustar el diseño de la figura
plt.tight_layout()

plt.show()
```
![AB](/A02.EDA/A02.EDA-Imagenes/AB009.png)
### Matrices de correlación [Menú](#análisis-exploratorio-de-datos)
Dos varibles pueden tener una correlación líneal, pero está puede ser perfecta o apenas una correlación pequeña, pero una forma de verlo gráficamente es en la siguiente imagen dónde se aprecia una dispersión despecto a una función de recta, entre más próxima sean las tendencias a la afunción la correlación será mayor.

![AB](/A02.EDA/A02.EDA-Imagenes/AB010.png)

![AB](/A02.EDA/A02.EDA-Imagenes/AB011.png)

![AB](/A02.EDA/A02.EDA-Imagenes/AB012.png)

[Método de optención de corelación líneal](https://www.youtube.com/watch?v=A0OvIcjDUDg&ab_channel=Probabilidadyestad%C3%ADsticaIBelver)
### Análisis de regresión simple [Menú](#análisis-exploratorio-de-datos)

[¿Cuál es la matemática detrás de la regresión lineal?](https://platzi.com/blog/cual-es-la-matematica-detras-de-la-regresion-lineal/)

Una regresión líneal nos permite obtener la función de la recta que determna el cambio en relación con las absisas y las ordenadas, en otras palabras, al tener las funciones de las recta podemos tenerminar independientemente de los grupos de datos que tengamos un parametro comparativo para determinar el estimulo que tiene la relación, ante un cambio en una varible, lo cual con un simple coeficiente de relación es complicado de ver.

```py
# Variables o atributos
mi_index = (
    processed_penguins_df
    .columns
    .slice_indexer(
        'bill_length_mm',
        'body_mass_g'
    )
)
species = processed_penguins_df['species'].value_counts().reset_index()['index']
variables = processed_penguins_df.columns[mi_index]

# Definiendo el grid y el grafico
cols = len(variables)
rows = cols
fig, ax = (
    plt
    .subplots(
        ncols=cols,
        nrows=rows,
        figsize=(20, 10),
        layout='constrained',
        facecolor='none'
    )
)

#Subtitulo de la figura
fig.suptitle('Regresion_Lineales Pinguinos')

# Filas
for i, variable_row in enumerate(variables):

    # Columnas
    for j, variable_col in enumerate(variables):

        # Graficando por especie en cada ax[i][j]
        for specie, group in processed_penguins_df.groupby('species'):
            sns.regplot(
                y=variable_row,
                x=variable_col,
                data=group,
                ax=ax[i][j],
                label=specie,
                color=penguin_color[specie]
            )

        # Parametros en 'comun'
        ax[i][j].grid(True)
        ax[i][j].set_xlabel('')

        # La specie como y_label pero solo en la columna 0
        if j != 0:
            ax[i][j].set_ylabel('')
        else:
            ax[i][j].set_ylabel(f'{variable_row}')

        # Solo titulos en la fila de arriba
        if (i == 0):
            ax[i][j].set_title(variable_col)

        # Solo tick label en la fila de abajo
        if (i != rows - 1):
            ax[i][j].set_xticklabels([])
        if i == j:
            ax[i][j].legend()
```

![AB](/A02.EDA/A02.EDA-Imagenes/AB013.png)


**Limitaciones de la regresión líneal**

![AB](/A02.EDA/A02.EDA-Imagenes/AB014.png)

La regresión no nos dice nada sobre la causualidad, pero existen herramientas para separar las relaciones entre múltiples varibles.




## Análisis multivariado [Menú](#análisis-exploratorio-de-datos)
### Regresión multiple [Menú](#análisis-exploratorio-de-datos)


```python
# Importamos statsmodels.formula.api para utilizar Ordinary Least Squares (OLS)
import statsmodels.formula.api as smf  

# Definimos el modelo de regresión lineal múltiple con Ordinary Least Squares (OLS)
model_2 = (
    smf.ols(
        formula="body_mass_g ~ bill_length_mm + bill_depth_mm ",
        data=processed_penguins_df
    )
    .fit()
)

# Mostramos el resumen del modelo
model_2.summary()
```

**Matemáticas detrás de `smf.ols`**

El método `ols` (Ordinary Least Squares, Mínimos Cuadrados Ordinarios) busca ajustar un modelo lineal de la forma:

$$
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \varepsilon
$$

Donde:
- \( Y \) es la variable dependiente (en este caso, `body_mass_g`).
- \( X_1 \) y \( X_2 \) son las variables predictoras (`bill_length_mm` y `bill_depth_mm`).
- \( \beta_0 \) es la intersección (intercepto).
- \( \beta_1, \beta_2 \) son los coeficientes de regresión que indican el impacto de cada variable predictora.
- \( \varepsilon \) es el término de error.

**Método de Mínimos Cuadrados Ordinarios (OLS)**

OLS minimiza la suma de los errores cuadráticos:

$$
\min_{\beta_0, \beta_1, \beta_2} \sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2
$$

Donde:
$$
\hat{Y}_i = \beta_0 + \beta_1 X_{1i} + \beta_2 X_{2i}
$$

El modelo estima los valores de \( \beta_0, \beta_1, \beta_2 \) usando la siguiente ecuación matricial:

$$
\boldsymbol{\beta} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{Y}
$$

Donde:
- \( \mathbf{X} \) es la matriz de diseño con una columna de unos (para el intercepto) y las columnas de variables predictoras.
- \( \mathbf{Y} \) es el vector de valores observados.
- \( \boldsymbol{\beta} \) es el vector de coeficientes a estimar.

El método `.fit()` ajusta el modelo, estimando \( \beta_0, \beta_1, \beta_2 \) y otros parámetros estadísticos.

**Interpretación del output `model_2.summary()`**

El comando `model_2.summary()` muestra información relevante como:

- **Coeficientes estimados** (\( \beta_0, \beta_1, \beta_2 \)).
- **Errores estándar** de los coeficientes.
- **Valor p** para evaluar la significancia de cada variable.
- **R² y R² ajustado** para medir la calidad del ajuste.
- **Estadísticos de prueba** como la prueba F y t-tests.

**Es importante destacar que esta función puede utilizarse con múltiples variables independientes para predecir una variable dependiente. Sin embargo, esto no garantiza que el modelo sea más preciso. Por ello, es fundamental seleccionar las variables más representativas y relacionadas con la variable dependiente.**

**Por ejemplo, si queremos determinar la cantidad de dientes que tiene una persona y utilizamos como variable independiente el tono de piel, es muy probable que no exista una relación significativa, lo que haría que el modelo fuera poco preciso. En cambio, si usamos como variables independientes la edad y una variable categórica que represente el lugar donde vive, es más probable que encontremos una tasa de cambio razonable en la cantidad de dientes.**

SMF es un paquete en Python utilizado para modelado estadístico, comúnmente empleado en econometría y ciencias sociales. La función `smf.logic()` no existe en la biblioteca Statsmodels (`smf` es el alias común para `statsmodels.formula.api`). Probablemente se refiere a `smf.logit()`, que se usa para la regresión logística binaria.

`smf.logit()` permite modelar relaciones donde la variable dependiente es binaria (0 o 1). Se basa en la siguiente ecuación:

$$
P(Y=1) = \frac{e^{(\beta_0 + \beta_1 X_1 + \beta_2 X_2 + ... + \beta_n X_n)}}{1 + e^{(\beta_0 + \beta_1 X_1 + \beta_2 X_2 + ... + \beta_n X_n)}}
$$

Para utilizar `smf.logit()`, primero se deben importar las bibliotecas necesarias y preparar los datos:

```python
import pandas as pd
import statsmodels.formula.api as smf

# Datos de ejemplo
data = pd.DataFrame({
    'X1': [1, 2, 3, 4, 5, 6],
    'X2': [2, 3, 4, 5, 6, 7],
    'Y': [0, 0, 0, 1, 1, 1]
})

# Modelo de regresión logística
model = smf.logit(formula='Y ~ X1 + X2', data=data).fit()

# Resumen del modelo
print(model.summary())
```

En este ejemplo:
- `formula='Y ~ X1 + X2'` indica que la variable dependiente es `Y` y las variables independientes son `X1` y `X2`.
- `.fit()` ajusta el modelo a los datos.
- `model.summary()` muestra estadísticas del modelo, incluyendo coeficientes y significancia.

Este método es útil para clasificación binaria, evaluación de riesgos y toma de decisiones en modelos predictivos.
### Regresión logística [Menú](#análisis-exploratorio-de-datos)

Explicación:

- Se generan datos aleatorios con dos características (`X1`, `X2`) y una etiqueta binaria `y`.
- Se dividen los datos en entrenamiento (80%) y prueba (20%).
- Se normalizan las características usando `StandardScaler` para mejorar el rendimiento del modelo.
- Se entrena un modelo de regresión logística con `LogisticRegression()` de `sklearn`.
- Se realizan predicciones en el conjunto de prueba.
- Se evalúa el modelo con `accuracy_score`, `confusion_matrix` y `classification_report`.
- Finalmente, se visualizan los datos en un gráfico de dispersión con colores para cada clase.

```py

# Importar bibliotecas necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Generar datos de ejemplo
np.random.seed(42)
n_samples = 1000
X1 = np.random.normal(2, 1, n_samples)
X2 = np.random.normal(-2, 1, n_samples)
y = (X1 + X2 > 0).astype(int)  # Etiqueta binaria

# Convertir los datos en un DataFrame
df = pd.DataFrame({'X1': X1, 'X2': X2, 'y': y})

# Dividir en conjuntos de entrenamiento y prueba
X = df[['X1', 'X2']]
y = df['y']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Estandarizar los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Crear y entrenar el modelo de regresión logística
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Hacer predicciones
y_pred = model.predict(X_test_scaled)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Mostrar resultados
print(f'Accuracy: {accuracy:.2f}')
print('Confusion Matrix:')
print(conf_matrix)
print('Classification Report:')
print(report)

# Visualizar los datos
plt.scatter(df['X1'], df['X2'], c=df['y'], cmap='bwr', alpha=0.5)
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Datos de Clasificación Binaria')
plt.show()
```
### Paradoja de Simpson [Menú](#análisis-exploratorio-de-datos)
**La paradoja de Simpson** es un fenómeno estadístico en el que una tendencia observada en varios grupos desaparece o se invierte cuando los datos se combinan en un solo grupo. Esto ocurre debido a la influencia de una variable oculta o de confusión.

**Ejemplo en Python**

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Crear datos de ejemplo
data = pd.DataFrame({
    'Grupo': ['A']*5 + ['B']*5,
    'Tratamiento': ['Sí', 'No', 'Sí', 'No', 'Sí', 'Sí', 'No', 'Sí', 'No', 'No'],
    'Éxito': [80, 90, 85, 88, 75, 30, 40, 35, 38, 32],
    'Total': [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
})

# Calcular tasas de éxito por grupo
data['Tasa de Éxito'] = data['Éxito'] / data['Total']

# Graficar los resultados
plt.figure(figsize=(8,5))
sns.barplot(x='Grupo', y='Tasa de Éxito', hue='Tratamiento', data=data)
plt.title('Ejemplo de la Paradoja de Simpson')
plt.ylabel('Tasa de Éxito')
plt.show()
```
**Ejemplo visual**

![AM](/A02.EDA/A02.EDA-Imagenes/AM001.png)

![AM](/A02.EDA/A02.EDA-Imagenes/AM002.png)

La paradoja de Simpson es un fenómeno estadístico donde una tendencia observada en múltiples grupos desaparece o se revierte cuando los datos se combinan, debido a la influencia de una variable oculta o de confusión. Esto ocurre porque la distribución de los datos en cada grupo puede afectar la interpretación global, llevando a conclusiones engañosas si no se analizan las relaciones dentro de los subgrupos.
### ¿Qué hacer cuando tenemos muchas varibles? [Menú](#análisis-exploratorio-de-datos)

Cuando tenemos muchas variables en un problema de programación, es fundamental aplicar técnicas de reducción de la dimensionalidad y selección de características para optimizar el rendimiento del modelo o la eficiencia del código. Podemos comenzar analizando la correlación entre variables para eliminar redundancias, usar métodos como PCA (Análisis de Componentes Principales) para transformar los datos en un espacio más compacto o aplicar algoritmos de selección como eliminación recursiva de características (RFE) y Lasso para identificar las más relevantes. Además, en problemas de machine learning, técnicas como ingeniería de características y regularización ayudan a mejorar la interpretabilidad y reducir el sobreajuste. En términos de programación estructurada, una estrategia efectiva es modularizar el código, encapsular variables en estructuras adecuadas (como diccionarios o clases) y usar nombres descriptivos para facilitar su gestión y mantenimiento.

![AM](/A02.EDA/A02.EDA-Imagenes/AM003.png)

[Referencia](https://pmc.ncbi.nlm.nih.gov/articles/PMC2735096/)

t-SNE (t-Distributed Stochastic Neighbor Embedding) es una técnica de reducción de dimensionalidad no lineal utilizada para visualizar datos de alta dimensión en espacios de 2D o 3D, preservando la estructura local de los datos. A diferencia de métodos lineales como PCA, t-SNE convierte las distancias entre puntos en probabilidades y minimiza la diferencia entre distribuciones de similitud en el espacio original y reducido, lo que permite agrupar datos similares de manera más intuitiva. Aunque es útil para exploración de datos y clustering visual, puede ser computacionalmente costoso y sufre de hiperparámetros sensibles, como la "perplejidad", que afecta la distribución de los puntos en el espacio reducido.

![AM](/A02.EDA/A02.EDA-Imagenes/AM004.png)

UMAP (Uniform Manifold Approximation and Projection) es una técnica de reducción de dimensionalidad que preserva tanto la estructura global como local de los datos de alta dimensión, siendo más rápida y escalable que t-SNE. Se basa en principios matemáticos de teoría de grafos y aprendizaje topológico, construyendo un gráfico de vecinos en el espacio original y luego optimizándolo en el espacio reducido para mantener relaciones importantes entre los puntos. UMAP es ampliamente usado en la exploración y visualización de datos, especialmente en machine learning y bioinformática, y es menos sensible a hiperparámetros en comparación con t-SNE, lo que lo hace una opción más eficiente para conjuntos de datos grandes.

![AM](/A02.EDA/A02.EDA-Imagenes/AM005.png)

[Referencia](https://arxiv.org/pdf/1802.03426)

## Recomendación final [Menú](#análisis-exploratorio-de-datos)
**¿Qué quiero mostrar?**

![RF](/A02.EDA/A02.EDA-Imagenes/RF001.png)

![RF](/A02.EDA/A02.EDA-Imagenes/RF002.png)

La exploración de datos es hacerte preguntas.

![RF](/A02.EDA/A02.EDA-Imagenes/RF003.png)

![RF](/A02.EDA/A02.EDA-Imagenes/RF004.png)

![RF](/A02.EDA/A02.EDA-Imagenes/RF005.png)