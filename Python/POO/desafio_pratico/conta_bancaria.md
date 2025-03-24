## Exercício: Sistema de Conta Bancária
Crie um programa em Python que modele um sistema bancário simples usando Programação Orientada a Objetos (POO). O sistema deve conter:

Uma classe ContaBancaria com os seguintes atributos e métodos:

Atributos:
- titular (nome do dono da conta)
- saldo (valor inicial da conta, padrão: 0)

Métodos:
- depositar(valor): adiciona um valor ao saldo.
- sacar(valor): subtrai um valor do saldo (se houver saldo suficiente).
- exibir_saldo(): imprime o saldo atual.

Criação de uma conta e realização de operações:

Criar uma conta para um usuário fictício.

Realizar depósitos e saques.

Exibir o saldo após cada operação.

Exemplo de uso esperado:


```
conta = ContaBancaria("João Silva", 1000)
conta.depositar(500)
conta.sacar(300)
conta.exibir_saldo()
```

### Saída
````
Depósito de R$500 realizado. Novo saldo: R$1500
Saque de R$300 realizado. Novo saldo: R$1200
Saldo atual: R$1200
````