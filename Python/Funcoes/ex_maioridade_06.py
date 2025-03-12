#verifica maioridade

# def maioridade(num):
#     if num < 18:
#         print("Menor de idade")
#     else:
#        print("Maior de idade")

# maioridade(18)

def contagem_crescente(num):
    if num >= 10:
        if num == 10:
            print(num)
        return 0
    else:
        print(num)
        num = num + 1
        contagem_crescente(num)

def contagem_regressiva(num):
    if num <= 0:
        if num == 0:
            print(num)
        return 0
    else:
        print(num)
        num = num - 1
        contagem_regressiva(num)

print("Regressiva...")
contagem_regressiva(10)
print("Crescente...")
contagem_crescente(0)