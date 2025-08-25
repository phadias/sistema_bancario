# 💰 Sistema Bancário em Python

Este projeto foi desenvolvido como parte do **Desafio do Bootcamp Suzano - Python Developer #2** na [Digital Innovation One (DIO)](https://www.dio.me/).  

O objetivo é implementar um sistema bancário simples em **Python**, utilizando conceitos básicos da linguagem, como variáveis, funções, estruturas condicionais e loops.

---

## 🚀 Funcionalidades

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

- **Sair**
  - Encerra o programa de forma amigável.

---

## 🛠️ Estrutura do Código

- `deposito(info)`: Função responsável por depósitos.  
- `saque(info)`: Função responsável pelos saques, com controle de limite.  
- `extrato(info)`: Mostra todas as transações e o saldo.  
- `menu()`: Exibe as opções do usuário.  
- `limpar_tela()`: Limpa o terminal (compatível com Windows e Linux).  
- `main()`: Função principal que mantém o loop do sistema.  

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
   
2. Acesse a pasta do projeto:
   ```bash
   cd sistema-bancario

3. Execute o programa:
   ```bash
   python main.py


---

## 📸 Exemplo de Uso
  ```bash
     Selecione uma opção:
     
     [d] Depósito
     [s] Saque
     [e] Extrato
     [q] Sair
     
     => d
     Digite o valor do depósito: R$ 100
     Valor de R$ 100.00 foi depositado em sua conta
