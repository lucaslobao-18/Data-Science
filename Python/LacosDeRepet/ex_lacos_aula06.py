aluno=[]
a=1
for a in range(1):
    aluno.append(input("insira o nome do aluno: "))
    aluno.append(input("insira o cpf do aluno: "))
    aluno.append(input("insira o email do aluno: "))
    aluno.append(input("insira a matrícula do aluno: "))

    notas=[]
    notas.append(int(input("Insira a primeira nota: ")))
    notas.append(int(input("Insira a segunda nota: ")))
    notas.append(int(input("Insira a terceira nota: ")))

    media=(notas[0]+notas[1]+notas[2])/3
    if media<6:
        notas.append(int(input("Insira a quarta nota: ")))
        media=(notas[0]+notas[1]+notas[2]+notas[3])/4
        if media<6:
            status="Reprovado"
            print("Reprovado")
        else:
            status="Aprovado"
            print("Aprovado")
    else:
        status="Aprovado"
        print("aprovado")

    aluno.append(notas)
    aluno.append(status)

    print(aluno)
    # alunos.append(aluno)

# print(alunos)
# print(aluno[4] from alunos[0])