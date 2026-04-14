# Crie um programa que leia o nome de uma cidade e diga se começa com SANTO

cid = str(input("digite o nome da cidade: ")).strip()
print(cid[:5].upper() == "SANTO")

