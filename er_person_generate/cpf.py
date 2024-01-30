import random

""" Código que gera um CPF aleatório válido.
    
    Esse código em Python gera um número de CPF (Cadastro de Pessoas Físicas) 
    aleatório e valida se o CPF gerado é válido. 
    """

def cpf():
    """Função que gera um CPF aleatório válido.
    
    Esta função gera uma parte numérica aleatória de 9 dígitos e calcula os dois 
    dígitos verificadores do CPF (decimo_digito e decimo_primeiro_digito). Em seguida, 
    constrói o CPF completo e verifica se é válido usando a função valida_cpf. Se for 
    válido, retorna o CPF formatado.

    Returns:
        str: Um número de CPF aleatório e válido.
    """
    while True:
        parte_numerica = ''.join(str(random.randint(0, 9)) for _ in range(9))

        soma = sum(int(digito) * (10 - i) for i, digito in enumerate(parte_numerica))
        decimo_digito = (soma * 10) % 11

        soma = sum(int(digito) * (11 - i) for i, digito in enumerate(parte_numerica + str(decimo_digito)))
        decimo_primeiro_digito = (soma * 10) % 11

        cpf = f'{parte_numerica}{decimo_digito}{decimo_primeiro_digito}'

        if valida_cpf(cpf):
            return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

def valida_cpf(cpf):
    """Verificador de CPF.
    
    Esta função valida um CPF verificando se ele tem 11 dígitos e se os dígitos 
    verificadores estão corretos.

    Args:
        cpf (int): Número de CPF a ser validado.

    Returns:
        bool : True se o CPF for válido, False caso contrário.
    """
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return False
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 11 - resto if resto >= 2 else 0
    if digito1 != int(cpf[9]):
        return False
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 11 - resto if resto >= 2 else 0
    if digito2 != int(cpf[10]):
        return False
    return True

