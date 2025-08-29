import math as m #rtamos el módulo 'math' para usar 'pi'

def calcular_area_circulo(radio):
    area = m.pi * radio**2
    return area

# Calcular el área de un círculo con radio 10
area_del_circulo = calcular_area_circulo(10)
print(f"El área del círculo es: {area_del_circulo:.2f}") # Formateo para 2 decimales