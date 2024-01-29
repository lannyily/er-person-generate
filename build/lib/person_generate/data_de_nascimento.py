from datetime import datetime
import random

def dataNascimento(idade=None):
    ano_atual = datetime.now().year

    if idade == "+18":
        ano_minimo = 1950
        ano_maximo = ano_atual - 18
        ano = random.randint(ano_minimo, ano_maximo)
    elif idade == "-18":
        ano_minimo = ano_atual - 18
        ano_maximo = 2020
        ano = random.randint(ano_minimo, ano_maximo)
    else:
        ano_minimo = 1950
        ano_maximo = ano_atual
        ano = random.randint(ano_minimo, ano_maximo)

    mes = random.randint(1, 12)

    if mes in [1, 3, 5, 7, 8, 10, 12]:
        dia = random.randint(1, 31)
    elif mes == 2:
        if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
            dia = random.randint(1, 29)
        else:
            dia = random.randint(1, 28)
    else:
        dia = random.randint(1, 30)

    return f'{dia:02}/{mes:02}/{ano}'
