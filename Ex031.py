#pergunte a distancia de uma viagem em kms, calcule o preço cobrando 0,50 por km para 200km e mais longas 0,45.

distancia = float(input("Quantos kms é a sua viagem?: "))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print("O Valor da sua passagem será de R${:.2f}".format(preco))