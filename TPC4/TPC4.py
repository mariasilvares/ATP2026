import random

def menu():
    print ("Menu")
    print ("(0) Sair")
    print ("(1) Criar Lista")
    print ("(2) Ler Lista")
    print ("(3) Soma")
    print ("(4) Média")
    print ("(5) Maior")
    print ("(6) Menor")
    print ("(7) estaOrdenada por ordem crescente")
    print ("(8) estaOrdenada por ordem decrescente")
    print ("(9) Procura um elemento")


def criarLista ():
    lista=[]
    comp=random.randint(1,20)
    while comp>0:
        n=random.randint(1,100)
        lista.append(n)
        comp=comp-1
    return lista

def lerLista():
    lista=[]
    continuar="s"
    while continuar=="s":
        n=int(input("Introduza um número inteiro: "))
        lista.append(n)
        continuar=input("Deseja adicionar mais algum número à sua lista? (s/n): ")
    return lista

def soma (lista):
    i=0
    soma=0
    while i<len(lista):
        soma=soma+lista[i]
        i=i+1
    return soma

def média (lista):
    i=0
    soma=0
    while i<len(lista):
        soma=soma+lista[i]
        i=i+1
    média=soma/len(lista)
    return média

def maior(lista):
    i=0
    maior=lista[0]
    while i<len(lista):
        if lista[i]>maior:
            maior=lista[i]
        i=i+1
    return maior

def menor(lista):
    i=0
    menor=lista[0]
    while i<len(lista):
        if lista[i]<menor:
            menor=lista[i]
        i=i+1
    return menor

def ordenaCrescente(lista):
    lista=lista.copy()
    trocas=True
    while trocas==True:
        trocas=False
        i=0
        while i<len(lista)-1: 
            if lista[i]>lista[i+1]:
                temporário=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=temporário
                trocas=True
            i=i+1
    return lista

def ordenaDecrescente(lista):
    lista=lista.copy()
    trocas=True
    while trocas==True:
        trocas=False
        i=0
        while i<len(lista)-1: 
            if lista[i]<lista[i+1]:
                temporário=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=temporário
                trocas=True
            i=i+1
    return lista

def procuraElemento(lista, elem):
    i=0
    res=-1
    while i<len(lista) and elem!=lista[i]:
        i=i+1
    if i<len(lista):
        res=i
    return res

def opção():
    listaatual=[]
    op=-1
    while op!=0:
        menu()
        op = int(input("Escolha uma opção: "))

        if op==1:
            listaatual=criarLista()
            print(f"Lista criada com sucesso: {listaatual}")

        elif op==2:
            listaatual=lerLista()
            print(f"Lista guardada com sucesso: {listaatual}")

        elif op==3:
            if len(listaatual)==0:
                print("A lista está vazia.")
            else:
                print(f"Soma dos elementos: {soma(listaatual)}")

        elif op==4:
            if len(listaatual)==0:
                print("A lista está vazia.")
            else:
                print(f"Média dos elementos: {média(listaatual)}")

        elif op==5:
            if len(listaatual)==0:
                print("A lista está vazia.")
            else:
                print(f"Maior elemento: {maior(listaatual)}")

        elif op==6:
            if len(listaatual)==0:
                print("A lista está vazia.")
            else:
                print(f"Menor elemento: {menor(listaatual)}")

        elif op==7:
            if len(listaatual)==0:
                print("A lista está vazia.")
            else:
                print(ordenaCrescente(listaatual))

        elif op==8:
            if len(listaatual)==0:
                print("A lista está vazia.")
            else:
                print(ordenaDecrescente(listaatual))
  
        elif op==9:
            if len(listaatual)==0:
                print("A lista está vazia.")
            else:          
                elem=int(input("Qual o elemento que pretende procurar?"))
                print(f"Posição do elemento (-1 se não existir): {procuraElemento(listaatual, elem)}")
            
        elif op==0:
            print("A terminar o programa. Até Breve!")

        else:
            print("Opção Inválida!")
            
opção()
