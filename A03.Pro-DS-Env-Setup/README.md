# Pro DS Env Setup (Professional Data Science Environment Setup)
- [Introducción](#introducción-menú)
- [DS-Workflow-Templates](#ds-workflow-templates-menú)
    - [¿Qué son y porque utilizar plantillas de proyectos?](#qué-son-y-porque-utilizar-plantillas-de-proyectos-menú)
    - [Cookiecutter](#cookiecutter-menú)
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

**Ahora haremos los siguientes pasos para poner en línea nuestro gestor de plantillas**

1. El primer comando es **conda config --add channels conda-forge**. Este comando agrega el canal "conda-forge" a la configuración de conda, lo que permite buscar paquetes en ese canal al instalar software, como Cookiecutter. Esto es esencial, ya que algunos paquetes, incluidos los que necesitas para ciencia de datos, están disponibles en este canal específico. Asegúrate de familiarizarte con este tipo de comandos para gestionar eficientemente tus entornos y paquetes en Conda. **¿Por qué se añade este canal?** Porque cookiecutter se encuentra en este mismo canal, por lo cual la gestión de librerías es eficiente en dicho canal de gestión de software.

```sh
conda config --add channels conda-forge
```

2. El segundo comando que utiliza el profesor para instalar Cookiecutter es **conda create --name cookiecutter-personal cookiecutter=1.7.3**. Este comando crea un nuevo ambiente de conda llamado **cookiecutter-personal** (igual qué la carpeta creada) y especifica que se debe instalar la versión 1.7.3 de Cookiecutter. Esto es útil para mantener la consistencia de las versiones de los paquetes en tus proyectos de ciencia de datos. Al crear ambientes separados, puedes evitar conflictos entre diferentes proyectos y sus dependencias. ¿Qué versión usar cual es el criterio? **Elige la versión más reciente de Cookiecutter compatible con tus herramientas y requisitos del proyecto. Consulta la documentación oficial de Cookiecutter o su página en PyPI para verificar la versión estable más reciente y leer las notas de cambios. Prioriza consistencia: usa la misma versión en proyectos compartidos o según las guías del curso/proyecto.** [documentación oficial de Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/).

```sh
conda create --name cookiecutter-personal cookiecutter=1.7.3
```

## Manjeo de archivos en Python [Menú](#pro-ds-env-setup-professional-data-science-environment-setup)

## Ejemplo Práctico [Menú](#pro-ds-env-setup-professional-data-science-environment-setup)
