import random
computador=random.randint(0,50)
print("Sou seu computador,acabei de pensar em um numero..... entre 0 a 50")
print(" Tente Advinhar em que numero eu pensei")
acertou =False
tentavias=0
while not acertou:
      jogador=int(input("Qual é o seu palpite"))
      tentavias+=1
      if jogador==computador:
          acertou=True
      else:
          if jogador>computador:
              print("Menos")
          elif jogador<computador:
              print("Mais")
print("Parabéns você ganhou em {} tentativas. ".format(tentavias))


