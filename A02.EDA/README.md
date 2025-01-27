# Análisis Exploratorio de Datos
- [Preliminares](#preliminares-menú)
    - [Intro](#intro-menú)
    - [¿Qué razones tenemos para comenzar un análisis exploratorio de datos?](#qué-razones-tenemos-para-comenzar-un-análisis-exploratorio-de-datos)
    - [Tipos de análisis de datos](#tipos-de-análisis-de-datos-menú)
    - [Tipos de datos y análisis de variables](#tipos-de-datos-y-análisis-de-variables-menú)
    - [Herramientas en el análisis exploratorio de datos](#herramientas-en-el-análisis-exploratorio-de-datos-menú)
    - 

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
- [Deepnote](Curso-EDA-Communication-c92bae1e-ca3b-47c5-b028-6a9a99949ed3)
### Conjutno de Datos [Menú](#análisis-exploratorio-de-datos)

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
### Validación


## Análisis Univariado 

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
```py

```
```py

```
```py

```
```py

```
