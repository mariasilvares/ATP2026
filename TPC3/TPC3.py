import random

# Corrida para o 100
m=int(input("Qual a modalidade que deseja? (1/2)"))

# Computador joga primeiro (deverá ganhar sempre)
if m==1:
    n=1
    print(f"Jogo o número 1 e a soma é {n}")
    while n!=100:
        jogador=int(input("Insira um número entre 1 e 10"))
        while (jogador<1) or (jogador>10):
            jogador=int(input("Número inválido, insira um número entre 1 e 10"))
        computador=11-jogador
        n=n+jogador+computador
        print(f"Jogo o número {computador} e a soma é {n}")
    print("Ganhei!")

# Computador joga em segundo lugar (poderá ganhar ou não dependendo das jogadas do outro)
if m==2:
    n=0
    while n!=100:
        jogador=int(input("Insira um número entre 1 e 10"))
        while (jogador<1) or (jogador>10) or (n+jogador>100):
            jogador=int(input("Número inválido, insira um número entre 1 e 10"))
        n=n+jogador
        if n==100:
            print("Ganhaste!")
        else:
            computador=(1-n)%11
            if computador==0:
                computador=random.randint(1,10)
            if n>=90:
                computador=100-n
            n=n+computador
            print(f"Jogaste o número {jogador}, jogo o número {computador} e a soma é {n}")
            if n==100:
                print("Ganhei!")
