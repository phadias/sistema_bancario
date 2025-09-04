# 💰 Sistema Bancário em Python

Este projeto foi desenvolvido como parte do **Desafio do Bootcamp Suzano - Python Developer #2** na [Digital Innovation One (DIO)](https://www.dio.me/).  

O objetivo é implementar um sistema bancário simples em **Python**, utilizando conceitos como variáveis, funções, estruturas condicionais, loops e manipulação de listas e dicionários.

---

## 🚀 Funcionalidades

- **Cadastro de Usuário**
  - Cria um novo usuário com CPF, nome, data de nascimento e endereço.
  - Cada novo usuário já recebe automaticamente uma conta.

- **Cadastro de Conta**
  - Permite criar múltiplas contas vinculadas a um mesmo CPF.

- **Depósito**
  - Permite adicionar valores à conta.
  - Não aceita valores negativos.

- **Saque**
  - Permite realizar saques até um limite definido.
  - Restrição de quantidade máxima de saques por dia.
  - Impede saque de valor maior que o saldo disponível.

- **Extrato**
  - Lista todas as movimentações (depósitos e saques).
  - Mostra o saldo atual ao final.

- **Menu interativo**
  - Separa opções de **cadastro** e de **transações**.
  - Exibe as contas vinculadas a um CPF e permite selecionar qual utilizar.

- **Sair**
  - Encerra o programa de forma amigável.

---

## 🛠️ Estrutura do Código

- `limpar_tela()`: Limpa o terminal (compatível com Windows e Linux).  
- `pausar_execucao()`: Pausa até o usuário pressionar Enter.  
- `deposito(saldo, extrato)`: Realiza depósitos na conta.  
- `saque(saldo, extrato, numero_saques, limite, LIMITE_SAQUES)`: Executa saques com regras de limite e saldo.  
- `exibir_extrato(saldo, extrato)`: Mostra todas as transações e o saldo.  
- `novo_usuario(cpf, usuarios, contas)`: Cadastra um novo usuário e já cria uma conta vinculada.  
- `nova_conta(cpf, contas)`: Cria uma nova conta para um CPF existente.  
- `validar_cpf(cpf, usuarios)`: Verifica se o CPF já existe.  
- `selecionar_conta(cpf, contas)`: Permite escolher entre múltiplas contas do mesmo CPF.  
- `validar_usuario()`: Gerencia o acesso via CPF.  
- `menu(tipo, conta=None)`: Exibe menus de cadastro ou transações.  
- `selecionar_opcoes(cpf, opcao, conta)`: Executa a ação escolhida no menu.  
- `main()`: Loop principal do sistema bancário.

---

## 📂 Estrutura do Projeto

📦 sistema-bancario  
┣ 📜 main.py # Código principal  
┣ 📜 README.md # Documentação do projeto  

---

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/sistema-bancario.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd sistema-bancario
   ```
3. Execute o programa:
   ```bash
   python main.py
   ```

---

## 📸 Exemplo de Uso
```bash
--------------------
Conta Corrente:   1
--------------------

Selecione uma opção:

[n] Nova Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

>>> d
Digite o valor do depósito: R$ 100
Valor de R$ 100.00 foi depositado em sua conta
```
