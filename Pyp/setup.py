from setuptools import setup

# Lendo o conteúdo do README.md para a descrição longa
with open("README.md", "r", encoding="utf-8") as arq:
    readme = arq.read()

setup(
    name='MatematicaEducacional',  # Nome do pacote
    version='0.0.1',  # Versão inicial
    license='MIT',  # Licença
    author='MarvinTL-24',  # Seu nome ou nome de usuário
    author_email='descrentetrabalhador@gmail.com',  # Substitua pelo seu email real
    description='O programa é uma ferramenta educacional que abrange uma ampla gama de conceitos fundamentais e avançados de matemática escolar. Ele está estruturado em diferentes módulos, cada um abordando um conjunto específico de tópicos, desde operações básicas até álgebra, geometria, trigonometria, equações, estatísticas e progressões. O objetivo do programa é proporcionar uma maneira prática e acessível para estudantes e professores resolverem problemas matemáticos e aprenderem conceitos de forma interativa.',  # Breve descrição
    long_description=readme,  # Descrição longa retirada do README.md
    long_description_content_type="text/markdown",  # Formato do README
    url='https://github.com/MarvinTL-24/Marvin-Python',  # Link para o seu GitHub
    keywords=['github', 'Matematica', 'Educação', 'Ensino', 'Matemática'],  # Palavras-chave relevantes
    packages=['Matematica'],  # Pasta do pacote Python
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Versão mínima do Python necessária
    project_urls={  # Links úteis
        "Bug Tracker": "https://github.com/MarvinTL-24",
        "Source Code": "https://github.com/MarvinTL-24/Marvin-Python",
    },
)
