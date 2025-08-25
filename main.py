import os

info = {
    'saldo': 0,
    'limite': 500,
    'extrato': [],
    'numero_saques': 0,
    'LIMITE_SAQUES': 3
}


def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def menu():
    opcoes = '''

Selecione uma opção:
                
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

=> '''
    return opcoes


def deposito(info):
    while True:
        limpar_tela()
        try:
            valor_deposito = float(input('Digite o valor do depósito: R$ '))
        except ValueError:
            print('Valor inválido!')
            input('Aperte "Enter" para continuar')
            continue

        if valor_deposito > 0:
            info['saldo'] += valor_deposito
            info['extrato'].append(f'Depósito: R$ {valor_deposito:,.2f}')
            print(f'\nValor de R$ {valor_deposito:,.2f} foi depositado em sua conta\n')
            input('Aperte "Enter" para continuar')
            break
            break
        elif valor_deposito == 0:
            print('Depósito cancelado!')
            input('Aperte "Enter" para continuar')
            break
        else:
            print('Valor inválido!')
            input('Aperte "Enter" para continuar')



def saque(info):
    while True:
        limpar_tela()
        if info['saldo'] <= 0:
            print('Saldo insuficiente!')
            break
        elif info['numero_saques'] >= info['LIMITE_SAQUES']:
            print('Limite de saques excedido!')
            input('Aperte "Enter" para continuar')
            break

        try:
            valor_saque = float(input('Digite o valor do saque: R$ '))
        except ValueError:
            print('Valor inválido!')
            input('Aperte "Enter" para continuar')
            continue

        if valor_saque > info['limite']:
            print(f'Valor excede o limite de saque! (LIMITE ATUAL: R$ {info["limite"]:,.2f})')
            input('Aperte "Enter" para continuar')
            continue
        elif valor_saque > info['saldo']:
            print('Saldo insuficiente para este saque!')
            input('Aperte "Enter" para continuar')
            break
        elif valor_saque == 0:
            print('Saque cancelado!')
            input('Aperte "Enter" para continuar')
            break
        else:
            info['saldo'] -= valor_saque
            info['numero_saques'] += 1
            info['extrato'].append(f'Saque: R$ {valor_saque:,.2f}')
            print(f'\nValor de R$ {valor_saque:,.2f} foi sacado de sua conta\n')
            input('Aperte "Enter" para continuar')
            break


def extrato(info):
    if len(info['extrato']) == 0:
        print('Conta sem movimentações!')
        input('Aperte "Enter" para continuar')
    else:
        print(('#' * 30) + '\n')
        print('EXTRATO\n'.center(30))
        for transacao in info['extrato']:
            print(transacao)
        print(f'\nSALDO ATUAL: R$ {info["saldo"]:,.2f}')
        print('\n' + ('#' * 30) + '\n')
    input('Aperte "Enter" para continuar')


def opcoes():
    return {
        'd': deposito,
        's': saque,
        'e': extrato,
        'q': 'sair'
    }


def selecionar_opcoes():
    opcoes_disponiveis = opcoes()
    opcao = input(menu()).lower()

    if opcao not in opcoes_disponiveis.keys():
        print('Opção inválida!')
        input('Aperte "Enter" para continuar')
        return None
    elif opcao == 'q':
        return opcao
    else:
        limpar_tela()
        opcoes_disponiveis[opcao](info)


def main():
    while True:
        limpar_tela()
        selecao = selecionar_opcoes()
        if selecao == 'q':
            limpar_tela()
            print('Obrigado por usar nosso sistema. Volte sempre!')
            break

if __name__ == '__main__':
    main()
