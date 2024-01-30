import random

"""Código que gera um peso aleatório.
    """

def peso(sexo=None):
    """A função aceita um argumento opcional chamado sexo, que pode ser "M" ou "m" 
    para masculino, "F" ou "f" para feminino, ou None para não especificado. Com base 
    no sexo fornecido, a função escolhe um intervalo de peso aleatório correspondente 
    (masculino ou feminino) e retorna o peso formatado como uma string com uma casa 
    decimal.

    Args:
        sexo (str, optional): definição do peso da pessoa. Defaults to None.

    Returns:
        float: Um peso aleatório, dependendo das restrições fornecidas.
    """
    if sexo == "M" or sexo == "m":
        peso_kg = random.uniform(60, 100)
    elif sexo == "F" or sexo == "f":
        peso_kg = random.uniform(45, 90)
    else:
        peso_kg = random.uniform(45, 100)

    return f'{peso_kg:.1f}'

