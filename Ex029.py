# escreva um programa que leia a velocidade de um carro. se ultrapassar 80kmh a multa vai custar 7.00 por km acima do limite.
print("APLICADOR DE MULTAS")
print("limite 80km´s por hora!")
velocidade = int(input("Qual era a velocidade do carro?: "))
if velocidade > 80:
    excedente = velocidade - 80
    multa = excedente * 7.00
    print("Multado! O valor da sua multa é de R${:.2f}".format(multa))
else:
    print("Você estava dentro do limite de velocidade! continue assim!")
