import math

print('1- Faça um algoritmo para ler dois números e imprimir a soma dos números lidos. \n')
print('2-Faça um algoritmo para ler três números e imprimir a soma, média e produto dos números lidos. \n')
print('3-Faça um algoritmo para ler dois números e imprimir o maior, o menor ou então dizer se são iguais. \n')
print('4-Faça um algoritmo para ler um número inteiro e dizer se o número lido é par ou ímpar. \n')
print('5-Faça um algoritmo para ler dois números A e B e dizer se A é divisível por B. \n')
print('6-Faça um algoritmo para ler dois números e imprimi-los em ordem crescente. \n')
print('7-Faça um algoritmo para ler três números e imprimir o maior. \n')
print('8-Faça um algoritmo para ler três números e imprimir se estes podem ou não formar um triângulo. \n '
      'Observação – Para formar os lados de um triângulo, cada um dos valores tem que ser menor que a soma dos outros dois. \n')
print('9-Faça um algoritmo para ler três números e se estes puderem formar um triângulo dizer se o triângulo é “EQUILÁTERO”, “ISÓSCELES” OU “ESCALENO”. \n')
print('10-Faça um algoritmo para ler o preço de compra de uma mercadoria e calcular o seu preço de venda para que possa ser obtido um lucro de 30%. \n')
print('11-Faça um algoritmo para ler os catetos de um triângulo retângulo e calcular e imprimir a sua hipotenusa. \n') 
print('12-Faça um algoritmo para ler o raio e calcular o comprimento, a área e o volume de uma esfera. \n')   
Escolha = input('Digite o que deseja saber: ')

if Escolha == '1':
    N1 = float(input('Digite o valor desejado para N1: \n'))
    N2 = float(input('Digite o valor desejado para N2: \n'))
    soma = N1 + N2
    print(f'A soma de {N1} e {N2} é {soma}.')
    
elif Escolha == '2':
    N1 = float(input('Digite o valor desejado para N1: \n'))
    N2 = float(input('Digite o valor desejado para N2: \n'))
    N3 = float(input('Digite o valor desejado para N3: \n'))
    soma = N1 + N2 + N3
    media = soma / 3
    produto = N1 * N2 * N3
    print(f'A soma de {N1}, {N2} e {N3} é {soma}.')
    print(f'A média dos três valores é {media}.')
    print(f'O produto dos três valores é {produto}.')
    
elif Escolha == '3':
    N1 = float(input('Digite o valor desejado para N1: \n'))
    N2 = float(input('Digite o valor desejado para N2: \n'))
    if N1 > N2:
        print(f'O maior número é {N1} e o menor é {N2}.')
    elif N1 < N2:
        print(f'O maior número é {N2} e o menor é {N1}.')
    else:
        print(f'Os números {N1} e {N2} são iguais.')

elif Escolha == '4':
    N1 = int(input('Digite o valor desejado para N1: \n'))
    if N1 % 2 == 0:
        print(f'O número {N1} é par.')
    else:
        print(f'O número {N1} é ímpar.')

elif Escolha == '5':
    N1 = float(input('Digite o valor desejado para N1: \n'))
    N2 = float(input('Digite o valor desejado para N2: \n'))
    if N1 % N2 == 0:
        print(f'O número {N1} é divisível por {N2}.')
    else:
        print(f'O número {N1} não é divisível por {N2}.')

elif Escolha == '6':
    N1 = float(input('Digite o valor desejado para N1: \n'))
    N2 = float(input('Digite o valor desejado para N2: \n'))
    if N1 > N2:
        print(f'Os números em ordem crescente são: {N2}, {N1}.')
    else:
        print(f'Os números em ordem crescente são: {N1}, {N2}.')

elif Escolha == '7':
    N1 = float(input('Digite o valor desejado para N1: \n'))
    N2 = float(input('Digite o valor desejado para N2: \n'))
    N3 = float(input('Digite o valor desejado para N3: \n'))
    print(f'O maior número é {max(N1, N2, N3)}.')

elif Escolha == '8':
    N1 = float(input('Digite o valor desejado para N1: \n'))
    N2 = float(input('Digite o valor desejado para N2: \n'))
    N3 = float(input('Digite o valor desejado para N3: \n'))
    if (N1 + N2 > N3) and (N2 + N3 > N1) and (N1 + N3 > N2):
        print(f'Os números podem formar um triângulo.')
    else:
        print(f'Os números não podem formar um triângulo.')

elif Escolha == '9':
    N1 = float(input('Digite o valor desejado para N1: \n'))
    N2 = float(input('Digite o valor desejado para N2: \n'))
    N3 = float(input('Digite o valor desejado para N3: \n'))
    if (N1 == N2 == N3):
        print(f'O triângulo é equilátero.')
    elif (N1 == N2) or (N1 == N3) or (N2 == N3):
        print(f'O triângulo é isósceles.')
    else:
        print(f'O triângulo é escaleno.')

elif Escolha == '10':
    mercadoria = float(input('Digite o valor desejado para o produto: \n'))
    venda = mercadoria * 1.3
    print(f'O valor de venda do produto é R${venda:.2f}.')

elif Escolha == '11':
    cateto_adjacente = float(input('Digite o valor desejado para o Cateto Adjacente: \n'))
    cateto_oposto = float(input('Digite o valor desejado para o Cateto Oposto: \n'))
    hipotenusa = math.sqrt(cateto_adjacente**2 + cateto_oposto**2)
    print(f'O valor da hipotenusa é {hipotenusa:.2f}.')

elif Escolha == '12':
    raio = float(input('Digite o valor do raio: \n'))
    comprimento = 2 * math.pi * raio
    area = math.pi * raio**2
    volume = (4/3) * math.pi * raio**3
    print(f'O comprimento da esfera é {comprimento:.2f}.')
    print(f'A área da esfera é {area:.2f}.')
    print(f'O volume da esfera é {volume:.2f}.')
else:
    print('Escolha inválida!')
