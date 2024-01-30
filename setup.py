from setuptools import setup,find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

VERSION = "1.5.0"
DESCRIPTION = "Pacote de geração de dados de pessoas"
LONG_DESCRIPTION = "Pacote de geração de dados de pessoas, tais como nome, cpf, data de nascimento, peso, altura, telefone, cidade e estado. Para mais informações acesse: https://github.com/lannyily/person-generate"

REQUIRED_PACKAGES = [
    'numpy',
    'faker'
]

setup(
    # the name must match the folder name
    name="er_person_generate",
    version = VERSION,
    author = "Erlanny",
    author_email = "erlannyrodrigues@gmail.com",
    description = DESCRIPTION,
    long_description = long_description,
    long_description_content_type='text/markdown',
    packages = find_packages(),
    install_requires = REQUIRED_PACKAGES,#adiciona bibliotecas adicionais
    keywords = ['python', 'person', 'generate', 'brasil'],
    classifiers = ["Development Status :: 3 - Alpha",]
)