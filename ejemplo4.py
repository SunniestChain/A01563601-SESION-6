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