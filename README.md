# Parcial-2

Este repositorio contiene el código y los archivos relacionados con el segundo parcial de la asignatura de Patrones.

## Contenido

- **Punto 1:** Descripción del primer punto.
- **Punto 2:** Descripción del segundo punto.
- **Punto 3:** Descripción del tercer punto.

## Requisitos

- Python 3.11
- ANTLR 4
- numpy

## Configuración del Entorno

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/dvar98/Parcial-2.git
cd Parcial-2
```

### Paso 2: Crear un Entorno Virtual

```bash
python3 -m venv .venv
```

### Paso 3: Activar el Entorno Virtual

- En Windows:
    ```bash
    .venv\Scripts\activate
    ```
- En macOS/Linux:
    ```bash
    source .venv/bin/activate
    ```

### Paso 4: Instalar las Dependencias

```bash
pip install -r requirements.txt
```

## Uso

### Paso 5: Generar los Archivos ANTLR

```bash
antlr4 -Dlanguage=Python3 Punto\ 3/FourierTransform.g4
```

### Paso 6: Ejecutar el Programa

```bash
python Punto\ 3/main.py input.txt
```

## Estructura del Proyecto

- `Punto 1/`: Archivos relacionados con el primer punto.
- `Punto 2/`: Archivos relacionados con el segundo punto.
- `Punto 3/`: Archivos relacionados con el tercer punto.
- `main.py`: Script principal para ejecutar el programa.
- `.g4`: Archivo de gramática ANTLR.

## Contribuciones

Para contribuir, por favor crea un fork del repositorio y haz un pull request con tus cambios.

## Licencia

Este proyecto está bajo la Licencia MIT.
