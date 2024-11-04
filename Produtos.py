def adicionar_itens():
    itens = []
    quantidade = []
    valores = []

    lista = int(input("Digite o volume total do seu carrinho: --> "))

    for _ in range(lista):
        compras = input("Digite o nome do item desejado: --> ")
        numeros = int(input("Digite a quantidade do item desejado: --> "))
        valor = float(input("Digite o valor do produto: --> "))

        itens.append(compras)
        quantidade.append(numeros)
        valores.append(valor)

    return itens, quantidade, valores


def calcular_totais(itens, quantidade, valores):
    soma_total = []
    total_itens = sum(quantidade) 
    print("\nLista de Compras:")
    
    for i in range(len(itens)):
        total_item = quantidade[i] * valores[i]
        soma_total.append(total_item)
        print(f" Item: {itens[i]}.\n Quantidade: {quantidade[i]}.\n Valor: R${valores[i]:.2f}.\n Total: R${total_item:.2f}")

    valor_total = sum(soma_total)

    # Aplicando desconto
    desconto = 0
    if total_itens >= 50:
        desconto = 0.15
    elif total_itens >= 20:
        desconto = 0.10
    elif total_itens >= 10:
        desconto = 0.05

    valor_total_com_desconto = valor_total * (1 - desconto)
    print(f"O valor total será: R${valor_total:.2f}")
    if desconto > 0:
        print(f"Desconto de {desconto * 100:.0f}% aplicado. Novo valor total: R${valor_total_com_desconto:.2f}")
    else:
        print("Nenhum desconto aplicado.")

    return valor_total_com_desconto


def salvar_lista(itens, quantidade, valores, valor_total):
    with open("lista_compras.txt", "w") as file:
        file.write("Lista de Compras:\n")
        for i in range(len(itens)):
            total_item = quantidade[i] * valores[i]
            file.write(f"Item: {itens[i]}, Quantidade: {quantidade[i]}, Valor: R${valores[i]:.2f}, Total: R${total_item:.2f}\n")
        file.write(f"Valor Total: R${valor_total:.2f}\n")
    print("Lista salva em 'lista_compras.txt'.")


def menu():
    itens, quantidade, valores = [], [], []
    continuar = 's'
    
    while continuar.lower() == 's':
        itens_temp, quantidade_temp, valores_temp = adicionar_itens()
        itens.extend(itens_temp)
        quantidade.extend(quantidade_temp)
        valores.extend(valores_temp)

        continuar = input("Deseja continuar digitando itens? (s/n): --> ")

    valor_total = calcular_totais(itens, quantidade, valores)
    salvar_opcao = input("Deseja salvar a lista em um arquivo? (s/n): --> ")

    if salvar_opcao.lower() == 's':
        salvar_lista(itens, quantidade, valores, valor_total)


if __name__ == "__main__":
    menu()
