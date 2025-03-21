lista = []

for a in range(5):
    lista.append(input("Nome: "))

#Desafio
#Func. recurssiva p/ verif se o valor "Descomplica" está presente na lista

def descomplica(lista,index=0):
    if index >= len(lista):
        for nome in lista: 
            print(nome)
        return
    if lista[index]=='Descomplica':
        print(lista[index])
        return 0
    else:
        descomplica(lista, index+1)

descomplica(lista)