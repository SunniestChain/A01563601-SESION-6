
def ctof(fahren):
    celc = (fahren - 32) * (5/9)
    print(f"La temperatura en Celcius es: {celc}")


ctof(float(input("Temperatura en Fahrenheit: ")))