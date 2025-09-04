import os
from typing import Any
import time


info = {
    'limite': 500,
    'LIMITE_SAQUES': 3,
    'usuarios': [],
    'contas': [],
}


def limpar_tela() -> None:
    """Limpa a tela do terminal de acordo com o sistema operacional."""
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar_execucao(msg: str = 'Aperte "Enter" para continuar...') -> None:
    """Pausa a execução aguardando o usuário pressionar Enter."""
    input(msg)


# ---------------------- FUNÇÕES DE TRANSAÇÕES ----------------------

def deposito(saldo: float, extrato: list[str]) -> tuple[float, list[str]]:
    """Realiza um depósito na conta, validando o valor informado."""
    while True:
        limpar_tela()
        try:
            valor = float(input('Digite o valor do depósito: R$ '))
        except ValueError:
            print('Valor inválido!')
            pausar_execucao()
            continue

        if valor > 0:
            saldo += valor
            extrato.append(
                f'Depósito:{"." * (30 - (17 + len(f"{valor:,.2f}")))
                            }R$ {valor:,.2f} (+)'
            )
    
            limpar_tela()

            print(f'\nValor de R$ {valor:,.2f} foi depositado em sua conta\n')
            pausar_execucao()
            break

        elif valor == 0:
            print('Depósito cancelado!')
            pausar_execucao()
            break
        else:
            print('Valor inválido!')
            pausar_execucao()

    return saldo, extrato


def saque(*, saldo: float, extrato: list[str], numero_saques: int,
          limite: float, LIMITE_SAQUES: int) -> tuple[float, int, list[str]]:
    """Realiza um saque na conta, respeitando limites e saldo disponível."""
    while True:
        limpar_tela()

        if saldo <= 0:
            print('Saldo insuficiente!')
            pausar_execucao()
            break

        if numero_saques >= LIMITE_SAQUES:
            print('Limite de saques excedido!')
            pausar_execucao()
            break

        try:
            valor = float(input('Digite o valor do saque: R$ '))
        except ValueError:
            print('Valor inválido!')
            pausar_execucao()
            continue

        limpar_tela()
        if valor > limite:
            print(
                f'Valor excede o limite de saque! (LIMITE ATUAL: R$ {limite:,.2f})')
            pausar_execucao()
            continue
        elif valor > saldo:
            print('Saldo insuficiente para este saque!')
            pausar_execucao()
            break
        elif valor == 0:
            print('Saque cancelado!')
            time.sleep(1)
            break
        else:
            
            limpar_tela()

            saldo -= valor
            numero_saques += 1
            extrato.append(
                f'Saque:{"." * (30 - (14 + len(f"{valor:,.2f}")))
                         }R$ {valor:,.2f} (-)'
            )
            print(f'\nValor de R$ {valor:,.2f} foi sacado de sua conta\n')
            pausar_execucao()
            break

    return saldo, numero_saques, extrato


def exibir_extrato(saldo: float, /, *, extrato: list[str]) -> None:
    """Exibe o extrato da conta."""
    limpar_tela()
    if not extrato:
        print('Conta sem movimentações!')
    else:
        print('-' * 30)
        print('EXTRATO\n'.center(30))
        for transacao in extrato:
            print(transacao)
        print(
            f'\nSALDO ATUAL:{"." * (30 - (16 + len(f"{saldo:,.2f}")))
                             }R$ {saldo:,.2f}'
        )
        print('-' * 30)
        print('')

    pausar_execucao()


# ---------------------- FUNÇÕES DE CADASTRO ----------------------

def nova_conta(cpf: str, lista_contas: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Cria uma nova conta vinculada a um CPF já cadastrado."""
    limpar_tela()

    conta = {
        'cpf': cpf,
        'agencia': '0001',
        'conta':  len(lista_contas) + 1,
        'saldo': 0,
        'extrato': [],
        'numero_saques': 0,
    }

    lista_contas.append(conta)
    print('-' * 30)
    print(f'DETALHES DA CONTA\n'.center(30))
    print(detalhes := f'CPF:', (' ' *
          (29 - (len(detalhes) + len(conta["cpf"])))) + f'{conta["cpf"]}')
    print(detalhes := f'Agência:', (' ' * (29 - (len(detalhes) +
          len(conta["agencia"])))) + f'{conta["agencia"]}')
    print(detalhes := f'Conta Corrente:', (' ' * (29 -
          (len(detalhes) + len(f'{conta["conta"]}')))) + f'{conta["conta"]}')
    print('-' * 30)
    print('')
    input(f'Aperte "Enter" para continuar...')

    return lista_contas


def novo_usuario(cpf: str, lista_usuarios: list[dict[str, Any]],
                 lista_contas: list[dict[str, Any]]) -> tuple[list, list]:
    """Cadastra um novo usuário e já cria uma conta vinculada a ele."""
    while True:
        limpar_tela()
        if any(usuario['cpf'] == cpf for usuario in lista_usuarios):
            print('Usuário já cadastrado com este CPF!')
            opcao = input('Aperte "Enter" para continuar ou "q" para sair... ')
            if opcao.lower() == 'q':
                return lista_usuarios, lista_contas
        else:
            break

    nome = input('Digite o nome completo: ')
    nascimento = input('Digite a data de nascimento (DD/MM/AAAA): ')
    endereco = input(
        'Digite o endereço (logradouro, número - bairro - cidade/sigla estado): ')

    usuario = {
        'nome': nome.upper(),
        'data_nascimento': nascimento,
        'cpf': cpf,
        'endereco': endereco.upper()
    }

    lista_usuarios.append(usuario)

    lista_contas = nova_conta(cpf, lista_contas)
    return lista_usuarios, lista_contas


# ---------------------- FUNÇÕES DE MENU ----------------------

def menu(tipo: str, conta: str | None = None) -> str:
    """Exibe o menu de cadastro ou transações."""

    MENU_CADASTRO = '''Selecione uma opção:\n
[c] Cadastro de Usuário
[q] Sair
\n>>> '''

    MENU_TRANSACOES = f'''
--------------------
Conta Corrente:   {conta}
--------------------
\nSelecione uma opção:\n
[n] Nova Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
\n>>> '''

    limpar_tela()
    return input(MENU_CADASTRO if tipo == 'cadastro' else MENU_TRANSACOES).lower()


# ---------------------- FUNÇÕES DE APOIO ----------------------

def validar_cpf(cpf: str, lista_usuarios: list[dict[str, Any]]) -> bool:
    """Verifica se o CPF já está cadastrado no sistema."""
    return any(usuario['cpf'] == cpf for usuario in lista_usuarios)


def selecionar_conta(cpf: str, lista_contas: list[dict[str, Any]]) -> int:
    """Permite selecionar uma conta vinculada a um CPF."""
    contas = [c for c in lista_contas if c['cpf'] == cpf]

    while True:
        limpar_tela()
        if len(contas) > 1:
            print(f'Contas vinculadas ao CPF: {cpf}\n')
            for conta in contas:
                print(f"Conta Corrente: [{conta['conta']}] - Agência: {conta['agencia']}")

            try:
                escolha = int(input('\nSelecione o número da conta: '))
                conta = next((c for c in contas if c['conta'] == escolha), None)
                if conta:
                    return lista_contas.index(conta)
                else:
                    print('Conta inválida!')
                    pausar_execucao()
            except ValueError:
                print('Entrada inválida!')
                pausar_execucao()
        else:
            return lista_contas.index(contas[0])
        

def validar_usuario():
    """Gerencia o fluxo do acesso pelo CPF"""
        
    while True:
    
        limpar_tela()

        cpf = input('Digite seu CPF: ')
        if cpf != '':
            if cpf == 'q':
                return 'q'
            if not validar_cpf(cpf, info['usuarios']):
                print('Usuário não cadastrado!')
                time.sleep(1)
                selecao = menu('cadastro')
                if selecao:
                    if selecao == 'q':
                        return 'q'
                    selecionar_opcoes(cpf, selecao, conta=None)
                    return cpf
            else:
                return cpf


# ---------------------- CONTROLE PRINCIPAL ----------------------

def selecionar_opcoes(cpf: str, opcao: str, conta: int | None) -> None:
    """Executa a opção escolhida pelo usuário."""

    if opcao not in ['c', 'n', 'd', 's', 'e', 'q']:
        print('Opção inválida!')
        pausar_execucao()
        return

    if opcao == 'c':
        info['usuarios'], info['contas'] = novo_usuario(
            cpf, info['usuarios'], info['contas'])
    elif opcao == 'n':
        info['contas'] = nova_conta(cpf, info['contas'])

    elif opcao == 'd' and conta is not None:
        conta_atual = info['contas'][conta]
        conta_atual['saldo'], conta_atual['extrato'] = deposito(
            conta_atual['saldo'], conta_atual['extrato'])
        
    elif opcao == 's' and conta is not None:
        conta_atual = info['contas'][conta]
        conta_atual['saldo'], conta_atual['numero_saques'], conta_atual['extrato'] = saque(
            saldo=conta_atual['saldo'],
            extrato=conta_atual['extrato'],
            numero_saques=conta_atual['numero_saques'],
            limite=info['limite'],
            LIMITE_SAQUES=info['LIMITE_SAQUES']
        )

    elif opcao == 'e' and conta is not None:
        conta_atual = info['contas'][conta]
        exibir_extrato(conta_atual['saldo'], extrato=conta_atual['extrato'])


def main():
    """Loop principal do sistema bancário."""
    while True:
        limpar_tela()

        print('\nBem-vindo!\n')
        pausar_execucao('Aperte "Enter" para iniciar...')

        cpf = validar_usuario()
        
        if cpf != 'q': 

            while True:

                conta = selecionar_conta(cpf, info['contas'])
            
                selecao = menu('outros', str(conta + 1))

                if selecao != 'q':
                    selecionar_opcoes(cpf, selecao, conta)
                else:
                    break
    
        limpar_tela()
        print('Obrigado por usar nosso sistema. Volte sempre!\n')
        time.sleep(1)
        pass

if __name__ == '__main__':
    main()
