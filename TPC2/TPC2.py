import random

m=int(input("Qual a modalidade que deseja? (1/2)"))
p=0

#Computador pensa num número e o utilizador tenta adivinhar 
if m==1:
    n=int(random.randint(0,100))
    x=101
    while x!=n:
        x=int(input("Adivinhe o número entre 0 e 100"))
        p=p+1
        if x>n:
            print("O número que pensei é Menor")
        elif x<n:
            print("O número que pensei é Maior")
        else:
            print(f"Acertou - o número de tentativas foi {p}")

#Utilizador pensa num número e o computador tenta adivinhar
if m==2:
    n=int(input("Pense e introduza um número inteiro entre 0 e 100"))
    min=0
    max=100
    r="resposta"

    while r!="Acertou":
        x=int(random.randint(min,max))
        r=input(f"O número que pensou é {x}? (O número que pensei é Menor/O número que pensei é Maior/Acertou)")
        p=p+1
        if r=="O número que pensei é Menor":
            max=x-1
        elif r=="O número que pensei é Maior":
            min=x+1
        else:
            print(f"O número de tentativas foi {p}")

