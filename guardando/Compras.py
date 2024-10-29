'''
Crie uma lista com as seguintes especificações:
1- Itens
2-Valores
3-Quantidade
'''

# Inicializando as listas com a mais
itens = []
quantidade = []
valores = []
soma_total = []

n = 0
# Acrescimo da atividade
lista = int(input("Digite a quantidade de itens que deseja comprar: --> "))

continuar = 's'
while continuar.lower() == 's':
    for n in range(lista):
        #Criando a lista
        compras = input("Digite o nome do item desejado: --> ")
        numeros = int(input("Digite a quantidade do item desejado: --> "))
        valor = float(input("Digite o valor do produto: --> "))
        
        #APPEND --- Adicionar na lista
        itens.append(compras)
        quantidade.append(numeros)
        valores.append(valor)

        n += 1
    # Continuar ou Não
    continuar = input("Deseja continuar digitando itens? (s/n): --> ")


# Exibindo os resultados
print("\n Lista de Compras:")
for i in range(len(itens)):
    total_item = quantidade[i] * valores[i]
    soma_total.append(total_item)
    print(f" Item: {itens[i]}. \n Quantidade: {quantidade[i]}. \n Valor: R${valores[i]:.2f}. \n Total: R${total_item:.2f}")

print(f"O valor total será: R${sum(soma_total):.2f}")



 