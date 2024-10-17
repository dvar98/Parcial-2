## Parcial-2

Este repositorio contiene el código y los archivos relacionados con el segundo parcial de la asignatura de Lenguajes.

#### Contenido del Proyecto

El proyecto está dividido en tres puntos principales, cada uno con su propio directorio y conjunto de archivos:

1. **Punto 1:**
   - **Objetivo:** Diseñar una gramática para un lenguaje de programación que pueda hacer operaciones con números complejos.
   - **Archivos:**
     - **`input.txt`**: Contiene las pruebas de entrada para la gramática de números complejos.
       ```plaintext
       (2 + 7i) + (3 - 4i)
       (1 + 2i) * (2 - 3i)
       ```
     - **[`main.py`](https://github.com/dvar98/Parcial-2/blob/main/Punto%201/main.py)**: Ejecuta la gramática y realiza las operaciones solicitadas con los números complejos.

2. **Punto 2:**
   - **Objetivo:** Diseñar una gramática para un lenguaje de programación que realice las siguientes funciones:
     - Aplicar una función sobre los ítems de un objeto iterable (lista, tupla, etc...).
       - Ejemplo: `MAP(function, objeto iterable)`
     - A partir de una lista o iterador y una función condicional, devolver una nueva colección con los elementos filtrados que cumplan la condición.
       - Ejemplo: `FILTER(multiple, numeros)`
   - **Archivos:**
     - **[`input.txt`](https://github.com/dvar98/Parcial-2/blob/main/Punto%202/input.txt)**: Contiene las pruebas de entrada para las funciones de mapeo y filtrado.
       ```plaintext
       MAP(square, [1, 2, 3, 4])
       FILTER(even, [1, 2, 3, 4, 5, 6])
       MAP(double, (5, 6, 7, 8))
       FILTER(multiple, [9, 10, 11, 12, 13, 14, 15])
       ```
     - **[`main.py`](https://github.com/dvar98/Parcial-2/blob/main/Punto%202/main.py)**: Ejecuta la gramática y realiza las operaciones de mapeo y filtrado.
       ```python
       import sys
       from antlr4 import *
       from MapFilterLexer import MapFilterLexer
       from MapFilterParser import MapFilterParser

       class MapFilterListener(ParseTreeListener):
           def enterMapExpr(self, ctx:MapFilterParser.MapExprContext):
               function = ctx.function().getText()
               iterable = self.getIterable(ctx.iterable())
               print(f"Applying MAP function '{function}' to iterable '{iterable}'")
               result = list(map(self.getFunction(function), iterable))
               print(f"Result: {result}")

           def enterFilterExpr(self, ctx:MapFilterParser.FilterExprContext):
               function = ctx.function().getText()
               iterable = self.getIterable(ctx.iterable())
               print(f"Applying FILTER function '{function}' to iterable '{iterable}'")
               result = list(filter(self.getFunction(function), iterable))
               print(f"Result: {result}")

           def getIterable(self, ctx):
               if ctx.NAME():
                   return ctx.NAME().getText()
               elif ctx.list_():
                   return [int(e.getText()) for e in ctx.list_().elements().element()]
               elif ctx.tuple_():
                   return [int(e.getText()) for e in ctx.tuple_().elements().element()]
               return []

           def getFunction(self, name):
               if name == "square":
                   return lambda x: x ** 2
               elif name == "double":
                   return lambda x: x * 2
               elif name == "even":
                   return lambda x: x % 2 == 0
               elif name == "odd":
                   return lambda x: x % 2 != 0
               elif name == "multiple":
                   return lambda x: x % 3 == 0
               return lambda x: x

       def main(argv):
           input_stream = FileStream(argv[1])
           lexer = MapFilterLexer(input_stream)
           stream = CommonTokenStream(lexer)
           parser = MapFilterParser(stream)
           tree = parser.prog()

           listener = MapFilterListener()
           walker = ParseTreeWalker()
           walker.walk(listener, tree)

       if __name__ == '__main__':
           main(sys.argv)
       ```

3. **Punto 3:**
   - **Objetivo:** Diseñar una gramática para un lenguaje de programación que calcule la transformada de Fourier.
   - **Archivos:**
     - **[`input.txt`](https://github.com/dvar98/Parcial-2/blob/main/Punto%203/input.txt)**: Contiene las pruebas de entrada para las transformadas de Fourier y transformadas de pares.
       ```plaintext
       FOURIER([1, 2, 3, 4])
       PAIRTRANSFORM([1, 2, 3, 4])
       ```
     - **[`main.py`](https://github.com/dvar98/Parcial-2/blob/main/Punto%203/main.py)**: Ejecuta la gramática y realiza las operaciones de transformadas de Fourier y transformadas de pares.
       ```python
       import sys
       from antlr4 import *
       from FourierTransformLexer import FourierTransformLexer
       from FourierTransformParser import FourierTransformParser

       class FourierTransformListener(ParseTreeListener):
           def enterFourierTransformStmt(self, ctx:FourierTransformParser.FourierTransformStmtContext):
               iterable = self.getIterable(ctx.iterable())
               print(f"Calculating Fourier Transform for iterable: {iterable}")
               result = self.calculateFourierTransform(iterable)
               print(f"Result: {result}")

           def enterPairTransformStmt(self, ctx:FourierTransformParser.PairTransformStmtContext):
               iterable = self.getIterable(ctx.iterable())
               print(f"Calculating Pair Transform for iterable: {iterable}")
               result = self.calculatePairTransform(iterable)
               print(f"Result: {result}")

           def getIterable(self, ctx):
               if ctx.NAME():
                   return ctx.NAME().getText()  # Placeholder for actual data retrieval
               elif ctx.list_():
                   return [float(e.getText()) for e in ctx.list_().elements().element()]
               elif ctx.tuple_():
                   return [float(e.getText()) for e in ctx.tuple_().elements().element()]
               return []

           def calculateFourierTransform(self, data):
               import numpy as np
               return np.fft.fft(data)

           def calculatePairTransform(self, data):
               # Placeholder for pair transform logic
               return [(x, 2*x) for x in data]

       def main(argv):
           input_stream = FileStream(argv[1])
           lexer = FourierTransformLexer(input_stream)
           stream = CommonTokenStream(lexer)
           parser = FourierTransformParser(stream)
           tree = parser.prog()

           listener = FourierTransformListener()
           walker = ParseTreeWalker()
           walker.walk(listener, tree)

       if __name__ == '__main__':
           main(sys.argv)
       ```

### Requisitos

- **Python 3.11**
- **ANTLR 4**
- **numpy**

### Configuración del Entorno

1. **Clonar el Repositorio**
   ```bash
   git clone https://github.com/dvar98/Parcial-2.git
   cd Parcial-2
   ```

2. **Crear un Entorno Virtual**
   ```bash
   python3 -m venv .venv
   ```

3. **Activar el Entorno Virtual**
   - En Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Instalar las Dependencias**
   ```bash
   pip install -r requirements.txt
   ```

### Uso

5. **Generar los Archivos ANTLR**
   ```bash
   antlr4 -Dlanguage=Python3 Punto\ 3/FourierTransform.g4
   ```

6. **Ejecutar el Programa**
   ```bash
   python Punto\ 3/main.py input.txt
   ```

### Estructura del Proyecto

- **`Punto 1/`**: Archivos relacionados con el primer punto.
- **`Punto 2/`**: Archivos relacionados con el segundo punto.
- **`Punto 3/`**: Archivos relacionados con el tercer punto.
- **`main.py`**: Script principal para ejecutar el programa.
- **`.g4`**: Archivo de gramática ANTLR.

### Contribuciones

Para contribuir, por favor crea un fork del repositorio y haz un pull request con tus cambios.

### Licencia

Este proyecto está bajo la Licencia MIT.
