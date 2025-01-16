# Missing-Data-Strategies
- [Introducción](#introducción-menú)
    - [Operaciones con valores faltantes](#operaciones-con-valores-faltantes-menú)
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

Con la información anterior se entiende implicitamente que dependiendo el entorno, lenguaje, librería, edición, etc del sofware donde estemos desarrollando será la forma en que el mismo interprete qué es un valor faltnate y qué no, para ello nos apoyaremos del [DeepNote](https://deepnote.com/workspace/platzi-escuela-datos-83832097-f136-43ff-b38d-abaa022e8ec7/project/datos-faltantes-694a3d08-7f18-421d-9e2f-c2820a79680e/notebook/553972dde60446379c4205c75670d7ad), para evaluar el tipo de dato no reconocido para diferentes herramientas de manipulación de datos.

**CON PYHTON**
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



## Manipulación inicial de Valores Faltantes [Menú](#missing-data-strategies)

## Busqueda de relaciones de Valores Faltantes [Menú](#missing-data-strategies)

## Tratamiento de Valores Faltantes [Menú](#missing-data-strategies)

