'''
Crie um programa que leia uma palavra e mostre quantas vogais ela possui.
'''

texto = input('Digite uma palavra: ')
vogais_minuscula = 0
vogais_maiuscula = 0
vogais = 0
minusculas = 'aeiou'
maiusculo = 'AEIOU'
encontradas = []

for letra in texto:
    if letra in minusculas + maiusculo:
        vogais += 1  # Conta todas as vogais
        encontradas.append(letra)  # Armazena as vogais encontradas
        if letra in maiusculo:
            vogais_maiuscula += 1  # Conta vogais maiúsculas
        elif letra in minusculas:
            vogais_minuscula += 1  # Conta vogais minúsculas

# Exibe os resultados
print(f'A palavra "{texto}" possui {vogais} vogais.')
print(f'Número de vogais maiúsculas: {vogais_maiuscula}')
print(f'Número de vogais minúsculas: {vogais_minuscula}')
print(f'As vogais encontradas são: {",".join(encontradas)}')
