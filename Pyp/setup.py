from setuptools import setup

# Lendo o conteúdo do README.md para a descrição longa
with open("README.md", "r", encoding="utf-8") as arq:
    readme = arq.read()

setup(
    name='Testando',  # Nome do pacote
    version='0.0.1',  # Versão inicial
    license='MIT',  # Licença
    author='MarvinTL-24',  # Seu nome ou nome de usuário
    author_email='descrentetrabalhador@gmail.com',  # Substitua pelo seu email real
    description='Isso é só um teste',  # Breve descrição
    long_description=readme,  # Descrição longa retirada do README.md
    long_description_content_type="text/markdown",  # Formato do README
    url='https://github.com/MarvinTL-24',  # Link para o seu GitHub
    keywords=['github', 'MarvinTL-24', 'Linguagens'],  # Palavras-chave relevantes
    packages=['MarvinTL-24'],  # Pasta do pacote Python
    install_requires=['requests'],  # Dependências do pacote
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Versão mínima do Python necessária
    project_urls={  # Links úteis
        "Bug Tracker": "https://github.com/MarvinTL-24/issues",
        "Source Code": "https://github.com/MarvinTL-24",
    },
)
