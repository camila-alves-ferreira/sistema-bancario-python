saldo = 0
numero_saques = 0
limite_saques = 3
limite = 500
deposito = []
extrato = []


while True:
    print('-' * 28)
    print('BANCO DIGITAL INNOVATION ONE')
    print('-' * 28)
    print('''
    [1] Depósito
    [2] Saque 
    [3] Extrato
    [0] Sair''')

    opcao = input('\nOpção: ')

    if opcao == '1':
        valor = float(input('Informe o valor do depósito: '))
        if valor > 0:
            saldo += valor
            extrato.append(f'Depósito: R$ {valor:.2f}')
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print('Operação não realizada! O valor informado é inválido.')

    elif opcao == '2':
        valor = float(input('Informe o valor do saque: '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= limite_saques

        '''if valor > 0:
            saldo -= valor
            extrato.append(f'Saque: R$ {valor:.2f}')
            numero_saques += 1
        elif excedeu_saldo:
            print('Operação não realizada! Você não tem saldo suficiente.')
        elif excedeu_limite:
            print('Operação não realizada! O saque excedeu o limite.')
        elif excedeu_saque:
            print('Operação não realizada! Você excedeu o limite de saques diários.')
        else:
            print('Operação não realizada! O valor informado é inválido.') '''

        if valor > 0:
            if not excedeu_saldo and not excedeu_limite and not excedeu_saque:
                saldo -= valor
                extrato.append(f'Saque: R$ {valor:.2f}')
                numero_saques += 1
                print(f'Saque: R$ {valor:.2f} realizado com sucesso.')
            elif excedeu_saldo:
                print('Operação não realizada! Você não tem saldo suficiente.')
            elif excedeu_limite:
                print('Operação não realizada! O saque excedeu o limite.')
            elif excedeu_saque:
                print('Operação não realizada! Você excedeu o limite de saques diários.')
        else:
            print('Operação não realizada! O valor informado é inválido.')

    elif opcao == '3':
        print('========== EXTRATO ==========')
        if not extrato:
            print('Não foram realizadas movimentações.')
        else:
            for movimentacao in extrato:
                print(movimentacao)
        print(f'Saldo: R${saldo:.2f}')
        print('=============================')

    elif opcao == '0':
        break

    else:
        print('Operação não realizada! Por favor, tente novamente.')