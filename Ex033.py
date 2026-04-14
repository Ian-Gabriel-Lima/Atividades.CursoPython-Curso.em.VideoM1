# leia 3 numeros e mostre qual é o maior e o menor
n1 = int(input("numero 1: "))
n2 = int(input("numero 2: "))
n3 = int(input("numero 3: "))
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
print("O maior é {}, e o menor é {}".format(maior, menor))
