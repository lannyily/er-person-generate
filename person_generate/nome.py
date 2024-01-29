import random

"""Codigo que gera um nome aleatório.

    Esse código gera um nome aleatório com base em listas de nomes e sobrenomes.
    """

nomes_femininos = ['Ana', 'Maria', 'Joana', 'Julia', 'Camila', 'Isabel', 'Ana Clara', 'Mariana', 'Fernanda', 'Luana', 'Luiza', 'Luisa', 'Lara', 'Larissa', 'Larisa', 'Ana Julía', 'Barbara', 'Beatriz']
nomes_masculinos = ['Carlos', 'João Gabriel', 'Pedro', 'Lucas', 'Rafael', 'Bruno', 'Luis', 'Gabriel', 'Luis', 'Gabriel', 'Marcos', 'Mateus', 'Matheus', 'Miguel', 'Guilherme', 'Gustavo', 'Felipe', 'Felipe']
sobrenomes1 = ['da Silva', 'Oliveira', 'dos Santos', 'Pereira', 'Lima', 'Martins', 'Costa', 'Rodrigues', 'Fernandes', 'Pinto']
sobrenomes2 = ['Almeida', 'Souza', 'Araújo', 'Barros', 'Cardoso', 'Carvalho', 'Castro', 'Dias', 'Duarte', 'Freitas']

def nome(sexo=None):
    """Função que gera um nome aleatório.
    
    A função aceita um argumento opcional chamado sexo, que pode ser "M" ou "m" para 
    masculino, "F" ou "f" para feminino, ou None para não especificado. Com base no 
    sexo fornecido, a função escolhe um nome aleatório da lista correspondente (masculino 
    ou feminino) e dois sobrenomes aleatórios, e retorna o nome completo formatado como 
    uma string.

    Args:
        sexo (str, optional): definição se quer um nome feminino ou masculino. Defaults to None.

    Returns:
        str: Um nome aleatório, dependendo das restrições fornecidas.
    """
    if sexo == "M" or sexo == "m":
        nome_aleatorio = random.choice(nomes_masculinos)
    elif sexo == "F" or sexo == "f":
        nome_aleatorio = random.choice(nomes_femininos)
    else:
        nome_aleatorio = random.choice(nomes_femininos + nomes_masculinos)
    
    sobrenome_aleatorio1 = random.choice(sobrenomes1)
    sobrenome_aleatorio2 = random.choice(sobrenomes2)
    
    return f'{nome_aleatorio} {sobrenome_aleatorio1} {sobrenome_aleatorio2}'

