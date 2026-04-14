#digite 3 retas e diga se forma um triangulo.
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
if a + b > c and a + c > b and b + c > a:
    print("É possível montar um triângulo")
else:
    print("Não é possível montar um triângulo")