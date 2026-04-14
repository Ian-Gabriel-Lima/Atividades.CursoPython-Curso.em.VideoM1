#aça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input("digite uma frase: ")).upper().strip()
print(frase.count("A"))
print("A primeira aparição de A foi: {}".format(frase.find("A")+1))
print("A ultima aparição de A foi: {}".format(frase.rfind("A")+1))
