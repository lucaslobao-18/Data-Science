ano_nasc = int(input("Qual é o sue ano de nascimento?"))
ano_atual = int(input("Ano atual:"))
idade = ano_atual-ano_nasc

if idade >= 18:
    print("Precisamos do título de eleitor")
else:
    print("precisamos do documento do responsável")