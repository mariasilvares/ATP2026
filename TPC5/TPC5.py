def menu():
    print("0: Sair da aplicação")
    print("1: Criar uma turma")
    print("2: Inserir um aluno na turma")
    print("3: Listar a turma")
    print("4: Consultar um aluno por id")
    print("8: Guardar a turma em ficheiro")
    print("9: Carregar uma turma dum ficheiro")
    op=int(input("Escolha a opção do menu: "))
    return(op)


def criarTurma():
    turma=[]
    n=int(input("Quantos alunos deseja adicionar na sua turma? "))
    a=1

    while n>0:
        nome=input(f"Insira o nome do {a}º aluno: ")
        id=int(input("Insira o número do aluno: "))
        notaTPC=int(input("Insira a nota do TPC do aluno: "))
        notaProj=int(input("Insira a nota do Projeto: "))
        notaTeste=int(input("Insira a nota do Teste: "))

        notas=[notaTPC, notaProj, notaTeste]
        aluno=(nome, id, notas)
        turma.append(aluno)

        a=a+1
        n=n-1

    return(turma)


def inserirAluno(turma):
    nome=input("Insira o nome do aluno: ")
    id=int(input("Insira o número do aluno: "))
    notaTPC=int(input("Insira a nota do TPC do aluno: "))
    notaProj=int(input("Insira a nota do Projeto: "))
    notaTeste=int(input("Insira a nota do Teste: "))

    notas=[notaTPC, notaProj, notaTeste]
    aluno=(nome, id, notas)
    turma.append(aluno)


def listarTurma(turma):
    for aluno in turma:
        nome=aluno[0]
        id=aluno[1]
        notas=aluno[2]

        notaTPC=notas[0]
        notaProj=notas[1]
        notaTeste=notas[2]

        print(f"Nome: {nome}, id: {id}, notaTPC: {notaTPC}, notaProj: {notaProj}, notaTeste: {notaTeste}")


def consultarAluno(turma):
    id=int(input("Insira o id do aluno que deseja consultar: "))
    i=0
    res=-1

    while i<len(turma) and id!=turma[i][1]:
        i=i+1

    if i<len(turma):
        res=i

    if res!=-1:
        print(turma[res])
    else:
        print("Aluno não encontrado.")


def guardarTurma(turma, fnome):
    file=open(fnome, "w")

    for aluno in turma:
        nome=aluno[0]
        id=aluno[1]
        notas=aluno[2]

        file.write(f"{nome};{id};{notas[0]};{notas[1]};{notas[2]}\n")

    file.close()


def carregarTurma(fnome):
    turma=[]
    file=open(fnome, "r")

    for linha in file:
        dados=linha.strip().split(";")

        nome=dados[0]
        id=int(dados[1])
        notaTPC=int(dados[2])
        notaProj=int(dados[3])
        notaTeste=int(dados[4])

        notas=[notaTPC, notaProj, notaTeste]
        aluno=(nome, id, notas)
        turma.append(aluno)

    file.close()
    return(turma)


turma=[]
op=-1

while op!=0:
    op=menu()

    if op==1:
        turma=criarTurma()
        print("Turma criada com sucesso.")

    elif op==2:
        inserirAluno(turma)
        print("Aluno inserido com sucesso.")

    elif op==3:
        listarTurma(turma)

    elif op==4:
        consultarAluno(turma)

    elif op==8:
        guardarTurma(turma, "turma.txt")
        print("Turma guardada com sucesso.")

    elif op==9:
        turma=carregarTurma("turma.txt")
        print("Turma carregada com sucesso.")

    elif op==0:
        print("A sair da aplicação...")

    else:
        print("Opção inválida.")