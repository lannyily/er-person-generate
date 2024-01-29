import csv
import random
from pycep import PyCep

nome_arquivo = 'person_generate/lista.csv'

def sorteia_numero():
    numeros = []
    
    with open(nome_arquivo, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
    
        for linha in leitor_csv:
            for numero in linha:
                numeros.append(numero)
    
    return random.choice(numeros)

def cidadeEstado():
    numero = sorteia_numero()
    cep = PyCep(numero)
    
    result = cep.dadosCep
    nome_cidade = result['localidade']
    estado = result['uf']
    return f'{nome_cidade} - {estado}'
    