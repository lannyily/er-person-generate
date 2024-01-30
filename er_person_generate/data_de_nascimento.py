from datetime import datetime
import random

"""Gera uma data de nascimento aleatória, o usuário pode escolher se quer uma pessoa 
   com mais de 18 anos, menos de 18 anos ou qualquer idade.
    """

def dataNascimento(idade=None):
    """Gera a data de nascimento de uma pessoa aleatória.
    
    A função aceita um argumento opcional chamado idade, que pode ser +18 para gerar 
    uma data de nascimento de uma pessoa com mais de 18 anos, -18 para uma pessoa com 
    menos de 18 anos, ou None para não impor restrições de idade. O código então gera 
    aleatoriamente um ano, mês e dia de acordo com as restrições ou sem restrições, e 
    retorna a data de nascimento formatada como uma string no formato 'dd/mm/aaaa'.
    
    Args:
        idade (str, optional): "+18" para uma pessoa maior de idade e "-18" para uma 
        pessoa menor de idade. Defaults to None.

    Returns:
        str: a data de nascimento de acordo com as restrições fornecidas.
    """
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
