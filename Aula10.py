# Aula 10 estruturas condicionais / aula teórica

nome = str(input('Digite seu nome: ')).strip()
if nome.lower() == 'gustavo':
    print("Que nome lindo")
else:
    print("Seu nome é FEZES!")
print("Bom dia {}!".format(nome))


#|||||||||||||||||||||||||||||||||||||||||||||||||

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2)/2
print("A sua média foi {:.1f}".format(media))
print("parabéns" if media >= 6 else "estude mais vagabundo!")