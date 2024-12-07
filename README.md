# Proyecto Django: Web de Música 🎵

Este proyecto es una web de música. Permite gestionar artistas, álbumes y canciones, además de buscar álbumes por su título. 

## **Características**
- **Herencia de plantillas**: La web utiliza un diseño modular basado en una plantilla base.
- **Modelos**: Incluye tres modelos principales: `Artista`, `Álbum`, y `Canción`.
- **Formularios**: Se pueden agregar artistas, álbumes y canciones mediante formularios.
- **Búsquedas**: Es posible buscar álbumes en la base de datos por su título.

## **Instrucciones de uso**
1. **Clonar el repositorio**:
    ```bash
    git clone <URL-DEL-REPOSITORIO>
    cd blog_project
    ```

2. **Instalar dependencias**:
    Asegurate de tener un entorno virtual configurado e instalá las dependencias:
    ```bash
    pip install django
    ```

3. **Realizar migraciones**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Correr el servidor**:
    ```bash
    python manage.py runserver
    ```

5. **Probar funcionalidades**:
    - Acceder a [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
    - Crear artistas, álbumes y canciones desde las opciones del menú.
    - Buscar álbumes por título en la sección de búsqueda.

## **Estructura del proyecto**
- **Modelos**:
  - `Artista`: Nombre y género musical.
  - `Álbum`: Título, año de lanzamiento, y relación con un artista.
  - `Canción`: Título, duración, y relación con un álbum.
  
- **Formularios**:
  - Formulario para agregar artistas.
  - Formulario para agregar álbumes.
  - Formulario para agregar canciones.
  - Formulario para buscar álbumes por título.

- **Templates**:
  - `base.html`: Plantilla base con el diseño principal.
  - `inicio.html`: Página de inicio.
  - `formulario.html`: Para mostrar los formularios.
  - `buscar.html`: Página para buscar álbumes.

## **Autor**
Este proyecto fue desarrollado como práctica para aprender Django y el patrón MVT.
