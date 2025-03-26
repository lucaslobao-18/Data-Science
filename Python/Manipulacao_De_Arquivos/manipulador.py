conteudo = open("texto.txt", "a")
conteudo.write("\nNovaS linha escrita")
conteudo.close()

conteudo = open("texto.txt","r")
print(conteudo.read())
conteudo.close()

# Flags para usar com o comando OPEN
# R = READ
# W = WRITE
# X = EXECUTE
# A = APPEND
# R+
# WB = Write Binary