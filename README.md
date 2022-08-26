# Proyecto de Inteligencia Artificial

Deteccion de armas en imagenes.

- El modelo entrenado se encuentra en la carpeta net.

# Guía de instalación

### Entorno Virtual

Se necesita un entorno virtual, en el caso de contar con más de una versión de python especificar python3:

```
python -m venv <env-name>
```

Activar dicho entorno creado:

#### Windows

```
<env-name>\Scripts\activate
```

#### Linux

```
source <env-name>/bin/activate
```

Debe aparecer en el terminal/consola el nombre del entorno virtual entre paréntesis:

```
(<env-name>)
```

### Dependencias

Las dependencias están reunidas en el archivo [requirements](requirements.txt), basta con ejecutar:

```
(<env-name>) pip install -r requirements.txt
```

# Despliegue

**Luego** de instalar el proyecto se puede desplegar al ejecutar:

```
python manage.py runserver
```

Y listo, el proyecto se encuentra activo en el puerto 8000.

# Colaboradores

```
Xavier Carlier
Kevin Cevallos
Jeffrey Prado
```
