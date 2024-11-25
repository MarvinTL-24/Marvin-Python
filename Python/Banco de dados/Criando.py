import sqlite3
from pathlib import Path

# Define o caminho para o banco de dados
ROOT_PATH = Path(__file__).parent
db_path = ROOT_PATH / 'data/banco_de_dados.db'

# Cria o diretório 'data' caso não exista
db_path.parent.mkdir(parents=True, exist_ok=True)

# Cria uma conexão com o banco de dados (se o arquivo não existir, ele será criado automaticamente)
conexao = sqlite3.connect(db_path)
cursor = conexao.cursor()

# Função para criar a tabela
def criar_tabela():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cursos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT
    );
    """)
    conexao.commit()

# Função para inserir dados
def inserir_dados():
    cursor.execute("""
    INSERT INTO cursos (nome, descricao) VALUES
    ('Python para Iniciantes', 'Aprenda o básico de Python'),
    ('Desenvolvimento Web', 'Curso de front-end e back-end'),
    ('Banco de Dados SQL', 'Aprenda a manipular dados com SQL')
    """)
    conexao.commit()

# Função para consultar dados
def consultar_dados():
    cursor.execute("SELECT * FROM cursos")
    print("\nCursos cadastrados:")
    for linha in cursor.fetchall():
        print(f"ID: {linha[0]}, Nome: {linha[1]}, Descrição: {linha[2]}")

# Função principal
def main():
    # Cria a tabela (se não existir)
    criar_tabela()
    
    # Insere alguns dados (único momento em que inserimos)
    inserir_dados()
    
    # Consulta e exibe os dados
    consultar_dados()

# Executa a função principal
main()

# Fecha a conexão com o banco de dados
conexao.close()
