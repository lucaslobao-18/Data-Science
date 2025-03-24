from conta import ContaBancaria
import os

print("Bem vindo ao LucasBank")
username = input("insira seu nome: ")

c = ContaBancaria(username,0)
i=0
print("Bem vindo(a) a sua conta",c.titular)
while i==0:
    print("1 - Deposito")
    print("2 - Saque")
    print("3 - Ver Saldo")
    print("4 - Sair")
    op = int(input("Digite o número da operação: "))

    match op:
        case 1:
            os.system('cls')
            valor = int(input("Insira o valor do depósito: "))
            print(c.depositar(valor))
        case 2:
            os.system('cls')
            valor = int(input("Insira o valor do saque: "))
            print(c.sacar(valor))
        case 3:
            os.system('cls')
            print(c.exibir_saldo())
        case 4:
            os.system('cls')
            print("Obrigado, até logo")
            i = 1
