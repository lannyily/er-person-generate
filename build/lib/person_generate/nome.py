import random

nomes_femininos = ['Ana', 'Maria', 'Joana', 'Julia', 'Camila', 'Isabel', 'Ana Clara', 'Mariana', 'Fernanda', 'Luana', 'Luiza', 'Luisa', 'Lara', 'Larissa', 'Larisa', 'Ana Julía', 'Barbara', 'Beatriz']
nomes_masculinos = ['Carlos', 'João Gabriel', 'Pedro', 'Lucas', 'Rafael', 'Bruno', 'Luis', 'Gabriel', 'Luis', 'Gabriel', 'Marcos', 'Mateus', 'Matheus', 'Miguel', 'Guilherme', 'Gustavo', 'Felipe', 'Felipe']
sobrenomes1 = ['da Silva', 'Oliveira', 'dos Santos', 'Pereira', 'Lima', 'Martins', 'Costa', 'Rodrigues', 'Fernandes', 'Pinto']
sobrenomes2 = ['Almeida', 'Souza', 'Araújo', 'Barros', 'Cardoso', 'Carvalho', 'Castro', 'Dias', 'Duarte', 'Freitas']

def nome(sexo=None):
    if sexo == "M" or sexo == "m":
        nome_aleatorio = random.choice(nomes_masculinos)
    elif sexo == "F" or sexo == "f":
        nome_aleatorio = random.choice(nomes_femininos)
    else:
        nome_aleatorio = random.choice(nomes_femininos + nomes_masculinos)
    
    sobrenome_aleatorio1 = random.choice(sobrenomes1)
    sobrenome_aleatorio2 = random.choice(sobrenomes2)
    
    return f'{nome_aleatorio} {sobrenome_aleatorio1} {sobrenome_aleatorio2}'

