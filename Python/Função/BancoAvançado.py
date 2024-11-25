clientes = {}  # Dicionário para armazenar clientes e seus saldos
saques = {}    # Dicionário para armazenar contadores de saques

def cadastrar_cliente(cpf):
    if cpf in clientes:
        print("Cliente já cadastrado.")
    else:
        clientes[cpf] = 500  # Saldo inicial
        saques[cpf] = 0      # Contador de saques inicial
        print(f"Cliente com CPF {cpf} cadastrado com sucesso.")

def saqueando(cpf):
    global saques
    if saques[cpf] >= 3:
        print("Você já realizou o limite de 3 saques hoje.")
    else:
        valor = float(input('Digite o valor desejado para saque: R$ '))
        if valor > clientes[cpf]:
            print("Saldo insuficiente para o saque.")
        else:
            clientes[cpf] -= valor
            saques[cpf] += 1
            print(f'O valor sacado foi: R${valor:.2f}. Seu saldo atual é R${clientes[cpf]:.2f}.')
            print(f'Você já realizou {saques[cpf]} de 3 saques permitidos.\n')

def depositando(cpf):
    deposito = float(input('Digite o valor que deseja depositar: R$ '))
    clientes[cpf] += deposito
    print(f'O valor depositado foi: R${deposito:.2f}. Seu saldo atual é R${clientes[cpf]:.2f}.')

def extrato(cpf):
    print(f'O saldo atual da conta com CPF {cpf} é R${clientes[cpf]:.2f}.')

print('-----------------------------------------------------------------------------------------------------')
print('Bem-vindo ao banco, o que deseja fazer a seguir?\n')
print('1- Cadastrar cliente.\n')
print('2- Acessar conta.\n')
print('3- Sair.\n')

while True:
    escolha = input("Digite sua escolha: ")
    print('-----------------------------------------------------------------------------------------------------')
    
    if escolha == '1':
        cpf = input("Digite o CPF do cliente: ")
        cadastrar_cliente(cpf)
    
    elif escolha == '2':
        cpf = input("Digite o CPF do cliente: ")
        if cpf not in clientes:
            print("Cliente não encontrado. Cadastre primeiro.")
            continue
        print("Bem-vindo à sua conta bancária.\n")
        while True:
            print("Escolha uma das seguintes ações:\n")
            print('1- Saque.\n')
            print('2- Depósito.\n')
            print('3- Extrato.\n')
            print('4- Sair da conta.\n')

            optativa = input("Digite a ação desejada: ")
            print('-----------------------------------------------------------------------------------------------------')
            if optativa == '1':
                print(f'A sua conta bancária tem atualmente o saldo de R${clientes[cpf]:.2f}.\n')
                saqueando(cpf)
            elif optativa == '2':
                print(f'A sua conta bancária tem atualmente o saldo de R${clientes[cpf]:.2f}.\n')
                depositando(cpf)
            elif optativa == '3':
                extrato(cpf)
                print('-----------------------------------------------------------------------------------------------------')
            elif optativa == '4':
                print('Obrigado por utilizar o serviço bancário. Até logo.')
                print('-----------------------------------------------------------------------------------------------------')
                break
            else:
                print("Ação inválida.")
                print('-----------------------------------------------------------------------------------------------------')
    
    elif escolha == '3':
        print('Obrigado pela visita. Adeus.\n')
        print('-----------------------------------------------------------------------------------------------------')
        break
    
    else:
        print("Opção inválida.")
