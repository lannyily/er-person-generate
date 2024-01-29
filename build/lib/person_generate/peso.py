import random

def peso(sexo=None):
    if sexo == "M" or sexo == "m":
        peso_kg = random.uniform(60, 100)
    elif sexo == "F" or sexo == "f":
        peso_kg = random.uniform(45, 90)
    else:
        peso_kg = random.uniform(45, 100)

    return f'{peso_kg:.1f}'

