# 3xe.q

Página web simple hecha en Python con Flask.

## Archivos que debes añadir

Coloca tus archivos dentro de la carpeta `static` con estos nombres exactos:

```text
static/Fondo.mp4
static/logo.png
static/logox.png
```

Tu video actual está en:

```text
C:\Users\ezequ\OneDrive\Escritorio\todo\Fondo.mp4
```

Cópialo a la carpeta `static` del proyecto.

## Ejecutar

1. Instala dependencias:

```bash
pip install -r requirements.txt
```

2. Inicia la página:

```bash
python app.py
```

3. Abre en el navegador:

```text
http://localhost:5000
```

## Cambiar el video

Reemplaza este archivo:

```text
static/Fondo.mp4
```

O cambia esta línea en `app.py`:

```html
<source src="{{ url_for('static', filename='Fondo.mp4') }}" type="video/mp4">
```

## Cambiar el logo

Reemplaza este archivo:

```text
static/logo.png
static/logox.png
```

O cambia esta línea en `app.py`:

```html
<img class="logo" src="{{ url_for('static', filename='logo.png') }}" alt="Contenido exclusivo">
```

Si tu logo es `.jpg`, por ejemplo `logo.jpg`, cambia `logo.png` por `logo.jpg`.

La página redirige a:

https://onlyfans.com/exeof

## Diseño actualizado

- El logo/icono se muestra cuadrado con esquinas ligeramente redondeadas.
- El texto aparece como `EXCLUSIVE CONTENT` en inglés, en mayúsculas y con una fuente llamativa.

## Vista en teléfono

En pantallas pequeñas, el logo y el texto se hacen más pequeños automáticamente y se mantienen centrados.


## Age confirmation

When the user clicks `EXCLUSIVE CONTENT`, an English confirmation popup appears:

```text
Are you 18 or older?
Yes / No
```

If the user clicks `Yes`, the page redirects to:

```text
https://onlyfans.com/exeof
```

If the user clicks `No`, the page shows this message:

```text
You must be 18 or older to continue.
```


## X card

A second card was added with the title:

```text
X
```

It redirects to:

```text
https://x.com/3xeqnima
```

The image for this card must be placed here:

```text
static/logox.png
```
