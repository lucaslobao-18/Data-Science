# IF/ELSE
# Match
# Ternários

#IF/ELSE
a = 3 
if a<5:
    a = 2+2
else:
    a = 1+1

# # TERNÁRIO, condicionais com apenas 3 saidas, e deixar a sintaxe mais limpa (gasta menos linhas)
# idade = int(input("digite sua idade: "))
# print("É MAIOR") if idade >= 18 else print("É MENOR")

#Match Case (Switch Case)
a = "Marcio"
match a:
    case "Antonio":
        print("Não é Marcio")
    case "Marcio":
        print("É Marcio")

