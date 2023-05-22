import random

numero_secreto = random.randint(1,100)
total_de_tentativas = 0 
pontos = 1000
pontos_perdidos = 0 


print('----Nivel de Dificuldade-----')
print('(1) Fácil (2) Médio (3) Difícil')

nv = input('Escolha o nível:')

if nv == 1:
    total_de_tentativas = 10
elif nv == 2:
    total_de_tentativas = 5
else:
    total_de_tentativas = 2


for rodada in range(1, total_de_tentativas+1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite o seu número entre 1  e 100\n")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    if(chute<1 or chute>100):
        print("Intervalo invalido")
        continue
        #Pula para proxima tentativa

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns! Você acertou! Pontos {} ".format(pontos))
        break
        #Parada imediata
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")
        pontos_perdidos = numero_secreto - chute
        pontos = pontos - abs(pontos_perdidos)

print("Fim do jogo")