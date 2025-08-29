# Funciones Definidas por el Desarrollador de Software en Python

Las **funciones** son bloques de código reutilizable que realizan una tarea específica. Piensa en ellas como una "caja negra" a la que le das una entrada (llamada **argumento**) y te da una salida (el **valor de retorno**). Para un ingeniero, las funciones son esenciales para organizar el código, hacerlo más legible y evitar la repetición.

## Sintaxis Básica

La sintaxis para definir una función en Python es sencilla:

``` Python
def nombre_de_la_funcion(parametro1, parametro2):
    # Bloque de código de la función
    resultado = parametro1 + parametro2
    return resultado # La palabra clave 'return' devuelve un valor
```

* **`def`**: Esta palabra clave se utiliza para iniciar la definición de una función.

* **`nombre_de_la_funcion`**: Es el nombre que le das a tu función. Debe ser descriptivo y seguir las convenciones de nombrado (usualmente en **minúsculas** y con **guiones bajos**).

* **`parametro1, parametro2`**: Son los valores de entrada que la función necesita para trabajar. Son opcionales.

* **`:`**: Un **dos puntos** marca el final de la línea de la definición.

* **`return`**: Esta palabra clave **devuelve un valor** desde la función. Si no se usa `return`, la función devuelve `None` por defecto.

## Ejemplos Prácticos

### Ejemplo 1: Saludo Simple 👋

Este ejemplo muestra una función sin parámetros que simplemente imprime un mensaje de bienvenida.

``` Python
def saludar():
    print("¡Hola, estudiante de ingeniería!")

# Llamar a la función para que se ejecute
saludar()
```

***

### Ejemplo 2: Suma de Dos Números ➕

Aquí vemos una función que toma dos parámetros (`a` y `b`) y devuelve su suma.

``` Python
def sumar_numeros(a, b):
    return a + b

# Llamar a la función y guardar el resultado
resultado = sumar_numeros(5, 3)
print("El resultado de la suma es:", resultado)
```

***

### Ejemplo 3: Cálculo del Área de un Círculo 🔵

Este ejemplo muestra cómo una función puede realizar un cálculo matemático usando un parámetro (el radio) y una constante (`PI`).

``` Python
import math # Importamos el módulo 'math' para usar 'pi'

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area

# Calcular el área de un círculo con radio 10
area_del_circulo = calcular_area_circulo(10)
print(f"El área del círculo es: {area_del_circulo:.2f}") # Formateo para 2 decimales
```

***

### Ejemplo 4: Verificación de un Número Positivo o Negativo 🤔

Las funciones pueden tener lógica condicional (como `if/else`) para devolver diferentes resultados.

``` Python
def verificar_signo(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Cero"

# Probar la función con diferentes números
print("El número 10 es:", verificar_signo(10))
print("El número -5 es:", verificar_signo(-5))
print("El número 0 es:", verificar_signo(0))
```

***

### Ejemplo 5: Formateo de Nombre Completo 🧑‍💻

Este último ejemplo une dos cadenas de texto (nombre y apellido) y devuelve un nombre completo con un formato específico.

``` Python
def formatear_nombre_completo(nombre, apellido):
    nombre_completo = f"{nombre.capitalize()} {apellido.capitalize()}"
    return nombre_completo

# Llamar a la función con valores de ejemplo
nombre_formateado = formatear_nombre_completo("juan", "perez")
print("Nombre formateado:", nombre_formateado)
```

***
## Ejercicios
### Ejercicio 1: Conversor de Temperatura 🌡️

**Problema:** Crea una función llamada `convertir_fahrenheit_a_celsius` que tome una temperatura en grados Fahrenheit y la convierta a grados Celsius. La fórmula de conversión es: 
$C = (F - 32) * 5/9$.

``` Python
# Ejemplo de uso
temp_fahrenheit = 68
temp_celsius = convertir_fahrenheit_a_celsius(temp_fahrenheit)
print(f"{temp_fahrenheit}°F es igual a {temp_celsius}°C")
# Salida esperada: 68.0°F es igual a 20.0°C
```

***

### Ejercicio 2: Verificador de Mayoría de Edad 🧑‍🎓

**Problema:** Escribe una función llamada `es_mayor_de_edad` que tome un parámetro `edad` (un número entero). La función debe devolver `True` si la edad es 18 o mayor, y `False` en caso contrario.

``` Python
# Ejemplos de uso
print("¿Tienes 20 años? ", es_mayor_de_edad(20))
print("¿Tienes 17 años? ", es_mayor_de_edad(17))
# Salida esperada:
# ¿Tienes 20 años?  True
# ¿Tienes 17 años?  False
```

***

### Ejercicio 3: Calculadora de Descuento 🏷️

**Problema:** Desarrolla una función llamada `calcular_descuento` que tome el `precio` original de un producto y un `porcentaje_descuento`. La función debe calcular y devolver el precio final después de aplicar el descuento.

``` Python

# Ejemplo de uso
precio_original = 100
descuento = 25
precio_final = calcular_descuento(precio_original, descuento)
print(f"El precio final con un {descuento}% de descuento es: ${precio_final:.2f}")
# Salida esperada: El precio final con un 25% de descuento es: $75.00
```

***

### Ejercicio 4: Verificador de Par o Impar ✨

**Problema:** Crea una función llamada `es_par` que tome un número entero. La función debe devolver la cadena de texto `"Par"` si el número es par, y `"Impar"` si el número es impar. (Pista: Usa el operador módulo `%`).

``` Python
# Ejemplos de uso
print("El número 12 es:", es_par(12))
print("El número 7 es:", es_par(7))
# Salida esperada:
# El número 12 es: Par
# El número 7 es: Impar
```

***

### Ejercicio 5: Concatenador de Cadenas de Texto 🔗

**Problema:** Escribe una función llamada `crear_mensaje` que tome un `nombre` y un `producto` como parámetros. La función debe construir y devolver un mensaje de saludo que incluya ambos parámetros, por ejemplo: `"Hola [Nombre], tu [Producto] está listo."`

**Solución:**

``` Python
# Ejemplo de uso
mensaje_cliente = crear_mensaje("Carlos", "pedido")
print(mensaje_cliente)
# Salida esperada: Hola Carlos, tu pedido está listo.
```

