# mostre se o ano é bissexto
ano = int(input("Digite o ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("{} é bissexto".format(ano))
else:
    print("{} este ano não é bissexto".format(ano))