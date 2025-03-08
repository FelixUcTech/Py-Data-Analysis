# Pro DS Env Setup (Professional Data Science Environment Setup)
- [Introducción](#introducción-menú)
- [DS-Workflow-Templates](#ds-workflow-templates-menú)
    - [¿Qué son y porque utilizar plantillas de proyectos?](#qué-son-y-porque-utilizar-plantillas-de-proyectos-menú)
    - [Cookiecutter](#cookiecutter-menú)
    - [Crear plantillas de proyecto personalizadas](#crear-plantillas-de-proyecto-personalizadas-menú)
    - [Hooks](#hooks-menú)
- [Manjeo de archivos en Python](#manjeo-de-archivos-en-python-menú)
    - [Manejo de rutas](#manejo-de-rutas-menú)
    - [Manejador de rutas](#manejador-de-rutas-menú)
    - [Pathlib](#pathlib-menú)
    - [Manejo de rutas del sistema: PyFilesystem2](#manejo-de-rutas-del-sistema-pyfilesystem2-menú)
- [Ejemplo Práctico](#ejemplo-práctico-menú)

## Introducción [Menú](#pro-ds-env-setup-professional-data-science-environment-setup)
- El alcance de estas notas son, ayudar en la creación de plantillas en entorno de trabajo personalizados para el análisis.
- Aprender a desarrollar proyectos autocontenibles y multiplataforma.

## DS-Workflow-Templates [Menú](#pro-ds-env-setup-professional-data-science-environment-setup)
### ¿Qué son y porque utilizar plantillas de proyectos? [Menú](#pro-ds-env-setup-professional-data-science-environment-setup)
![¿Qué son las plantillas de proyecto?](/A03.Pro-DS-Env-Setup/A03-Pro-DS-Env-Setup-Imagenes/PlantillasQueSon.png)

Un ejemplo grande de qué son estás plantillas, es cuando definimos la estructura de carpetas, donde se guardará la data, dónde vamos a gestionar el codigo principal, configuraciones perifericas, si es una base de datos las notas principales de configaración del motor de base de datos, etc, estás se pueden hacer prediseñadas.

![¿Por qué utilizarlas?](/A03.Pro-DS-Env-Setup/A03-Pro-DS-Env-Setup-Imagenes/whyusethem.png)
###  Cookiecutter [Menú](#pro-ds-env-setup-professional-data-science-environment-setup)
**¿Qué es Cookiecuter?:** Es un herramienta multiplataforma qué te permite crear plantillas.

![Cookiecutter](/A03.Pro-DS-Env-Setup/A03-Pro-DS-Env-Setup-Imagenes/cookiecuter.png)

**¿Cómo funciona?:**

![Cookiecutter](/A03.Pro-DS-Env-Setup/A03-Pro-DS-Env-Setup-Imagenes/cookiecuter1.png)

Detrás de Cookiercutter se encuentra jinja, es similar a python por lo cual ayuda para escribir plantillas para las personas que ya usan python como lenguaje de programación.

**Documentación**
- [cookiecutter-data-science](https://cookiecutter-data-science.drivendata.org/)
- [cookiecutter.readthedocs](https://cookiecutter.readthedocs.io/en/1.7.2/README.html)
- [repo-curso](https://github.com/platzi/curso-entorno-avanzado-ds)

Para crear un cookiecutter personal, es preferible desarrollarlo en una carpeta para darle el espacio definido al proyecto de la plantilla ejemplo, la nombraremos **"cookiecutter-personal"**.

**Notas:** Puedes usar herramientas como venv (entornos virtuales de Python) o simplemente instalar los paquetes globalmente, aunque esto último no es recomendado para evitar conflictos. No es estrictamente necesario usar conda como entorno si ya manejas bien tu terminal de Ubuntu.

**Opción sin conda**
1. Crear un habiente virtual en nuestra carpeta del pryecto
```sh
python3 -m venv venv
```
2. Activar el ambiente virtual
```sh
source venv/bin/activate
```
3. Dargarcar cookiecutter.
```sh
pip install cookiecutter==1.7.3
```

4. Para exportar la configuración y mantener tu entorno organizado, en lugar de usar **conda env export**, usaremos pip freeze para exportar las dependencias:

```sh
pip freeze > requirements.txt
```

4. 1. Cualquier persona que quiera replicar tu entorno puede usar el archivo **requirements.txt** y crear un entorno virtual con el siguiente comando: 
```sh
python3 -m venv nuevo-entorno
source nuevo-entorno/bin/activate
pip install -r requirements.txt
```

**¿Por qué hacerlo?**
- Exportar dependencias asegura que puedas compartir o recrear tu entorno en cualquier máquina.
- Aunque conda env export es exclusivo de conda, pip freeze logra lo mismo en entornos creados con venv.

5. Clonar la estructura del proyecto
```sh
cookiecutter https://github.com/platzi/curso-entorno-avanzado-ds --checkout cookiecutter-personal-platzi
```

**Otra forma de hacerlo:**

**Ahora haremos los siguientes pasos para poner en línea nuestro gestor de plantillas**

1. El primer comando es **conda config --add channels conda-forge**. Este comando agrega el canal "conda-forge" a la configuración de conda, lo que permite buscar paquetes en ese canal al instalar software, como Cookiecutter. Esto es esencial, ya que algunos paquetes, incluidos los que necesitas para ciencia de datos, están disponibles en este canal específico. Asegúrate de familiarizarte con este tipo de comandos para gestionar eficientemente tus entornos y paquetes en Conda. **¿Por qué se añade este canal?** Porque cookiecutter se encuentra en este mismo canal, por lo cual la gestión de librerías es eficiente en dicho canal de gestión de software.
```sh
conda config --add channels conda-forge
```

2. El segundo comando se utiliza para instalar Cookiecutter es **conda create --name cookiecutter-personal cookiecutter=1.7.3**. Este comando crea un nuevo ambiente de conda llamado **cookiecutter-personal** (igual qué la carpeta creada) y especifica que se debe instalar la versión 1.7.3 de Cookiecutter. Esto es útil para mantener la consistencia de las versiones de los paquetes en tus proyectos de ciencia de datos. Al crear ambientes separados, puedes evitar conflictos entre diferentes proyectos y sus dependencias. ¿Qué versión usar cual es el criterio? **Elige la versión más reciente de Cookiecutter compatible con tus herramientas y requisitos del proyecto. Consulta la documentación oficial de Cookiecutter o su página en PyPI para verificar la versión estable más reciente y leer las notas de cambios. Prioriza consistencia: usa la misma versión en proyectos compartidos o según las guías del curso/proyecto.** [documentación oficial de Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/).
```sh
conda create --name cookiecutter-personal cookiecutter=1.7.3
```

3. Activar el ambiente en conda.
```sh
conda activate cookiecutter-personal
```

4. Definir donde estará el ambiente
```sh
conda env export --from-history --file enviroment.yml
```

5. Clonar la estructura del proyecto
```sh
cookiecutter https://github.com/platzi/curso-entorno-avanzado-ds --checkout cookiecutter-personal-platzi
```
### Crear plantillas de proyecto personalizadas [Menú](#pro-ds-env-setup-professional-data-science-environment-setup)
Partiendo de la creación de una carpeta, dentro de ella se declaran algunas cosas basicas de un proyecto como:

Al final esta estructura definida va a guardar la estructura que se defina y también los errores, por lo cual es bueno ser cuidadoso con dicha estructura y definiciones.

- [{{cookiecutter.project_slug}}](/A03.Pro-DS-Env-Setup/Creación%20de%20plantilla/{{%20cookiecutter.project_slug%20}}/)
    - data
    - notebooks
    - READMe.m
    - etc

Muchos valores del templet que desarrolles pueden ser variados, por lo cual podemos definirlo mediante el doble {{}}, ejemplo de esto esta en [README.md](/A03.Pro-DS-Env-Setup/Creación%20de%20plantilla/README.md), donde definimos el algunos campos que se llenarán al incio de general la plantilla.

Entodos lados pueden andar declarando alias con cookiecutter que al momento de ejecutar para generar una estructura basada en tu template se podran remplazar por el usuario, pero un archivo .json se declaran las varibles por default, para este ejemplo no es la acepción, [Varibles por defaul](/A03.Pro-DS-Env-Setup/Creación%20de%20plantilla/cookiecutter.json)

Siguiendo el ejemplo el el punto anterior la carpeta definida como [Creación de plantilla](/A03.Pro-DS-Env-Setup/Creación%20de%20plantilla/), sería el equivalente al link del repo, pero esta vez el despliegue sería local en vez de traerlo de una plantilla en línea.
### Hooks [Menú](#pro-ds-env-setup-professional-data-science-environment-setup)
Los hooks, también llamados ganchos, son scripts que permiten extender las funcionalidades de Cookiecutter, ejecutándose antes (pre-gen) o después (post-gen) de la generación de una plantilla de datos. Estos hooks pueden utilizarse para validar entradas del usuario, modificar archivos generados, instalar dependencias o configurar el entorno automáticamente. Al estar escritos en Python o en cualquier otro lenguaje compatible con el sistema operativo, ofrecen gran flexibilidad para personalizar la estructura y el comportamiento de los proyectos generados, mejorando la automatización y estandarización en entornos de desarrollo.

[Ejemplo](/A03.Pro-DS-Env-Setup/Creación%20de%20plantilla/cookiecutter.json)

[Hooks](/A03.Pro-DS-Env-Setup/hooks/)

## Manjeo de archivos en Python [Menú](#pro-ds-env-setup-professional-data-science-environment-setup)
### Manejo de rutas [Menú](#pro-ds-env-setup-professional-data-science-environment-setup)
Considerar que en multiples ocaciones la rutas no son compatible entre sistemas opertativos, es decir, que la forma de llegar a un directorio es diferente en cada carpeta por lo cual la sintaxis no es la misma, esto para la consulta en terminal.

![MAP](/A03.Pro-DS-Env-Setup/A03-Pro-DS-Env-Setup-Imagenes/MAP001.png)

Un problema común en el manejo de rutas es la incompatibilidad entre los sistemas de archivos de distintos sistemas operativos, como Windows, macOS, Linux o WSL. Por ejemplo, Windows usa el backslash (\) en sus rutas de archivos, mientras que los demás utilizan el forward slash (/). Esta diferencia puede generar errores al escribir rutas de forma manual en código que debe ejecutarse en múltiples plataformas. Para solucionar esto, se recomienda usar la biblioteca os.path o pathlib en Python, ya que estas herramientas manejan automáticamente las diferencias de sintaxis según el sistema operativo, garantizando compatibilidad y portabilidad en los scripts.
### Manejador de rutas [Menú](#pro-ds-env-setup-professional-data-science-environment-setup)
El **manejador de rutas `os`** en Python se refiere a la biblioteca **`os`**, que proporciona funciones para interactuar con el sistema operativo y manejar rutas de archivos de manera compatible entre diferentes sistemas operativos. A través del módulo **`os.path`**, se pueden realizar operaciones sobre rutas de archivos y directorios, independientemente de si el código se ejecuta en Windows, Linux o macOS.

Algunas funciones clave de `os.path` son:
- **`os.path.join()`**: Permite construir rutas de archivos de manera segura y compatible con el sistema operativo. Combina componentes de rutas utilizando el separador adecuado (`/` o `\`).
- **`os.path.exists()`**: Verifica si una ruta de archivo o directorio existe en el sistema de archivos.
- **`os.path.abspath()`**: Obtiene la ruta absoluta de un archivo o directorio a partir de una ruta relativa.
- **`os.path.basename()`**: Extrae el nombre de un archivo a partir de una ruta completa.
- **`os.path.dirname()`**: Obtiene el directorio de una ruta, excluyendo el nombre del archivo.

El módulo **`os`** permite que el código sea más portátil, ya que maneja automáticamente las diferencias en las rutas entre sistemas operativos, evitando problemas de compatibilidad y simplificando la escritura de código que funcione en cualquier entorno.

```py
import os

# Ruta de ejemplo
ruta_relativa = "carpeta/subcarpeta/archivo.txt"

# Unir rutas de manera segura
ruta_completa = os.path.join("home", "usuario", ruta_relativa)
print("Ruta completa:", ruta_completa)

# Verificar si la ruta existe
existe = os.path.exists(ruta_completa)
print("La ruta existe:", existe)

# Obtener la ruta absoluta
ruta_absoluta = os.path.abspath(ruta_completa)
print("Ruta absoluta:", ruta_absoluta)

# Obtener el nombre del archivo
nombre_archivo = os.path.basename(ruta_completa)
print("Nombre del archivo:", nombre_archivo)

# Obtener el directorio de la ruta
directorio = os.path.dirname(ruta_completa)
print("Directorio:", directorio)
```
### Pathlib [Menú](#pro-ds-env-setup-professional-data-science-environment-setup)
**Pathlib** es un módulo en Python que proporciona una interfaz orientada a objetos para trabajar con rutas de archivos y directorios. A diferencia de `os.path`, que utiliza funciones basadas en cadenas, `pathlib` permite manipular rutas utilizando objetos que representan esas rutas, lo que hace el código más limpio y fácil de leer. Este módulo también maneja automáticamente las diferencias de sintaxis entre sistemas operativos, como el uso de barras invertidas en Windows y barras normales en otros sistemas. Además, permite realizar operaciones como la creación de directorios, la comprobación de existencia de archivos y la combinación de rutas de forma más intuitiva.

```python
from pathlib import Path

# Ruta de ejemplo
ruta = Path("carpeta/subcarpeta/archivo.txt")

# Unir rutas de manera segura
ruta_completa = Path("home") / "usuario" / ruta
print("Ruta completa:", ruta_completa)

# Verificar si la ruta existe
existe = ruta_completa.exists()
print("La ruta existe:", existe)

# Obtener la ruta absoluta
ruta_absoluta = ruta_completa.resolve()
print("Ruta absoluta:", ruta_absoluta)

# Obtener el nombre del archivo
nombre_archivo = ruta_completa.name
print("Nombre del archivo:", nombre_archivo)

# Obtener el directorio de la ruta
directorio = ruta_completa.parent
print("Directorio:", directorio)
```
### Manejo de rutas del sistema: PyFilesystem2 [Menú](#pro-ds-env-setup-professional-data-science-environment-setup)
La **librería `fs`** en Python es una biblioteca que proporciona una interfaz unificada y coherente para interactuar con sistemas de archivos, tanto locales como remotos. Permite manejar archivos y directorios de manera fácil, sin preocuparse por los detalles específicos de cada sistema operativo o tipo de almacenamiento. Esta librería soporta operaciones como lectura, escritura, copia, eliminación y navegación de directorios, y puede trabajar con sistemas de archivos virtuales como **FTP**, **SFTP**, **WebDAV**, entre otros. `fs` abstrae las diferencias entre estos sistemas de archivos, lo que facilita el desarrollo de aplicaciones que necesitan interactuar con distintos tipos de almacenamiento.

Ejemplo de uso básico:

```python
from fs import open_fs

# Abrir un sistema de archivos local
fs = open_fs('osfs://')

# Listar archivos en el directorio actual
print(fs.listdir('/'))

# Crear un nuevo archivo y escribir en él
with fs.open('/nuevo_archivo.txt', 'w') as file:
    file.write("Hola, mundo!")

# Leer el archivo recién creado
with fs.open('/nuevo_archivo.txt', 'r') as file:
    print(file.read())

# Cerrar el sistema de archivos
fs.close()
```
[Documentación](https://docs.pyfilesystem.org/en/latest/introduction.html)

## Ejemplo Práctico [Menú](#pro-ds-env-setup-professional-data-science-environment-setup)+

[Documentación](https://github.com/drivendata/cookiecutter-data-science)

[Documentación](https://github.com/jvelezmagic/cookiecutter-conda-data-science)