import random

"""Esse código gera um número de telefone brasileiro aleatório, 
    incluindo DDD (Código de Discagem Direta).
    """

def telefone():
    """A função utiliza um dicionário ddds_por_estado que mapeia 
    estados brasileiros para listas de DDDs associados a esses estados. 
    Em seguida, ela escolhe aleatoriamente um estado, obtém os DDDs 
    correspondentes a esse estado e, por fim, escolhe aleatoriamente um 
    DDD e gera um número de telefone aleatório, retornando-o como uma 
    string formatada.

    Returns:
        str: Um número de telefone aleatório.
    """
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

    estados = list(ddds_por_estado.keys())
    estado = random.choice(estados)
    
    ddds = ddds_por_estado.get(estado)
    
    if ddds:
        ddd = random.choice(ddds)
        numero_principal = ''.join(str(random.randint(0, 9)) for _ in range(8))  
        telefone = f'({ddd}) {numero_principal[:4]}-{numero_principal[4:]}'
        return telefone
