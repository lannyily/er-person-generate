import csv
import random
from pycep import PyCep

""" Código que gera uma cidade e estado aleatórios.

    Esse código ler um arquivo CSV contendo o valor minimo do CEP de todas as cidades do Brasil,
    sorteia um CEP aleatório desse arquivo e, em seguida, usa esse número para obter informações
    de CEP (Código de Endereçamento Postal), que estão em um discionário usando a biblioteca pycep. 
    """

nome_arquivo = 'person_generate/lista.csv'

def sorteia_numero():
    """Função que sorteia um CEP de um arquivo CSV.
    
    Esta função lê o arquivo CSV, itera sobre as linhas e os números dentro das linhas, adiciona 
    esses números a uma lista chamada numeros e, finalmente, retorna um número aleatório dessa lista.

    Returns:
    str: Uma string aleatória do arquivo CSV.

    """
    numeros = []
    
    with open(nome_arquivo, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
    
        for linha in leitor_csv:
            for numero in linha:
                numeros.append(numero)
    
    return random.choice(numeros)

def cidadeEstado():
    """Função que gera uma cidade e estado aleatórios.
    
    Esta função utiliza o número aleatório gerado pela função sorteia_numero para obter informações de CEP 
    usando a biblioteca pycep. O nome da cidade (localidade) e o estado (uf) são extraídos do resultado e 
    retornados formatados como uma string contendo "Nome da Cidade - Estado"
    
    Returns:
        str: Uma string contendo o nome da cidade e o estado.
    """
    numero = sorteia_numero()
    cep = PyCep(numero)
    
    result = cep.dadosCep
    nome_cidade = result['localidade']
    estado = result['uf']
    return f'{nome_cidade} - {estado}'
    