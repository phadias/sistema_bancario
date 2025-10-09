from abc import ABC,  abstractmethod
from datetime import datetime
import os
import textwrap
import time


class Cliente:
    def __init__(self, endereco: str) -> None:
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta: int, transacao):
        transacao.registrar(conta)

    def adicionar_contas(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf: int, nome: str, data_nascimento: str, endereco: str) -> None:
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero: int, cliente) -> None:
        self._saldo = 0
        self._numero = numero
        self._agencia  = '0001'
        self._cliente =  cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, numero: int, cliente):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor: int) -> bool:
        saldo: int = self.saldo
        excedeu_saldo: bool = valor > self.saldo
    
        if excedeu_saldo:
            print("Saldo insulficiente!")
        
        elif valor > 0:
            self._saldo -=  valor
            print('Saque realizado com  sucesso!')
            return True
        else:
            print('Valor inválido')
        
        return False

    def depositar(self, valor: int) -> bool:
        if valor > 0:
            self._saldo += valor
            return  True
        else:
            print('Valor inválido')
            return False
    
class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente, limite: int=500, limite_saques: int=3) -> None:
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def sacar(self, valor: int):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saque = numero_saques > self.limite_saques

        if excedeu_limite:
            print(f'Valor do saque excede o limite - LIMITE: {self.limite}')
        elif excedeu_saque:
            print(f'Número máximo de saques excedido - LIMITE DE SAQUE: {self.limite_saques}')
        else:
            return super().sacar(valor)
        
        return False

    def __str__(self) -> str:
        return f'''\
                Agência: \t{self.agencia}
                C/C: \t\t{self.agencia}
                Titular: \t{self.cliente.nome}
                '''
    
class Historico:
    def __init__(self) -> None:
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                'tipo': transacao.__class__.__name__,
                'valor': transacao.valor,
                'data': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            }
        )

class Transacao(ABC):      
        @property
        @abstractmethod
        def valor(self):
            pass

        @abstractmethod
        def registrar(self, conta):
            pass

class Saque(Transacao):
    def __init__(self, valor) -> None:
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao  = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
        

# ---------------------- FUNÇÕES DE MENU ----------------------

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def menu(x) -> str:
    """Exibe o menu de cadastro ou transações."""

    MENU_TRANSACOES = f'''
\nSelecione uma opção:\n
[c] Cadastro Usuário
[n] Nova Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
\n>>>'''

    limpar_tela()
    return input(MENU_TRANSACOES).lower()

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if str(cliente.cpf) == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print('\nCliente não possui conta!')
        return
    
    return cliente.contas[0]
        
def depositar(clientes):
    cpf = input('Informe o CPF do Cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        limpar_tela()
        print('\nCliente não encontrado!')
        input('Aperte Enter para voltar ao menu...')
        return
    
    valor = float(input('Informe o valor do depósito: '))
    transacao = Deposito(valor)

    limpar_tela()

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        input('Aperte Enter para voltar ao menu...')
        return
    
    cliente.realizar_transacao(conta, transacao)
    print('\nDepósito realizado com sucesso!')
    input('Aperte Enter para voltar ao menu...')
    


def sacar(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    limpar_tela()

    if not cliente:
        print('\nCliente não encontrado!')
        input('Aperte Enter para voltar ao menu...')
        return

    valor = float(input('Informe o valor do saque: '))
    transacao = Saque(valor)

    limpar_tela()

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        input('Aperte Enter para voltar ao menu...')
        return
    
    cliente.realizar_transacao(conta, transacao)
    input('Aperte Enter para voltar ao menu...')

def exibir_extrato(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    limpar_tela()

    if not cliente:
        print('\nCliente não encontrado!')
        input('Aperte Enter para voltar ao menu...')
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        input('Aperte Enter para voltar ao menu...')
        return
    
    print('\n', 'EXTRATO'.center(30, '-'))
    transacoes = conta.historico.transacoes

    extrato = ''

    if not transacoes:
        extrato = 'Não foram realizadas movimentações.'
        input('Aperte Enter para voltar ao menu...')
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}: R$ {transacao['valor']:.2f}"

    print(extrato)
    print(f'\nSaldo Atual:R$ {conta.saldo:.2f}')
    print('-' * 30)
    input('Aperte Enter para voltar ao menu...')

def cadastrar_conta(nova_conta, clientes, contas):

    limpar_tela()

    cpf = input('Informe o CPF do ciente: ')
    cliente = filtrar_cliente(cpf=cpf, clientes=clientes)

    limpar_tela()

    if not cliente:
        print('\nCliente não encontrado!')
        input('\nAperte Enter para voltar ao menu...')
        return
    
    conta = ContaCorrente(numero=nova_conta, cliente=cliente)
    contas.append(conta)
    cliente.contas.append(conta)

    limpar_tela()

    print('\nConta criada com sucesso!')
    input('Aperte Enter para voltar ao menu...')

def listar_contas(contas):
    for conta in contas:
        print('-'*100)
        print(textwrap.dedent(str(conta)))

    limpar_tela()

def cadastrar_cliente(clientes: list):

    limpar_tela()

    cpf=int(input('\nInforme o CPF (somente números):'))
    cliente=filtrar_cliente(cpf=cpf, clientes=clientes)

    limpar_tela()

    if cliente:
        print('\nCliente já cadastrado')
        input('Aperte Enter para voltar ao menu...')
        return
    
    nome=input('Informe o nome completo: ')

    limpar_tela()

    data_nascimento=input('Infome a data de nascimento (dd-mm-aaaa): ')

    limpar_tela()

    endereco=input('Informe o endereço (logradouro - numero - bairro - cidade/sigla estado): ')

    limpar_tela()

    cliente = PessoaFisica(cpf=cpf, nome=nome, data_nascimento=data_nascimento, endereco=endereco)
    
    clientes.append(cliente)

    print('O Cliente foi cadastrado!')
    input('Aperte Enter para voltar ao menu...')
    
def main():
    clientes = []
    contas= []

    while True:

        limpar_tela()

        print('\nBem-vindo!\n')
        input('Aperte "Enter" para iniciar...')

        selecao = menu(clientes)

        if selecao == 'd':
            depositar(clientes)

        if selecao == 's':
            sacar(clientes)

        if selecao == 'e':
            exibir_extrato(clientes)

        if selecao == 'c':
            cadastrar_cliente(clientes)

        if selecao == 'n':
            nova_conta = len(contas) + 1
            cadastrar_conta(nova_conta, clientes, contas)

        if selecao == 'q':
            limpar_tela()
            print('Obrigado por usar nosso sistema. Volte sempre!\n')
            time.sleep(2)
            pass

if __name__ == '__main__':
    main()