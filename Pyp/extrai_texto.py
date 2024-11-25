import requests
from bs4 import BeautifulSoup

# URL da página web a ser analisada
url = "https://www.wikipedia.org/"

# Fazendo a requisição para a página
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Parseando o conteúdo HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extraindo o texto principal
    texto = soup.get_text()
    
    # Exibindo as primeiras linhas do texto
    print("Texto extraído da página:")
    print(texto[:500])  # Exibe os primeiros 500 caracteres
    
    # Extraindo títulos (h1, h2, h3, ...)
    titulos = []
    for i in range(1, 7):  # h1 até h6
        for tag in soup.find_all(f'h{i}'):
            titulos.append((f"h{i}", tag.get_text().strip()))
    
    # Exibindo os títulos extraídos
    print("\nTítulos encontrados:")
    for nivel, titulo in titulos:
        print(f"{nivel}: {titulo}")
    
    # Salvando o texto e os títulos em arquivos separados
    with open('texto_extraido.txt', 'w', encoding='utf-8') as arquivo_texto:
        arquivo_texto.write(texto)
    print("\nTexto salvo em 'texto_extraido.txt'.")
    
    with open('titulos_extraidos.txt', 'w', encoding='utf-8') as arquivo_titulos:
        for nivel, titulo in titulos:
            arquivo_titulos.write(f"{nivel}: {titulo}\n")
    print("Títulos salvos em 'titulos_extraidos.txt'.")
else:
    print(f"Erro ao acessar a página. Status code: {response.status_code}")
