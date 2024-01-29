import random

def altura(sexo=None):
    if sexo == "M" or sexo == "m":
        altura_metros = random.uniform(1.60, 2.00)
    elif sexo == "F" or sexo == "f":
        altura_metros = random.uniform(1.50, 1.90)
    else:
        altura_metros = random.uniform(1.50, 2.00)

    altura_centimetros = int(altura_metros * 100)
    return f'{altura_centimetros // 100}.{altura_centimetros % 100:02d}'

