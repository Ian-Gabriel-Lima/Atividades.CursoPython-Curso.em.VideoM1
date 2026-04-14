# digite um salario e calcule um aumento: para salarios maiores que 1250 um aumento de 10%, para inferiores 15%
salario = float(input("Qual o seu salario: "))

if salario > 1250.00:
    nv_salario = salario + (salario * 10 / 100)
else:
    nv_salario = salario + (salario * 15 / 100)

print("Seu novo salário é de R${:.2f}".format(nv_salario))