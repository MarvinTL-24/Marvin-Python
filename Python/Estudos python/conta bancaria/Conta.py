saldo = 500  # Saldo inicial da conta
saques = 0  # Contador de saques

print('1-Conta bancária.\n')
print('2-Sair.\n')

escolha = input("Digite se deseja entrar em sua conta bancária ou não: ")
print('-----------------------------------------------------------------------------------------------------')
if escolha == '1':
    print("Bem-vindo à sua conta bancária.\n")
    while True:  #Loop para permitir que o usuário faça várias ações (acima do nivel atual)
        print("Escolha uma das seguintes ações:\n")
        print('1-Conta Saque.\n')
        print('2-Conta Depósito.\n')
        print('3-Conta Extrato.\n')
        print('4-Sair.\n')  #Adicionado uma opção para sair do loop

        optativa = input("Digite a ação desejada: ")
        print('-----------------------------------------------------------------------------------------------------')
        if optativa == '1': #Saque
            if saques >= 3:
                print("Você já realizou o limite de 3 saques hoje.")
            else:
                valor = float(input('Digite o valor desejado para saque: R$ '))
                if valor > saldo:
                    print("Saldo insuficiente para o saque.")
                else:
                    saldo -= valor
                    saques += 1
                    print(f'O valor sacado foi: R${valor:.2f}. Seu saldo atual é R${saldo:.2f}.')
                    print(f'Você já realizou {saques} de 3 saques permitidos.\n')
                    print('-----------------------------------------------------------------------------------------------------')
        elif optativa == '2':  #Depósito
            deposito = float(input('Digite o valor que deseja depositar: R$ '))
            saldo += deposito
            print(f'O valor depositado foi: R${deposito:.2f}. Seu saldo atual é R${saldo:.2f}.')
            print('-----------------------------------------------------------------------------------------------------')
        elif optativa == '3':  #Extrato
            print(f'O saldo atual da sua conta é R${saldo:.2f}.')
            print('-----------------------------------------------------------------------------------------------------')

        elif optativa == '4':  #Sair
            print('Obrigado por utilizar o serviço bancário. Até logo.')
            print('-----------------------------------------------------------------------------------------------------')
            break  #Sai do loop e finaliza o programa

        else:
            print("Ação inválida.")
            print('-----------------------------------------------------------------------------------------------------')

else:
    print('Obrigado pela visita. Adeus.\n')
    print('-----------------------------------------------------------------------------------------------------')
