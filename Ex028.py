# faça o computador pensar em um número entre 0 e 5 e peça para o user tentar descobrir qual é, depois imprima uma mensagem dizendo se ele venceu ou perdeu
from random import randint
num = randint(0,5)
chute = int(input("Digite um número entre 0 e 5: "))
if chute == num:
    print("ACERTOU!")
    print("Cagão")
else:
    print("ERROU!")
    print("Tente novamente!")
print("o numero era: {} e você chutou: {}!".format(num, chute))