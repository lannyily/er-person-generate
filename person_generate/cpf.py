import random

def cpf():
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

