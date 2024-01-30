import random

"""Código que gera uma altura aleatória.
    """

def altura(sexo=None):
    """Função que gera uma altura aleatória em metros e centímetros.
    
        Essa função gera uma altura aleatória com base no sexo fornecido como argumento ou, 
        se nenhum sexo for fornecido, para ambos os sexos. 
        A biblioteca random, que é usada para gerar números aleatórios. A função aceita um 
        argumento opcional chamado sexo, que pode ser "M" ou "m" para masculino, "F" ou "f" 
        para feminino, ou None para não especificado.
        Dependendo do valor de sexo, a altura é gerada de forma diferente. Se o sexo for 
        masculino, a altura é gerada entre 1.60 e 2.00 metros. Se for feminino, a altura é 
        gerada entre 1.50 e 1.90 metros. Se nenhum sexo for especificado, a altura é gerada 
        entre 1.50 e 2.00 metros.
        A altura é convertida de metros para centímetros e, em seguida, a função retorna uma 
        string formatada representando a altura, onde a parte inteira é a quantidade de metros 
        e a parte decimal representa os centímetros.
        
        Args:
        sexo (str, optional): "F" para a altura de uma mulher, "M" para a altura de um homem. 
        Defaults to None.
        
        Returns:
        float: Uma altura aleatória em metros e centímetros, dependendo do sexo fornecido. """
    if sexo == "M" or sexo == "m":
        altura_metros = random.uniform(1.60, 2.00)
    elif sexo == "F" or sexo == "f":
        altura_metros = random.uniform(1.50, 1.90)
    else:
        altura_metros = random.uniform(1.50, 2.00)

    altura_centimetros = int(altura_metros * 100)
    return f'{altura_centimetros // 100}.{altura_centimetros % 100:02d}'

