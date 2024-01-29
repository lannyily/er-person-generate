from setuptools import setup,find_packages

VERSION = "0.4.0"
DESCRIPTION = "Pacote de geração de dados de pessoas"
LONG_DESCRIPTION = "Pacote de geração de dados de pessoas, tais como nome, cpf, data de nascimento, peso, altura, telefone, cidade e estado."

#setting up

setup(
    # the name must match the folder name
    name="person_generate",
    version = VERSION,
    author = "Erlanny",
    author_email = "erlannyrodrigues@gmail.com",
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    packages = find_packages(),
    install_requires = ["numpy"],#adiciona bibliotecas adicionais
    keywords = ['python', 'person', 'generate', 'brasil'],
    classifiers = ["Development Status :: 3 - Alpha",],
    package_data={'person_generate': ['lista.csv']}
)