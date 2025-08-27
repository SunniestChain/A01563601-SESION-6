# Actividad: Uso de condicionales
### Instrucciones:
A continuación de presentan dos problemas, considera lo siguiente:
1. Nombra los programas **A0XXXXXXXProblema1.py** y **A0XXXXXXXProblema2.py** respectivamente
2. Lee **cuidadosamente** cada especificación de los problemas.
3. Por favor revise **detalladamente** las rúbricas de evaluación al final de este documento.

***

### 📝 Problema 1: Verificador de Edad para Eventos

**Problema a resolver:** Escribe un programa en Python que le pida al usuario su edad y determine si puede asistir a un evento con restricciones de edad. Hay tres tipos de eventos:

1. **Evento Juvenil:** Para personas de 13 a 17 años (inclusive).

2. **Evento para Adultos:** Para personas de 18 años o más.

3. **Evento Familiar:** Para todas las edades.

El programa debe usar la función `input()` para obtener la edad del usuario y sentencias `if`, `elif` y `else` para mostrar el mensaje adecuado.

**Instrucciones:**

1. Usa `input()` para pedirle al usuario que ingrese su edad. Recuerda que `input()` devuelve una cadena de texto, por lo que necesitarás convertirla a un número entero usando `int()`.

2. Usa una estructura `if-elif-else` para verificar la edad del usuario.

3. Imprime un mensaje para el usuario indicando a qué tipo(s) de evento puede asistir. Si el usuario es menor de 13 años, el programa debe informarle que no puede asistir a ninguno de los eventos con restricción de edad.

**Ejemplo de cómo debería funcionar:**

* Si el usuario ingresa **15**, el programa debe imprimir: "Puedes asistir al Evento Juvenil y al Evento Familiar."

* Si el usuario ingresa **25**, el programa debe imprimir: "Puedes asistir al Evento para Adultos y al Evento Familiar."

* Si el usuario ingresa **8**, el programa debe imprimir: "Lo siento, no puedes asistir a los eventos con restricción de edad. Solo al Evento Familiar."

***

### 📝 Problema 2: Calculadora de Calificaciones

**Problema a resolver:** Crea un programa que ayude a un estudiante a saber si aprobó un curso. El programa debe pedirle las calificaciones de 3 exámenes y calcular su promedio. Luego, debe usar una cláusula `if` para determinar si el promedio es suficiente para aprobar, considerando un umbral de aprobación de 70.

**Instrucciones:**

1. Usa `input()` para pedirle al usuario las calificaciones de los tres exámenes.

2. Recuerda que `input()` devuelve texto, por lo que necesitarás convertir cada calificación a un número usando `int()` o `float()` (para permitir decimales).

3. Calcula el promedio de las tres calificaciones.

4. Usa una sentencia `if-else` para comparar el promedio con 70.

5. Imprime un mensaje claro que indique si el estudiante aprobó o no, y cuál fue su promedio.

**Ejemplo de cómo debería funcionar:**

* Si el usuario ingresa las calificaciones **60, 80, y 90**, el promedio es 76.67, por lo que el programa debe imprimir: "¡Felicidades! Tu promedio es 76.67, has aprobado el curso."

* Si el usuario ingresa las calificaciones **50, 60, y 70**, el promedio es 60, por lo que el programa debe imprimir: "Lo siento, tu promedio es 60.0, no has aprobado el curso."

-----

### 📝 Rúbrica de Evaluación para el Programa 1: Verificador de Edad para Eventos

Este programa tiene un valor total de **6 puntos**.

| Criterio de Evaluación | Puntos (0-6) | Descripción del Nivel de Logro |
| :--- | :--- | :--- |
| **Entrada de Usuario y Conversión** | 2 | **2 puntos:** El programa utiliza `input()` correctamente y convierte la entrada a un tipo numérico (`int` o `float`). **1 punto:** El programa utiliza `input()` pero no realiza la conversión de tipo, o la conversión es incorrecta. **0 puntos:** No se pide la entrada al usuario o el código genera errores de forma inmediata. |
| **Lógica de Comparación** | 2 | **2 puntos:** La lógica del `if`, `elif` y `else` evalúa correctamente las tres condiciones de edad (13-17, 18+ y \<13) y usa los operadores de comparación (`>=`, `<=`) de manera apropiada. **1 punto:** La lógica es parcialmente correcta, por ejemplo, los rangos están definidos incorrectamente o se omite una de las condiciones. **0 puntos:** La lógica de comparación es incorrecta o no existe. |
| **Mensajes y Salida** | 1 | **1 punto:** Los mensajes de salida son claros, informan correctamente al usuario a qué eventos puede asistir y coinciden con los ejemplos proporcionados. **0 puntos:** El programa no imprime el resultado o la salida es incorrecta. |
| **Comentarios** | 1 | **1 punto:** El código incluye al menos 3 comentarios relevantes que explican la lógica o secciones importantes del programa. **0 puntos:** El código tiene menos de 3 comentarios o estos no son relevantes. |

-----

### 📝 Rúbrica de Evaluación para el Programa 2: Calculadora de Calificaciones

Este programa tiene un valor total de **6 puntos**.

| Criterio de Evaluación | Puntos (0-6) | Descripción del Nivel de Logro |
| :--- | :--- | :--- |
| **Entrada y Cálculo del Promedio** | 2 | **2 puntos:** El programa solicita las tres calificaciones usando `input()`, las convierte a un tipo numérico y calcula el promedio de forma correcta. **1 punto:** El programa pide las calificaciones pero el cálculo del promedio es incorrecto, o no se realiza la conversión de tipo adecuadamente. **0 puntos:** No se obtienen las calificaciones o el programa no realiza el cálculo. |
| **Lógica de Aprobación** | 2 | **2 puntos:** La sentencia `if-else` compara correctamente el promedio con el umbral de aprobación de 70. **1 punto:** La lógica es incorrecta (por ejemplo, usa el operador `==` en lugar de `>=`) o no se utiliza la estructura `if-else`. **0 puntos:** No se evalúa el promedio para determinar si se aprobó o no. |
| **Mensajes y Salida** | 1 | **1 punto:** Los mensajes de salida son claros y concisos, incluyen el promedio del estudiante y anuncian correctamente si aprobó o no el curso, según los ejemplos. **0 puntos:** El programa no muestra un mensaje de resultado o la salida es incorrecta. |
| **Comentarios** | 1 | **1 punto:** El código incluye al menos 3 comentarios relevantes que explican la lógica o secciones importantes del programa. **0 puntos:** El código tiene menos de 3 comentarios o estos no son relevantes. |
