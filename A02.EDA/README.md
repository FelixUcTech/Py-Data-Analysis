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


## Análisis Bivariado

## Análisis multivariado




```py

```
```py

```
```py

```
```py

```
```py

```
```py

```
```py

```
```py

```
```py

```
```py

```
```py

```
```py

```
```py

```
```py

```
