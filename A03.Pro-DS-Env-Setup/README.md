# Pro DS Env Setup (Professional Data Science Environment Setup)
- [Introducción](#introducción-menú)
- [DS-Workflow-Templates](#ds-workflow-templates-menú)
    - [¿Qué son y porque utilizar plantillas de proyectos?](#qué-son-y-porque-utilizar-plantillas-de-proyectos-menú)
    - [Cookiecutter](#cookiecutter-menú)
    - [Crear plantillas de proyecto personalizadas](#crear-plantillas-de-proyecto-personalizadas-menú)
    - [Hooks](#hooks-menú)
- [Manjeo de archivos en Python](#manjeo-de-archivos-en-python-menú)
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
Los hooks o también llamados ganchos, es una herramienta qué puede aplir las capacidades de cookiecutter, estos se ejecutan antes o después de generar la plantilla de datos.


## Manjeo de archivos en Python [Menú](#pro-ds-env-setup-professional-data-science-environment-setup)

## Ejemplo Práctico [Menú](#pro-ds-env-setup-professional-data-science-environment-setup)
