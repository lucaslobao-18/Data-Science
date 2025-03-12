# def é a palavra reservada para criar a função

# def soma(a,b):
#     c = a + b
#     return c

# print(soma(int(input("insira o num1: ")),int(input("insira o num2: "))))

# Recursividade, Ex: Fatorial
def fatorial(num):
    if num == 1:
        return 1
    else:
        return num * fatorial(num - 1)

print(fatorial(5))

## Funções nativas muito utilizadas
# abs(): retorna o valor absoluto de um número;
# pow(): realiza cálculos de potência;
# next(): retorna o próximo elemento de uma lista iterativa
# hash(): retorna o valor em hash de um objeto
# open(): permite trabalhar com arquivos (veremos isso mais adiante!)