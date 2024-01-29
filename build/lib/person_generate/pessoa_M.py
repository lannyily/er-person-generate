import random
from datetime import datetime
import string
from pycep import PyCep
import csv

nome_sorteado = None
nome_arquivo = 'person_generate/lista.csv'

nomes_masculinos = ['Carlos', 'João Gabriel', 'Pedro', 'Lucas', 'Rafael', 'Bruno', 'Luis', 'Gabriel', 'Luis', 'Gabriel', 'Marcos', 'Mateus', 'Matheus', 'Miguel', 'Guilherme', 'Gustavo', 'Felipe', 'Felipe']
sobrenomes1 = ['da Silva', 'Oliveira', 'dos Santos', 'Pereira', 'Lima', 'Martins', 'Costa', 'Rodrigues', 'Fernandes', 'Pinto']
sobrenomes2 = ['Almeida', 'Souza', 'Araújo', 'Barros', 'Cardoso', 'Carvalho', 'Castro', 'Dias', 'Duarte', 'Freitas']

def gerar_nome():
    global nome_sorteado
    nome_aleatorio = random.choice(nomes_masculinos)
    sobrenome_aleatorio1 = random.choice(sobrenomes1)
    sobrenome_aleatorio2 = random.choice(sobrenomes2)
    nome_sorteado = f'{nome_aleatorio} {sobrenome_aleatorio1} {sobrenome_aleatorio2}'
    return nome_sorteado

def gerar_email():
    global nome_sorteado
    nome_completo = nome_sorteado.replace(" ", "").lower()
    dominios = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'example.com']  # Adicione mais domínios se necessário
    dominio_aleatorio = random.choice(dominios)
    
    numero_aleatorio = gerar_numero_aleatorio().replace(".", "").replace("-", "")
    data_nascimento = gerar_data_nascimento()
    ano_nascimento = data_nascimento.year
    
    email = f'{nome_completo}{ano_nascimento}@{dominio_aleatorio}'
    
    return email

def gerar_numero_aleatorio():
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

def gerar_data_nascimento():
    ano_atual = datetime.now().year
    
    ano_manimo = 1950
    ano_maximo = ano_atual - 18
    ano = random.randint(ano_manimo, ano_maximo)
    
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
        
    return datetime(ano, mes, dia)


def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def calcular_idade(data_nascimento):
    hoje = datetime.now()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

def sorteia_numero():
    numeros = []
    
    with open(nome_arquivo, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
    
        for linha in leitor_csv:
            for numero in linha:
                numeros.append(numero)
    
    return random.choice(numeros)

def obter_info_cep(numero_sorteado):
    cep = PyCep(numero_sorteado)
    
    result = cep.dadosCep
    nome_cidade = result['localidade']
    estado = result['uf']
    return nome_cidade, estado

def gerar_altura():
    altura_metros = random.uniform(1.60, 2.00)
    altura_centimetros = int(altura_metros * 100)
    return f'{altura_centimetros // 100}.{altura_centimetros % 100:02d} cm'

def gerar_peso():
    peso_kg = random.uniform(60, 100)
    return f'{peso_kg:.1f} kg'

def gerar_telefone(estado):
    ddds_por_estado = {
        'SP': ['11', '12', '13', '14', '15', '16', '17', '18', '19'],
        'RJ': ['21', '22', '24'],
        'ES': ['27', '28'],
        'MG': ['31', '32', '33', '34', '35', '37', '38'],
        'BA': ['71', '73', '74', '75', '77'],
        'SE': ['79'],
        'PE': ['81', '87'],
        'AL': ['82'],
        'PB': ['83'],
        'RN': ['84'],
        'CE': ['85', '88'],
        'PI': ['86', '89'],
        'MA': ['98', '99'],
        'PA': ['91', '93', '94'],
        'AP': ['96'],
        'AM': ['92', '97'],
        'RR': ['95'],
        'AC': ['68'],
        'GO': ['62', '64'],
        'TO': ['63'],
        'MT': ['65', '66'],
        'MS': ['67'],
        'RO': ['69'],
        'DF': ['61'],
        'PR': ['41', '42', '43', '44', '45', '46'],
        'SC': ['47', '48', '49'],
        'RS': ['51', '53', '54', '55']
    }

    ddds = ddds_por_estado.get(estado.upper())

    if ddds:
        ddd = random.choice(ddds)
        numero_principal = ''.join(str(random.randint(0, 9)) for _ in range(8))  
        telefone = f'({ddd}) {numero_principal[:4]}-{numero_principal[4:]}'
        return telefone
    else:
        return "Estado não encontrado."
    
def tipo_sanguineo():
    tipos_sanguineos = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    tipo = random.choice(tipos_sanguineos)
    return tipo

def pessoaM():
    nome = gerar_nome()
    cpf = gerar_numero_aleatorio()
    data_nascimento = gerar_data_nascimento()
    idade = calcular_idade(data_nascimento)
    sexo = 'Masculino'
    email = gerar_email()
    senha = gerar_senha()
    cep = sorteia_numero()
    cidade, estado = obter_info_cep(cep)
    telefone = gerar_telefone(estado)
    altura = gerar_altura()
    peso = gerar_peso()
    tipo_sang = tipo_sanguineo()
    return f'--- Dados Pessoais ---\nNome: {nome}\nCPF: {cpf}\nData de Nascimento: {data_nascimento.strftime("%d/%m/%Y")}\nIdade: {idade}\nSexo: {sexo}\n--- Online ---\nE-mail: {email}\nSenha: {senha}\n--- Endereço ---\nCEP: {cep}\nCidade: {cidade}\nEstado: {estado}\n--- Telefone ---\nCelular: {telefone}\n--- Caracteristicas Físicas ---\nAltura: {altura}\nPeso: {peso}\nTipo Sanguineo: {tipo_sang}'
